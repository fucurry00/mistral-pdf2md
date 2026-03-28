#!/usr/bin/env python3
"""
fix_ocr_math_md.py — OCR済み数学系Markdownの一括クリーンアップ

用途:
  数学の教科書PDFをOCR→Markdown変換した後に残る典型的なアーティファクトを
  一括修正する。特にLaTeX数式を多用する代数学・幾何学系のテキストを想定。

使い方:
  python fix_ocr_math_md.py <対象ディレクトリ>
  python fix_ocr_math_md.py <file.md> [file2.md ...]
  python fix_ocr_math_md.py <対象ディレクトリ> --dry-run   # 変更せず差分だけ表示
  python fix_ocr_math_md.py <対象ディレクトリ> --verbose    # 各修正の詳細を表示
  python fix_ocr_math_md.py <file.md> -o cleaned.md        # 出力先を指定

  # 特定の修正のみ適用（カンマ区切り）
  python fix_ocr_math_md.py <dir> --only=html_entities,spaced_text,text_spacing

  # 画像参照の処理方法を指定
  python fix_ocr_math_md.py <dir> --image-mode=comment   # <!-- Figure: ... -->（デフォルト）
  python fix_ocr_math_md.py <dir> --image-mode=delete    # 完全削除
  python fix_ocr_math_md.py <dir> --image-mode=placeholder  # [Figure] に置換

  # ページヘッダとして除去する著者名を指定
  python fix_ocr_math_md.py <dir> --page-header-author="Andreas Gathmann"

  # 書籍プリセットを使用（running headersを自動除去）
  python fix_ocr_math_md.py <dir> --preset dummit-foote

  # カスタムヘッダパターンを指定
  python fix_ocr_math_md.py <dir> --header-pattern "^Chapter \\d+" --header-pattern "^Section \\d+"

修正対象:
  1. html_entities      : &gt; &lt; &amp; → > < &（LaTeX数式のレンダリング破壊を修復）
  2. tab_corruption     : TAB+ext{ → \\text{（Python文字列処理で起きがちな\\t化けの修復）
  3. spaced_text        : \\text{f o r a l l} → \\text{for all}（OCRの文字間スペース挿入を修復）
  4. text_spacing       : \\text{for} → \\text{ for }（数式モード内の接続詞にスペース付与）
  5. separators         : --- ページ区切りの除去（--no-remove-separators で無効化）
  6. running_headers    : running headers/footers の除去（--preset / --header-pattern）
  7. image_refs         : ![img-*](images/*) → コメント化/削除/プレースホルダ
  8. page_headers       : 著者名単独行・ALL CAPSセクションヘッダの除去
  9. page_break_headers : ---直後の裸のチャプタータイトル繰り返しの除去
  10. empty_headings    : 中身のない ## の除去
  11. page_numbers      : 孤立したページ番号（アラビア数字・ローマ数字）の除去
  12. dollar_artifacts  : $$ $$ のような空の数式ブロックの除去
  13. standalone_dots   : 白紙ページ跡の孤立ドットの除去
  14. excessive_blanks  : 4行以上の連続空行を2行に圧縮

ノウハウ・注意点:
  - Pythonの文字列リテラルで '\\text' を扱う際、\\t がタブ文字(0x09)に化ける罠がある。
    本スクリプトではバイナリモードで直接バイト列を置換することで回避している。
  - \\text{} 内の接続詞スペース付与は、re.sub の replacement に f-string を使うと
    \\t 化けが再発する。raw string を使うか、関数置換で回避する。
  - ページヘッダの除去は書籍ごとにパターンが異なるため、著者名はCLI引数で指定可能。
  - 画像を除いたmdを扱う場合、参照だけ残ると壊れたリンクになるので処理が必要。
"""

import argparse
import difflib
import glob
import os
import re
import sys
from pathlib import Path


# Built-in presets: book name → list of regex patterns for running headers
PRESETS: dict[str, list[str]] = {
    "dummit-foote": [
        r"^Sec\. \d+\.\d+[^\n]*$",   # "Sec. 10.1 Basic Definitions and Examples"
        r"^Chap\. \d+[^\n]*$",         # "Chap. 10 Introduction to Module Theory"
    ],
}


# ============================================================
# 修正関数群
# ============================================================

def fix_separators(text: str) -> str:
    """--- ページ区切り行を除去する。"""
    return re.sub(r"^---\s*$", "", text, flags=re.MULTILINE)


def fix_running_headers(text: str, patterns: list[str]) -> str:
    """指定した正規表現パターンに一致するrunning header/footer行を除去する。"""
    for pattern in patterns:
        text = re.sub(pattern, "", text, flags=re.MULTILINE)
    return text


