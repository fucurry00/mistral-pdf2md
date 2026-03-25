import argparse
import os
import re
import subprocess
import sys

def split_into_chunks(text, pages_per_chunk=5):
    """
    Splits the OCR'd markdown text into logical chunks.
    We assume each slide/page is separated by the repeating header:
    'Bara Kim 2026, Spring, Korea University\nReal Analysis'
    """
    # Use the recurring header as a delimiter to split the text into individual pages
    header_pattern = r"Bara Kim 2026, Spring, Korea University\s+Real Analysis\s*"

    pages = re.split(header_pattern, text)

    # Clean up empty pages that might result from splitting at the very beginning
    pages = [p.strip() for p in pages if p.strip()]

    chunks = []
    current_chunk = []
    current_count = 0

    for page in pages:
        current_chunk.append(page)
        current_count += 1

        # When we reach the desired number of pages per chunk, save the chunk
        if current_count >= pages_per_chunk:
            chunks.append("\n\n---\n\n".join(current_chunk))
            current_chunk = []
            current_count = 0

    # Append any remaining pages as the final chunk
    if current_chunk:
        chunks.append("\n\n---\n\n".join(current_chunk))

    return chunks

def run_gemini(input_text, prompt_path):
    """
    Runs the gemini CLI command with the specified prompt and input text.
    """
    try:
        with open(prompt_path, "r", encoding="utf-8") as f:
            prompt = f.read()
        cmd = ["gemini", "--model", "gemini-3-flash-preview", "-p", prompt]
        result = subprocess.run(
            cmd,
            input=input_text,
            capture_output=True,
            text=True,
            encoding='utf-8',
            check=True
        )
        return result.stdout.strip()
    except subprocess.CalledProcessError as e:
        print(f"\nError processing via gemini CLI: {e.stderr}", file=sys.stderr)
        sys.exit(1)
    except FileNotFoundError:
        print("\nError: 'gemini' CLI command not found. Please ensure it is installed and in your PATH.", file=sys.stderr)
        sys.exit(1)

def main():
    parser = argparse.ArgumentParser(description="Clean up OCR'd Markdown using Gemini CLI (2-Pass Approach)")
    parser.add_argument("input_file", help="Path to the input Markdown file")
    parser.add_argument("-o", "--output", help="Path to the output Markdown file", required=True)
    parser.add_argument("-p1", "--prompt1", help="Path to the Pass 1 prompt file", default="ocr_cleanup/prompt_pass1.md")
    parser.add_argument("-p2", "--prompt2", help="Path to the Pass 2 prompt file", default="ocr_cleanup/prompt_pass2.md")
    parser.add_argument("-c", "--chunk-size", type=int, default=5, help="Number of pages per chunk (default: 5)")

    args = parser.parse_args()

    if not os.path.exists(args.input_file):
        print(f"Input file not found: {args.input_file}")
        sys.exit(1)

    if not os.path.exists(args.prompt1):
        print(f"Pass 1 Prompt file not found: {args.prompt1}")
        sys.exit(1)

    if not os.path.exists(args.prompt2):
        print(f"Pass 2 Prompt file not found: {args.prompt2}")
        sys.exit(1)

    print(f"Reading input file: {args.input_file}...")
    with open(args.input_file, 'r', encoding='utf-8') as f:
        text = f.read()

    # Pass 1: Extract Global Context
    print("\n--- Pass 1: Analyzing entire document for global context ---")
    global_context = run_gemini(text, args.prompt1)
    print("Global context extracted successfully.\n")

    # Pass 2: Process Chunks
    print(f"--- Pass 2: Splitting and processing chunks (pages per chunk: {args.chunk_size}) ---")
    chunks = split_into_chunks(text, pages_per_chunk=args.chunk_size)
    print(f"Total chunks created: {len(chunks)}\n")

    processed_chunks = []
    for i, chunk in enumerate(chunks, 1):
        print(f"Processing chunk {i}/{len(chunks)}...")

        # Combine the global context and the specific chunk into the format expected by prompt_pass2.md
        combined_input = f"<global_context>\n{global_context}\n</global_context>\n\n<target_chunk>\n{chunk}\n</target_chunk>"

        cleaned_text = run_gemini(combined_input, args.prompt2)
        processed_chunks.append(cleaned_text)
        print(f"  -> Chunk {i} completed.\n")

    print(f"Combining chunks and writing to {args.output}...")
    with open(args.output, 'w', encoding='utf-8') as f:
        f.write("\n\n".join(processed_chunks))

    print(f"Done! Cleaned file saved to: {args.output}")

if __name__ == "__main__":
    main()
