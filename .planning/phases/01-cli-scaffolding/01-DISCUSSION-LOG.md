# Phase 1 Discussion Log

**Area: Category Input Format**
- **Options presented:**
  - Repeated flags (e.g., `--category "Invoice" --category "Receipt"`)
  - Comma-separated string (e.g., `--categories "Invoice,Receipt"`)
  - JSON/Text file input (e.g., `--categories-file categories.txt`)
- **Selection:** JSON/Text file input

**Area: Batch Output Structure**
- **Options presented:**
  - Single combined report mapping PDF path -> page -> category
  - Separate report file generated per PDF
  - Both
- **Selection:** Separate report file generated per PDF

**Area: PDF Saving Strategy**
- **Options presented:**
  - Save a copy to a specified output directory with a suffix (e.g., `file_categorized.pdf`)
  - Overwrite the original PDFs with the new metadata in-place
  - Ask the user at runtime
- **Selection:** Save a copy to a specified output directory with a suffix