def fix_html_entities(text: str) -> str:
    """HTMLエンティティをプレーン文字に復元する。

    OCRツール（特にMathpix等）がLaTeX数式中の < > & を
    &lt; &gt; &amp; にエスケープしてしまうケースへの対応。
    $d &gt; 4$ → $d > 4$ のように修正する。
    """
    text = text.replace('&gt;', '>')
    text = text.replace('&lt;', '<')
    text = text.replace('&amp;', '&')
    return text


def fix_spaced_text(text: str) -> str:
    r"""\\text{} 内でOCRが1文字ずつスペースを入れた問題を修復。

    OCRが \\text{for all} を \\text{f o r a l l} のように出力する。
    単一文字がスペース区切りで並ぶパターンを検出し、既知の英単語に再構成する。
    """
    def fix_spaced_text_block(match):
        content = match.group(1)
        # 単一文字のスペース区切りパターンか判定
        if re.match(r'^[a-z]( [a-z])+$', content.strip()):
            collapsed = content.strip().replace(' ', '')
            restored = _re_wordify(collapsed)
            return '\\text{' + restored + '}'
        return match.group(0)

    text = re.sub(r'\\text\s*\{([^}]+)\}', fix_spaced_text_block, text)
    return text


# 貪欲マッチ用の単語辞書（長い語句を先に試す）
_WORD_TABLE = [
    ('withrespectto', 'with respect to'),
    ('ifandonlyif', 'if and only if'),
    ('ifandonly', 'if and only'),
    ('suchthat', 'such that'),
    ('otherwise', 'otherwise'),
    ('forall', 'for all'),
    ('forevery', 'for every'),
    ('foreach', 'for each'),
    ('forsome', 'for some'),
    ('forany', 'for any'),
    ('either', 'either'),
    ('neither', 'neither'),
    ('where', 'where'),
    ('since', 'since'),
    ('hence', 'hence'),
    ('with', 'with'),
    ('resp', 'resp'),
    ('some', 'some'),
    ('over', 'over'),
    ('then', 'then'),
    ('and', 'and'),
    ('for', 'for'),
    ('all', 'all'),
    ('any', 'any'),
    ('not', 'not'),
    ('mod', 'mod'),
    ('iff', 'iff'),
    ('if', 'if'),
    ('in', 'in'),
    ('or', 'or'),
    ('on', 'on'),
    ('of', 'of'),
    ('as', 'as'),
    ('to', 'to'),
]


def _re_wordify(collapsed: str) -> str:
    """スペースなし文字列 'forall' を 'for all' のように単語に分解する。"""
    result = []
    i = 0
    while i < len(collapsed):
        matched = False
        for word, replacement in _WORD_TABLE:
            if collapsed[i:].startswith(word):
                if result:
                    result.append(' ')
                result.append(replacement)
                i += len(word)
                matched = True
                break
        if not matched:
            result.append(collapsed[i])
            i += 1
    return ''.join(result)


# 数式モード内で単独使用される接続詞（前後にスペースが必要）
_CONNECTOR_WORDS = [
    'for all', 'for some', 'for any', 'for every', 'for each',
    'such that', 'if and only if',
    'and', 'or', 'if', 'with', 'for', 'in', 'on', 'as', 'to',
    'where', 'resp', 'otherwise', 'mod',
]


def fix_text_spacing(text: str) -> str:
    r"""\\text{接続詞} に前後スペースを付与する。

    LaTeX数式モードでは \\text{for} の前後のスペースは無視される。
    \\text{ for } のように内部にスペースを含める必要がある。
    ただし \\text{for all} のような複数語はそのままでよい（内部にスペースあり）ので
    前後の空白だけ補う。

    【重要】re.sub の replacement で f'\\text{{ ... }}' を使うと
    \\t がタブ文字に化ける。関数置換で回避すること。
    """
    def add_spaces(match):
        content = match.group(1)
        stripped = content.strip()
        if stripped in _CONNECTOR_WORDS:
            return '\\text{ ' + stripped + ' }'
        return match.group(0)

    text = re.sub(r'\\text\{([^}]+)\}', add_spaces, text)
    return text


def fix_tab_corruption(filepath: str) -> bool:
    r"""バイナリレベルで TAB(0x09) + 'ext{' → '\\text{' を修復。

    Python文字列処理で '\\text' の \t がタブ文字に化けた場合の対策。
    テキストモードでは \t を含む文字列の扱いが難しいため、
    バイナリモードで直接バイト列を置換する。

    戻り値: 修正が行われたか
    """
    with open(filepath, 'rb') as f:
        content = f.read()

    original = content
    content = content.replace(b'\x09ext{', b'\\text{')
    content = content.replace(b'\x09ext {', b'\\text {')

    if content != original:
        with open(filepath, 'wb') as f:
            f.write(content)
        return True
    return False


