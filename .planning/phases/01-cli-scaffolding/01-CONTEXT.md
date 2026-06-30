# Phase 1 Context: CLI Scaffolding

## Domain
Implement the CLI application that batch-processes PDFs and manages the end-to-end flow. The CLI accepts PDF paths, parses dynamic categories, and orchestrates the image processing, AI classification, and reporting phases.

## Decisions

### Category Input Format
- **Decision:** Use JSON or text file input (e.g., `--categories-file categories.txt`)
- **Rationale:** Better handles dynamic and potentially lengthy or complex category names compared to inline flags or comma-separated strings.

### Batch Output Structure
- **Decision:** Separate report file generated per PDF
- **Rationale:** Easier to manage and trace results back to individual documents, especially when processing large batches.

### PDF Saving Strategy
- **Decision:** Save a copy to a specified output directory with a suffix (e.g., `file_categorized.pdf`)
- **Rationale:** Non-destructive operation that preserves the original files while clearly identifying processed output.

## Code Context
- **Patterns:** (None established yet — Greenfield CLI)
- **Reusable Assets:** (None established yet)

## Canonical Refs
*(None yet)*

## Deferred Ideas
*(None)*
