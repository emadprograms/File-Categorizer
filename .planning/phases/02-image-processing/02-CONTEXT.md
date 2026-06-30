# Phase 02: image-processing - Context

**Gathered:** 2026-06-30
**Status:** Ready for planning

<domain>
## Phase Boundary

Extract pages from the PDF into images and apply the image cleaning logic (division normalization, washout, black-hat filter) so they are ready for the Vision LLM in the next phase.

</domain>

<decisions>
## Implementation Decisions

### PDF to Image Library
- **D-01:** Use PyMuPDF (fitz) for PDF extraction (avoids external binaries).
- **D-02:** Extract images at 300 DPI by default. If the PDF native DPI is lower, apply a zoom matrix (`matrix=fitz.Matrix(300/72, 300/72)`) to upscale to 300 DPI for consistent sizing during morphological cleaning.

### Image Processing Stack
- **D-03:** Use OpenCV for image processing, providing access to necessary built-in morphological filters like black-hat.

### Workflow, Caching & Error Handling
- **D-04:** Check for final JSON output (`[filename]_report.json`). If it exists and is complete, skip the entire PDF.
- **D-05:** Use an isolated per-file temporary directory (`.tmp_[filename]/`) to store extracted and cleaned images, and a `progress.json` to cache page-level status. This avoids re-processing upon failure and prevents memory overload.
- **D-06:** If an individual page fails extraction or processing, log the error, skip the page, and continue processing the rest of the document.
- **D-07:** At the end of the PDF, loop back and retry any pages marked as failed in that specific file.
- **D-08:** Smart naming: If pages are permanently failed after retries, explicitly append them to the final PDF output filename (e.g., `[filename]_categorized_failed_pages_4_9.pdf`) so the user immediately knows which files have missing data. Delete the temp workspace after final output is generated.

</decisions>

<canonical_refs>
## Canonical References

**Downstream agents MUST read these before planning or implementing.**

### Project Scope
- `.planning/PROJECT.md` — Core value and context regarding morphological processing (white point 200-220, black-hat).
- `.planning/REQUIREMENTS.md` — Requirement IMG-01.

### Prior Phases
- `.planning/phases/01-cli-scaffolding/01-CONTEXT.md` — Context about batch output structure (separate JSON per PDF).

</canonical_refs>

<code_context>
## Existing Code Insights

### Reusable Assets
- None currently (Greenfield CLI processing module).

### Established Patterns
- Phase 01 established a try-except wrapper pattern in the CLI (`cli.py`) for graceful handling of dynamic input errors. Use similar patterns for handling extraction/processing errors.

### Integration Points
- This phase will be invoked by the CLI (from Phase 1) and will pass processed images/temp directory context to the AI phase (Phase 3).

</code_context>

<specifics>
## Specific Ideas

- The temporary workspace should be per-file (e.g. `.tmp_[filename]/`) to ensure multi-threading or parallel batch processing is possible down the line.

</specifics>

<deferred>
## Deferred Ideas

None — discussion stayed within phase scope.

</deferred>

---

*Phase: 02-image-processing*
*Context gathered: 2026-06-30*