def fix_image_refs(text: str, mode: str = 'comment') -> str:
    """画像参照を処理する。

    mode:
      'comment'     : <!-- Figure: alt_text --> に変換
      'delete'      : 行ごと完全削除
      'placeholder' : [Figure] テキストに置換
    """
    if mode == 'delete':
        text = re.sub(r'!\[[^\]]*\]\([^)]*\)\n?', '', text)
    elif mode == 'placeholder':
        text = re.sub(
            r'!\[[^\]]*\]\([^)]*\)',
            '[Figure]',
            text
        )
    else:  # comment
        text = re.sub(
            r'!\[([^\]]*)\]\([^)]*\)',
            lambda m: '<!-- Figure: ' + m.group(1) + ' -->',
            text
        )
    return text


def fix_page_headers(text: str, author: str = None) -> str:
    """ページヘッダ・フッタの残留を除去する。

    - 著者名の単独行（ページヘッダ）
    - ALL CAPSのセクションヘッダ行（例: '1.1. ALGEBRAIC PRELIMINARIES'）
    - 'CHAPTER N. TITLE' 形式のヘッダ行
    """
    # 著者名単独行の除去
    if author:
        # ファイル先頭のケース
        if text.startswith(author + '\n'):
            text = text[len(author) + 1:].lstrip('\n')
        # ファイル中のケース（前後に空行あり）
        text = re.sub(r'\n\n' + re.escape(author) + r'\n', '\n', text)

    # ALL CAPS セクションヘッダ（Fulton式：'1.1. ALGEBRAIC PRELIMINARIES'）
    text = re.sub(r'\n\d+\.\d+\.\s+[A-Z][A-Z\s]+\n', '\n', text)

    # CHAPTER ヘッダ（'CHAPTER 1. AFFINE ALGEBRAIC SETS'）
    text = re.sub(r'\nCHAPTER \d+\.\s+[A-Z][A-Z\s]+\n', '\n', text)

    return text


def fix_page_break_headers(text: str) -> str:
    """--- 直後に繰り返されるチャプタータイトル（裸テキスト）を除去。

    Gathmannの教材で見られるパターン:
      ---
      (空行)
      5. Tensor Products    ← ページヘッダとして繰り返されたタイトル
      (空行)
    '#' が付いていない裸のタイトルのみ除去する。

    注意: 番号付きリスト項目（'2. If $U\\subset X$...'）に誤マッチしないよう、
    タイトルは短く（60文字以内）、$を含まず、全体がタイトルらしい形式であること
    を条件とする。
    """
    lines = text.split('\n')
    result = []
    i = 0
    while i < len(lines):
        if (lines[i].strip() == '---'
                and i + 2 < len(lines)
                and lines[i + 1].strip() == ''
                and re.match(r'^\d+\.\s+[A-Z]', lines[i + 2].strip())
                and not lines[i + 2].strip().startswith('#')
                and len(lines[i + 2].strip()) <= 60
                and '$' not in lines[i + 2]):
            result.append(lines[i])    # --- は保持
            result.append(lines[i + 1])  # 空行は保持
            i += 3  # タイトル行をスキップ
            continue
        result.append(lines[i])
        i += 1
    return '\n'.join(result)


def fix_empty_headings(text: str) -> str:
    """中身のない見出し（## のみ）を除去する。"""
    lines = [l for l in text.split('\n') if l.strip() != '##']
    return '\n'.join(lines)


def fix_standalone_page_numbers(text: str) -> str:
    """孤立したページ番号を除去する。

    アラビア数字（1〜9999）とローマ数字（i, ii, ..., xiii 程度）の
    単独行を除去。前後が空行であることを条件とする。
    """
    text = re.sub(r'\n\n\d{1,4}\n\n', '\n\n', text)
    text = re.sub(
        r'\n\n(?:x{0,3}(?:ix|iv|v?i{0,3}))\n\n',
        '\n\n', text, flags=re.IGNORECASE
    )
    return text


def fix_dollar_artifacts(text: str) -> str:
    """空の数式ブロック $$ $$ を除去する。"""
    text = re.sub(r'\$\$\s+\$\$', '', text)
    return text


def fix_standalone_dots(text: str) -> str:
    """白紙ページ跡の孤立ドットを除去する。"""
    text = re.sub(r'\n\n\.\n\n', '\n\n', text)
    return text


