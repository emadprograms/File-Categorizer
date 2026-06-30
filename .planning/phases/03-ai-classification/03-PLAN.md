# Phase 03: ai-classification - Plan

**Date:** 2026-06-30
**Phase:** 03
**Status:** Executable

<objective>
Integrate the Gemma 4 26B Vision endpoint using the `google-genai` SDK to categorize extracted PDF pages. Enforce a strict 7-second rate limit, robust error backoff, and JSON schema validation.
</objective>

<dependencies>
- `01-cli-scaffolding`
- `02-image-processing`
</dependencies>

<tasks>
## 1. Implement API Integration & Rate Limiter
- **Type:** backend
- **Files:** `src/ai_classification.py`
- **Action:** Create `src/ai_classification.py`. Implement `classify_pages(tmp_dir, categories)` that iterates over pages in `progress.json`. Implement the strict 7-second rate limiter using `time.time()` and `time.sleep()`. Call the `google-genai` SDK to hit `gemma-4-26b`, passing the image and dynamic prompt. Enforce JSON schema output. Handle 429 (sleep 65s), 500/503 (sleep 15s), and 401 (sys.exit).
- **Verify:** `<automated>` Run `pytest tests/test_ai_classification.py`

## 2. Implement Fallback Strategy & Cache Updating
- **Type:** backend
- **Files:** `src/ai_classification.py`
- **Action:** In `classify_pages`, parse the JSON response. Validate the category against the allowed `categories` list. If valid, update `progress.json` with the category. If invalid/hallucinated, mark as error and retry up to 3 times before moving on.
- **Verify:** `<automated>` Run `pytest tests/test_ai_classification.py`

## 3. Integrate with CLI
- **Type:** backend
- **Files:** `src/cli.py`
- **Action:** Import `classify_pages`. In `cli.py`, after `process_pdf` returns, call `classify_pages(tmp_dir, categories)`. Wait until phase 4 to delete `tmp_dir`. Update `failed_pages` tracking to include pages that failed classification.
- **Verify:** `<automated>` Run `pytest tests/test_ai_classification.py`
</tasks>

<verification>
- Run full test suite: `pytest`
- Verify rate limiter logic functions without failing early.
- Verify fallback logic marks invalid categories as errors in `progress.json`.
</verification>

<success_criteria>
- Cleaned images are sent to the Gemma 4 26B vision endpoint.
- Prompt properly instructs the model to select exactly one of the user-provided categories.
- System reliably parses the classification response for each page.
- 7-second rate limit is strictly enforced.
- Specific HTTP errors are handled via backoff rules.
</success_criteria>
