# Phase 04: reporting-metadata - Discussion Log

**Date:** 2026-06-30

This document records the options presented and selections made during the context gathering phase. It is for human reference and auditing only. Downstream agents should rely on `04-CONTEXT.md`.

## Page Metadata Method
**Options Presented:**
- Use PDF Page Labels (Replaces page numbers like "1, 2" with "Invoice, Receipt" in PDF viewers)
- Use Document-level mapping
- Add invisible text to each page

**Selected:** Use PDF Page Labels

**Follow-up: Format**
**Options Presented:**
- Yes, format as "{page_num} - {category}"
- No, just use the category name
- You decide

**Selected:** Yes, format as "{page_num} - {category}"

## Report Content
**Options Presented:**
- Detailed telemetry (page-to-category mapping, plus processing time, retries, and failure reasons)
- Basic mapping only
- You decide

**Selected:** Detailed telemetry. (User specified: "detailed telemetry but I would like to add that we now use reasons as part of the json as well. so keep that in mind. the ai gives the category and the reason for that category as well.")

**Follow-up: JSON Structure**
**Options Presented:**
- Keyed by page number
- Array of objects
- You decide

**Selected:** Keyed by page number

## CSV Support
**Options Presented:**
- JSON only
- CSV only
- Both JSON and CSV

**Selected:** JSON only

## Failed Pages
**Options Presented:**
- Value is explicitly "Failed", with `reason` containing the error message
- Value is `null`
- Omit the page entirely

**Selected:** Value is explicitly "Failed". (User clarified: "and the filename should be the filenamen and then the failed page numbers with number is it starting from 1")

**Follow-up: Failed Page Label**
**Options Presented:**
- Format as "{page_num} - Failed"
- Leave the original page number unmodified
- You decide

**Selected:** Format as "{page_num} - Failed"
