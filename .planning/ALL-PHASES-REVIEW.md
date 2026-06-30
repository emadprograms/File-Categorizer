---
status: issues_found
files_reviewed: 10
critical: 1
warning: 2
info: 1
total: 4
---

# Code Review Report (All Phases)

This report encompasses source files from all executed phases (01 to 04.1).

## Findings

### CR-01: Google Cloud Storage Image Leak on API Errors
- **File:** `src/ai_classification.py`
- **Location:** `classify_pages` loop (line 71-126)
- **Severity:** Critical
- **Description:** 
  The application uploads images to the Google GenAI API using `image = client.files.upload(...)` inside a `try` block. If `client.models.generate_content` throws an exception (such as `APIError` 429 or 503), the execution jumps directly to the `except APIError` block. The cleanup code (`client.files.delete(name=image.name)`) is skipped, causing the image to leak and permanently remain in the user's Google Cloud storage.
- **Recommendation:** 
  Use a `try...finally` block for the uploaded image to ensure `client.files.delete` is executed regardless of whether `generate_content` succeeds or fails.

### WR-01: Local Temporary Directory Leak on Exceptions
- **File:** `src/cli.py`
- **Location:** `main` (line 130)
- **Severity:** Warning
- **Description:** 
  The cleanup of the temporary directory (`shutil.rmtree(tmp_dir)`) is located at the very end of the `try` block inside the main PDF processing loop. If an unhandled exception occurs during `classify_pages`, `generate_report`, or `inject_pdf_metadata`, the exception will be caught by the outer `except Exception as e:` block, skipping the `shutil.rmtree(tmp_dir)` call. This will leave intermediate images in the `.tmp_<pdfname>` directory on disk.
- **Recommendation:** 
  Move the `shutil.rmtree(tmp_dir, ignore_errors=True)` call into a `finally` block for that specific processing iteration, or handle it via a context manager.

### WR-02: Inline Imports Not Complying With PEP 8
- **File:** `src/cli.py`
- **Location:** Line 106
- **Severity:** Warning
- **Description:** 
  `from src.metadata import generate_report, inject_pdf_metadata` is imported inline within the `main()` function. While this works, it violates standard PEP 8 guidelines unless there is a specific need to avoid circular dependencies (which does not seem to be the case here).
- **Recommendation:** 
  Move the import to the top of the file alongside the other `src.*` imports.

### IN-01: Naive Division-by-Zero Handling in Image Processing
- **File:** `src/image_processing.py`
- **Location:** Line 127 (`bg_float[bg_float == 0] = 1e-6`)
- **Severity:** Info
- **Description:** 
  To prevent division by zero, the script replaces `0` with `1e-6` before dividing. While functionally correct and mathematically identical to handling NaNs, it's slightly unidiomatic for NumPy.
- **Recommendation:** 
  Consider using `np.divide` with the `out` and `where` parameters, or `np.errstate(divide='ignore', invalid='ignore')` for a more idiomatic approach to array division.
