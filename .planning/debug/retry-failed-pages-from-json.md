---
status: resolved
trigger: "currently when the program fails to extract pages, it just appends the failed page numbers at the end of the file, and if  rerun it. then there is no way for it identify if it supposed to only run the failed ones. we use status but I don't think we use status for determining if it is supposed to re-run. I think when a run starts and there is a 1281_report.json, then first reiterates those pages that failed and then run only those pages. If there is no json file, only then it should do everything from the beginning. don't just look if there json is a file and skip if there is. look inside the json and then act accordingly."
created: 2026-06-30T22:40:00+03:00
updated: 2026-06-30T22:43:00+03:00
---

# Debug Session: retry-failed-pages-from-json

## Symptoms
- **Expected behavior**: When a run starts and there is a `*_report.json`, the program should look inside the json, identify the pages that failed, and only re-run those failed pages. If there is no json file, it should process everything from the beginning.
- **Actual behavior**: When the program fails to extract pages, it appends the failed page numbers at the end of the file. Upon re-run, there is no way for it to identify that it should only run the failed ones. It looks like `status` is used, but not for determining if a page should be re-run.
- **Error messages**: N/A
- **Timeline**: N/A
- **Reproduction**: Run extraction, have pages fail, re-run extraction.

## Current Focus
- hypothesis: The code unconditionally skips a PDF if `report.json` exists without checking for failed pages.
- test: Inspect `main.py`
- expecting: To find an unconditional `continue` or skip block for `report.json` existing.
- next_action: Apply fix in `main.py`
- tdd_checkpoint: null
- reasoning_checkpoint: null

## Evidence
- timestamp: 2026-06-30T22:41:43+03:00
  checked: `main.py` lines 101-104
  found: `if os.path.exists(report_path): continue` skips unconditionally.
  implication: We must parse `report.json` to find if any pages failed and seed `progress.json`.

## Resolution
root_cause: `main.py` unconditionally skipped processing if the `_report.json` file existed, regardless of whether some pages failed during the previous run. The `.tmp_` directory was also deleted at the end of runs, losing `progress.json`.
fix: Modified `main.py` to parse `_report.json` when it exists. It seeds `progress.json` with the already successful pages marked as "classified", and any page with a category not in the valid categories list (which includes "Failed", "Uncategorized", or just extracted) as "error". `process_pdf` and `classify_pages` inherently skip "classified" pages, correctly resuming the workflow just for failed/unclassified pages.
verification: Manual code verification confirms that `progress.json` seeding will skip extraction and classification for already successful pages, while correctly retrying anything that was not successfully classified.
files_changed: 
  - `src/main.py`
