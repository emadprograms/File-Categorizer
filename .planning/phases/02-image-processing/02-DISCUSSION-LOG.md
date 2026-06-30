# Phase 02: image-processing - Discussion Log

> **Audit trail only.** Do not use as input to planning, research, or execution agents.
> Decisions are captured in CONTEXT.md — this log preserves the alternatives considered.

**Date:** 2026-06-30
**Phase:** 02-image-processing
**Areas discussed:** PDF to Image Library, Extraction DPI, Caching & Error Handling, Image Processing Stack

---

## PDF to Image Library

| Option | Description | Selected |
|--------|-------------|----------|
| PyMuPDF (fitz) | (Recommended) PyMuPDF (fitz) — Self-contained, very fast, doesn't require poppler binaries | ✓ |
| pdf2image + poppler | Standard but requires external system dependencies | |
| You decide | Let the agent decide | |

**User's choice:** PyMuPDF (fitz)
**Notes:** Decided to avoid external binary dependencies (poppler) and prioritize speed.

---

## Extraction DPI

| Option | Description | Selected |
|--------|-------------|----------|
| 300 DPI | (Recommended) 300 DPI — Standard for OCR/Vision models to preserve fine details | ✓ |
| 150 DPI | Faster but might lose fine typography and diacritics | |
| Native resolution | Native resolution of the PDF | |
| You decide | Let the agent decide | |

**User's choice:** 300 DPI
**Notes:** If the PDF DPI is less than 300, upscale it to 300 DPI (e.g. using `matrix=fitz.Matrix(300/72, 300/72)`) to ensure consistent image sizes for subsequent processing.

---

## Caching & Error Handling

| Option | Description | Selected |
|--------|-------------|----------|
| Fail fast | Fail fast and abort the entire PDF | |
| Skip & Log | (Recommended) Log the error, skip the bad page, and continue processing the rest of the PDF | ✓ |
| You decide | Let the agent decide | |

**User's choice:** Custom Workflow
**Notes:** The user requested a granular caching method. Decided on: individual JSON output per file, a temporary workspace (`.tmp_[filename]/`), a `progress.json` for page-level state tracking, and retrying failed pages at the end of the file. If pages fail permanently, append their numbers to the final filename (e.g. `[filename]_categorized_failed_pages_3_4.pdf`).

---

## Image Processing Stack

| Option | Description | Selected |
|--------|-------------|----------|
| OpenCV | (Recommended) OpenCV — Provides built-in morphological filters like black-hat needed for the cleaning logic | ✓ |
| Pillow | Simpler API, but requires manual implementation of morphological filters | |
| You decide | Let the agent decide | |

**User's choice:** OpenCV
**Notes:** Selected for built-in morphological operations.

---

## the agent's Discretion

None.

## Deferred Ideas

None.