def fix_excessive_blanks(text: str) -> str:
    """4行以上の連続空行を2行（1空行）に圧縮する。"""
    text = re.sub(r'\n{4,}', '\n\n\n', text)
    return text


# ============================================================
# 全修正の名前→関数マッピング
# ============================================================

ALL_FIXES = [
    'html_entities',
    'tab_corruption',
    'spaced_text',
    'text_spacing',
    'separators',
    'running_headers',
    'image_refs',
    'page_headers',
    'page_break_headers',
    'empty_headings',
    'page_numbers',
    'dollar_artifacts',
    'standalone_dots',
    'excessive_blanks',
]


# ============================================================
# ファイル処理
# ============================================================

def process_file(filepath: str, args: argparse.Namespace) -> tuple[bool, str]:
    """1ファイルに全修正を適用する。

    戻り値: (修正が行われたか, 差分テキスト)
    """
    active_fixes = set(args.only.split(',')) if args.only else set(ALL_FIXES)

    # tab_corruption はバイナリレベルで先に処理
    tab_fixed = False
    if 'tab_corruption' in active_fixes:
        tab_fixed = fix_tab_corruption(filepath)

    with open(filepath, 'r', encoding='utf-8') as f:
        original = f.read()

    text = original

    if 'html_entities' in active_fixes:
        text = fix_html_entities(text)

    if 'spaced_text' in active_fixes:
        text = fix_spaced_text(text)

    if 'text_spacing' in active_fixes:
        text = fix_text_spacing(text)

    if 'separators' in active_fixes and getattr(args, 'remove_separators', False):
        text = fix_separators(text)

    if 'running_headers' in active_fixes:
        patterns = getattr(args, '_header_patterns', [])
        if patterns:
            text = fix_running_headers(text, patterns)

    if 'image_refs' in active_fixes:
        text = fix_image_refs(text, mode=args.image_mode)

    if 'page_headers' in active_fixes:
        text = fix_page_headers(text, author=args.page_header_author)

    if 'page_break_headers' in active_fixes:
        text = fix_page_break_headers(text)

    if 'empty_headings' in active_fixes:
        text = fix_empty_headings(text)

    if 'page_numbers' in active_fixes:
        text = fix_standalone_page_numbers(text)

    if 'dollar_artifacts' in active_fixes:
        text = fix_dollar_artifacts(text)

    if 'standalone_dots' in active_fixes:
        text = fix_standalone_dots(text)

    if 'excessive_blanks' in active_fixes:
        text = fix_excessive_blanks(text)

    changed = (text != original) or tab_fixed
    diff_text = ''

    if changed and args.verbose:
        diff_text = '\n'.join(difflib.unified_diff(
            original.splitlines(), text.splitlines(),
            fromfile=f'a/{os.path.basename(filepath)}',
            tofile=f'b/{os.path.basename(filepath)}',
            lineterm='',
            n=1,
        ))

    if changed and not args.dry_run:
        output_path = getattr(args, 'output', None)
        if output_path:
            Path(output_path).parent.mkdir(parents=True, exist_ok=True)
            Path(output_path).write_text(text, encoding='utf-8')
        else:
            # Single-file mode: create a backup
            if getattr(args, '_single_file_mode', False):
                backup = Path(filepath).with_suffix('.md.bak')
                backup.write_text(original, encoding='utf-8')
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(text)

    return changed, diff_text


# ============================================================
# 検証
# ============================================================

def verify_files(filepaths: list[str]) -> dict[str, int]:
    """修正後のファイル群に残存する問題をカウントする。"""
    counts = {
        'html_entities': 0,
        'tab_corruption': 0,
        'spaced_text': 0,
        'image_refs': 0,
        'empty_headings': 0,
        'dollar_artifacts': 0,
    }

    for filepath in filepaths:
        with open(filepath, 'rb') as f:
            raw = f.read()
        with open(filepath, 'r', encoding='utf-8') as f:
            text = f.read()

        counts['html_entities'] += len(re.findall(r'&gt;|&lt;|&amp;', text))
        counts['tab_corruption'] += raw.count(b'\x09ext{') + raw.count(b'\x09ext {')
        counts['spaced_text'] += len(re.findall(
            r'\\text\s*\{[a-z]( [a-z]){2,}\}', text
        ))
        counts['image_refs'] += len(re.findall(r'!\[img-', text))
        counts['empty_headings'] += len(re.findall(r'(?m)^##\s*$', text))
        counts['dollar_artifacts'] += len(re.findall(r'\$\$\s+\$\$', text))

    return counts


# ============================================================
# CLI
# ============================================================

