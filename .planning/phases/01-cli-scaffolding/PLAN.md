---
wave: 1
depends_on: []
files_modified:
  - "src/cli.py"
  - "src/utils.py"
  - "tests/test_cli.py"
autonomous: false
requirements: ["CLI-01", "CLI-02"]
---

# Phase 1: CLI Scaffolding Plan

## Threat Model (ASVS Level 1)
- **Path Traversal / Local File Inclusion (CWE-22):** The CLI accepts file paths for inputs (`--input-pdfs`, `--categories-file`) and outputs (`--output-dir`). We must ensure the input paths are resolved properly and verified to exist before processing. The output directory must be created securely without overwriting critical system paths.
- **Denial of Service (CWE-400):** Processing maliciously large category files could consume excessive memory. While acceptable for a local CLI initially, basic sanity checks on file existence and accessibility are required.

## Artifacts this phase produces
- `src/cli.py` (file)
- `src/utils.py` (file)
- `tests/test_cli.py` (file)
- `src/cli.py:parse_args()` (function)
- `src/cli.py:main()` (function)
- `src/utils.py:load_categories()` (function)
- `--input-pdfs` (CLI argument)
- `--categories-file` (CLI argument)
- `--output-dir` (CLI argument)

## Wave 1

### Task 1.1: Create basic CLI entrypoint and argument parser
```xml
<task>
  <action>
    Create `src/cli.py` using Python's standard library `argparse`. Define three arguments:
    1. `--input-pdfs` (shorthand `-i`): Required, accepts multiple string arguments (nargs='+').
    2. `--categories-file` (shorthand `-c`): Required, accepts a single string path.
    3. `--output-dir` (shorthand `-o`): Required, accepts a single string path.
    Define `parse_args(args=None)` function that returns the parsed namespace.
    Define `main()` function that calls `parse_args()` and prints the parsed variables as placeholder logic.
  </action>
  <read_first>
    - src/cli.py
  </read_first>
  <acceptance_criteria>
    - Running `python src/cli.py --help` exits 0 and prints usage including `--input-pdfs`, `--categories-file`, and `--output-dir`.
    - Running `python src/cli.py -i test1.pdf test2.pdf -c cats.txt -o out` prints the parsed arguments to standard output.
  </acceptance_criteria>
</task>
```

### Task 1.2: Implement category file loading logic
```xml
<task>
  <action>
    Create `src/utils.py` and define `load_categories(filepath: str) -> list[str]`. 
    Implement logic to verify that `filepath` exists on disk. If the file ends with `.json`, parse it as a JSON list of strings using the `json` module. Otherwise, read it as a text file where each non-empty line represents a category. 
    Strip leading/trailing whitespace from the read categories.
  </action>
  <read_first>
    - src/utils.py
  </read_first>
  <acceptance_criteria>
    - `src/utils.py` contains `def load_categories(`.
    - `load_categories` correctly parses a `.txt` file with lines "Invoice\nReceipt " into `['Invoice', 'Receipt']`.
    - `load_categories` correctly parses a `.json` file containing `["Invoice", "Receipt"]` into `['Invoice', 'Receipt']`.
    - Calling `load_categories` on a non-existent file raises `FileNotFoundError`.
  </acceptance_criteria>
</task>
```

### Task 1.3: Wire category loading and path validation into main CLI
```xml
<task>
  <action>
    Modify `src/cli.py:main()` to import and call `load_categories()` from `src/utils.py` using the parsed `--categories-file` path. 
    Add path validation: iterate over the parsed `--input-pdfs` list and verify each path exists using `os.path.isfile` (or `pathlib.Path.is_file`). If any file is missing, print an error message to stderr and exit with status 1.
    Verify that `--output-dir` exists; if not, create it using `os.makedirs(exist_ok=True)`.
  </action>
  <read_first>
    - src/cli.py
    - src/utils.py
  </read_first>
  <acceptance_criteria>
    - Running `python src/cli.py -i nonexistent.pdf -c categories.txt -o out` prints an error to stderr and exits 1.
    - Providing valid existing files loads the categories and creates the output directory without error.
  </acceptance_criteria>
</task>
```

### Task 1.4: Add tests for the CLI and utilities
```xml
<task>
  <action>
    Create `tests/test_cli.py` using Python's standard `unittest` framework.
    Write test methods testing `src.utils.load_categories` for both TXT and JSON parsing using a temporary directory (e.g., via `tempfile`).
    Write test methods for `src.cli.parse_args` ensuring it parses `-i`, `-c`, and `-o` correctly into the expected attributes.
  </action>
  <read_first>
    - tests/test_cli.py
    - src/cli.py
    - src/utils.py
  </read_first>
  <acceptance_criteria>
    - `tests/test_cli.py` contains standard `unittest.TestCase` classes.
    - Running `python -m unittest discover tests` exits 0 with all written tests passing.
  </acceptance_criteria>
</task>
```

## Verification

### must_haves
```yaml
must_haves:
  truths:
    - "Running `python src/cli.py --help` outputs standard argparse help containing --input-pdfs, --categories-file, and --output-dir"
    - "Running `python -m unittest discover tests` exits 0"
  prohibitions:
    - statement: The CLI must not accept hardcoded categories directly as CLI arguments (must use --categories-file)
      status: resolved
      verification: "Running `python src/cli.py --help` does not show any inline categories argument"
```
