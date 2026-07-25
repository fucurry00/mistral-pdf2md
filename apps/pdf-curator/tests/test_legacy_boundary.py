import ast
from pathlib import Path

SRC = Path(__file__).parents[1] / "src"
FORBIDDEN_PATHS = ("mistral-ocr-process", "proofread-ocr")
FORBIDDEN_MODULES = {"cleanup_ocr", "convert_pdf_to_markdown", "pipeline"}


def test_new_app_has_no_legacy_import_or_execution_boundary():
    for path in SRC.rglob("*.py"):
        source = path.read_text()
        assert not any(forbidden in source for forbidden in FORBIDDEN_PATHS), path
        tree = ast.parse(source)
        for node in ast.walk(tree):
            if isinstance(node, ast.Import):
                assert not any(alias.name in FORBIDDEN_MODULES for alias in node.names), path
            elif isinstance(node, ast.ImportFrom) and node.module:
                assert node.module not in FORBIDDEN_MODULES, path
        assert "subprocess" not in source, path