def main():
    parser = argparse.ArgumentParser(
        description='OCR済み数学系Markdownの一括クリーンアップ',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=__doc__
    )
    parser.add_argument(
        'inputs',
        nargs='+',
        help='処理対象のMarkdownファイルまたはディレクトリ',
    )
    parser.add_argument(
        '--dry-run',
        action='store_true',
        help='変更を書き込まず、修正対象ファイルの一覧だけ表示',
    )
    parser.add_argument(
        '--verbose', '-v',
        action='store_true',
        help='各ファイルの差分を表示',
    )
    parser.add_argument(
        '--only',
        default=None,
        help=f'適用する修正をカンマ区切りで指定。選択肢: {",".join(ALL_FIXES)}',
    )
    parser.add_argument(
        '--image-mode',
        choices=['comment', 'delete', 'placeholder'],
        default='comment',
        help='画像参照の処理方法（デフォルト: comment）',
    )
    parser.add_argument(
        '--page-header-author',
        default=None,
        help='ページヘッダとして除去する著者名（例: "Andreas Gathmann"）',
    )
    parser.add_argument(
        '--preset',
        choices=list(PRESETS.keys()),
        help='running headers 除去の書籍プリセットを指定',
    )
    parser.add_argument(
        '--header-pattern',
        dest='header_patterns',
        action='append',
        default=[],
        metavar='REGEX',
        help='running headers として除去する正規表現パターン（複数指定可）',
    )
    parser.add_argument(
        '--no-remove-separators',
        dest='remove_separators',
        action='store_false',
        default=False,
        help='--- ページ区切りを除去する（separators 修正が有効な場合のみ適用）',
    )
    parser.add_argument(
        '--remove-separators',
        dest='remove_separators',
        action='store_true',
        help='--- ページ区切りを除去する（separators 修正を有効化）',
    )
    parser.add_argument(
        '--verify',
        action='store_true',
        help='修正後に残存問題をカウントして報告',
    )
    parser.add_argument(
        '-o', '--output',
        default=None,
        help='出力先ファイルを指定（単一ファイル入力時のみ有効）',
    )

    args = parser.parse_args()

    # Resolve header patterns from preset + explicit patterns
    header_patterns = list(args.header_patterns)
    if args.preset:
        header_patterns = PRESETS[args.preset] + header_patterns
    args._header_patterns = header_patterns

    # Collect files from inputs (files or directories)
    files = []
    for inp in args.inputs:
        if os.path.isdir(inp):
            files.extend(sorted(glob.glob(os.path.join(inp, '*.md'))))
        elif os.path.exists(inp):
            files.append(inp)
        else:
            print(f'Not found: {inp}', file=sys.stderr)

    if not files:
        print('No .md files found.', file=sys.stderr)
        sys.exit(1)

    if args.output and len(files) > 1:
        print('Error: --output は単一ファイル入力時のみ有効です', file=sys.stderr)
        sys.exit(1)

    # Mark single-file mode for backup behavior
    args._single_file_mode = (len(files) == 1 and not os.path.isdir(args.inputs[0]))

    mode_label = '[dry-run] ' if args.dry_run else ''
    print(f'{mode_label}Processing {len(files)} file(s) ...')
    if args.only:
        print(f'  Active fixes: {args.only}')
    if header_patterns:
        print(f'  Running header patterns: {len(header_patterns)} pattern(s)')

    modified = 0
    for filepath in files:
        fname = os.path.basename(filepath)
        changed, diff_text = process_file(filepath, args)
        if changed:
            modified += 1
            label = '[would modify]' if args.dry_run else 'Modified'
            suffix = ''
            if args.output:
                suffix = f'  → {args.output}'
            elif args._single_file_mode and not args.dry_run:
                suffix = f'  (backup: {Path(filepath).with_suffix(".md.bak").name})'
            print(f'  {label:>15}: {fname}{suffix}')
            if diff_text:
                print(diff_text)
        elif args.verbose:
            print(f'  {"No changes":>15}: {fname}')

    print(f'\n{mode_label}Done. {"Would modify" if args.dry_run else "Modified"}'
          f' {modified}/{len(files)} files.')

    # 検証
    if args.verify and not args.dry_run:
        print('\n=== Verification ===')
        counts = verify_files(files)
        all_clear = True
        for check, count in counts.items():
            status = '✓' if count == 0 else '✗'
            if count > 0:
                all_clear = False
            print(f'  {status} {check}: {count} remaining')
        if all_clear:
            print('  All checks passed!')
        else:
            print('  Some issues remain. Re-run or check manually.')


if __name__ == '__main__':
    main()
