# OCR Cleanup Tool Specification (2-Pass Architecture)

## Overview
This tool automates the process of cleaning up and formatting Markdown files generated from OCR (Optical Character Recognition). It is specifically designed for university lecture slides (Real Analysis) which contain repetitive headers, footers, and mathematical expressions.

The tool leverages the `gemini` CLI in a **2-pass architecture** to ensure global consistency across the document.

## Requirements
- **Python 3.x**: To run the automation script.
- **Gemini CLI**: The `gemini` command-line tool must be installed and authenticated in your environment.

## Directory Structure
```text
ocr_cleanup/
├── prompt_pass1.md      # AI instructions for extracting global context
├── prompt_pass2.md      # AI instructions for formatting individual chunks
├── process_markdown.py  # Python script orchestrating the 2-pass workflow
└── SPEC.md              # This specification document
```

## Architecture

### Pass 1: Global Context Extraction
- **Goal**: Understand the document as a whole before modifying any specific part.
- **Process**: The script feeds the *entire* raw OCR document to the AI using `prompt_pass1.md`.
- **Output**: The AI generates a `global_context` (a glossary, structural guide, and list of common OCR errors/notations).

### Pass 2: Chunk Processing
- **Goal**: Format the text accurately while adhering to context window limits.
- **Process**: The script splits the document into smaller chunks (e.g., 5 pages). For each chunk, it sends a combined input containing both the `global_context` (from Pass 1) and the specific chunk text to the AI using `prompt_pass2.md`.
- **Output**: Cleaned, properly formatted textbook-style Markdown blocks, which are then concatenated into the final file.

## Components

### 1. `prompt_pass1.md`
Instructs the AI to act as an analyzer, extracting overall structure, formatting rules, glossary, and recurring OCR artifacts.

### 2. `prompt_pass2.md`
Instructs the AI to act as an editor. It takes the context from Pass 1 to accurately reconstruct mathematical meaning, remove noise (slide headers/footers), fix LaTeX spacings, and apply proper Markdown headers.

### 3. `process_markdown.py`
The orchestrator script handling file reading, chunking (via Regex on headers), executing `gemini` CLI subprocesses, and merging the outputs.

## Usage

### Basic Command
Run the script by providing the input file and the desired output path:

```bash
python ocr_cleanup/process_markdown.py <input_file> -o <output_file>
```

### Options
- `-o`, `--output`: (Required) Path to save the cleaned Markdown.
- `-p1`, `--prompt1`: Path to the Pass 1 prompt file (Defaults to `ocr_cleanup/prompt_pass1.md`).
- `-p2`, `--prompt2`: Path to the Pass 2 prompt file (Defaults to `ocr_cleanup/prompt_pass2.md`).
- `-c`, `--chunk-size`: Number of pages per chunk (Defaults to `5`).

### Example
```bash
python ocr_cleanup/process_markdown.py Ch2-Real_Analysis_Folland/main.md -o Ch2-Real_Analysis_Folland/cleaned_main.md -c 5
```