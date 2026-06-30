# Phase 03 — Pattern Mapping

**Phase:** 03 - ai-classification
**Date:** 2026-06-30

## 1. Files to Create/Modify
- `src/cli.py` (Modify): Update to invoke `classify_pages(tmp_dir, categories)` and delete `tmp_dir` after processing.
- `src/ai_classification.py` (Create): Implement API integration, rate limiting, and backoff loop.

## 2. Existing Analogs & Code Excerpts

### Analog for `src/ai_classification.py` iteration
The current `process_pdf` in `src/image_processing.py` tracks per-page success in `progress.json`.
```python
# From src/image_processing.py
def process_pdf(pdf_path: str, output_dir: str) -> tuple[dict, str]:
    # ...
    progress_file = os.path.join(tmp_dir, "progress.json")
    status = {}
    if os.path.exists(progress_file):
        try:
            with open(progress_file, "r", encoding="utf-8") as f:
                status = json.load(f)
        except json.JSONDecodeError:
            pass

    def save_progress():
        with open(progress_file, "w", encoding="utf-8") as f:
            json.dump(status, f)
```
**Pattern Rule:** `src/ai_classification.py` must load this same `progress.json`, skip pages that are `classification_success`, and use `save_progress()` to persist updates.

### Analog for `src/cli.py` Error Handling
```python
# From src/cli.py
        try:
            status, tmp_dir = process_pdf(pdf_path, args.output_dir)
            # ...
        except Exception as e:
            print(f"Error processing {pdf_path}: {e}", file=sys.stderr)
            continue
```
**Pattern Rule:** Ensure `classify_pages` exceptions are caught at the CLI level to prevent crashing the entire batch when a single PDF fails completely.

## 3. Structural Constraints
- We must respect the 7-second rate limiter globally inside the classification loop.
- The `google-genai` SDK is the specified integration library.
- JSON schema output must be validated against the `categories` list from `src/utils.py`.
