# Phase 04: reporting-metadata - Context

**Gathered:** 2026-06-30
**Status:** Ready for planning

<domain>
## Phase Boundary

Updating PDF page metadata with the classification result and generating structured reports (JSON only). This covers injecting the LLM's categorized outputs (and reasons) into the PDF structure and rendering the final output file(s).

</domain>

<decisions>
## Implementation Decisions

### Page Metadata Method
- **D-01:** Attach category to individual pages using PDF Page Labels (built into PyMuPDF).
- **D-02:** Format the Page Label as `{page_num} - {category}` to preserve original numbering for reference.

### Report Content & Structure
- **D-03:** The JSON report will use detailed telemetry (including processing time, retries, failure reasons).
- **D-04:** Include the AI's `reason` for the category alongside the category itself.
- **D-05:** Organize the JSON keyed by page number (1-indexed): `{"1": {"category": "...", "reason": "...", "telemetry": {...}}}`.

### Export Formats
- **D-06:** Output JSON only. Do not generate a CSV report.

### Failed Pages
- **D-07:** For permanently failed pages, set the JSON `category` value explicitly to `"Failed"`, with the `reason` containing the error message.
- **D-08:** The final output PDF filename will append the failed page numbers (1-indexed) e.g., `[filename]_categorized_failed_pages_4_9.pdf` (consistent with Phase 02 D-08).
- **D-09:** The PDF Page Label for a failed page will be formatted as `{page_num} - Failed`.

</decisions>

<canonical_refs>
## Canonical References

**Downstream agents MUST read these before planning or implementing.**

### Project Scope
- `.planning/PROJECT.md` — Core value and context.
- `.planning/REQUIREMENTS.md` — Requirements OUT-01, OUT-02.

### Prior Phases
- `.planning/phases/01-cli-scaffolding/01-CONTEXT.md`
- `.planning/phases/02-image-processing/02-CONTEXT.md` — Context about smart naming for failed pages and output structure.
- `.planning/phases/03-ai-classification/03-CONTEXT.md` — Context about the AI returning a category and a reason.

</canonical_refs>

<code_context>
## Existing Code Insights

### Reusable Assets
- `src/cli.py` and `src/image_processing.py` handle the primary pipeline logic.
- `progress.json` (Phase 02) will dictate which pages succeeded/failed.

### Established Patterns
- Separate report file generated per PDF.
- 1-indexed page numbering for human-readable outputs and filenames.

### Integration Points
- `fitz` (PyMuPDF) will be used to load the original PDF and inject Page Labels before saving as `[filename]_categorized...pdf`.
- `progress.json` data + AI results will be compiled into the final `[filename]_report.json`.

</code_context>

<specifics>
## Specific Ideas

- None

</specifics>

<deferred>
## Deferred Ideas

- None

</deferred>

---

*Phase: 04-reporting-metadata*
*Context gathered: 2026-06-30*
