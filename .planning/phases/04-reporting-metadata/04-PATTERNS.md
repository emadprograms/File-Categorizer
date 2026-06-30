# Phase 04: reporting-metadata - Pattern Map

**Mapped:** 2026-06-30
**Files analyzed:** 2
**Analogs found:** 1 / 2

## File Classification

| New/Modified File | Role | Data Flow | Closest Analog | Match Quality |
|-------------------|------|-----------|----------------|---------------|
| `src/cli.py` | controller | pipeline | `src/cli.py` | exact |
| `src/metadata.py` | utility | file-I/O | `src/image_processing.py` | role-match |

## Pattern Assignments

### `src/cli.py` (controller, pipeline)

**Analog:** `src/cli.py`

**Error handling pattern**:
```python
try:
    ...
except Exception as e:
    logger.error(f"Error: {str(e)}")
```

## Shared Patterns

### File I/O
**Source:** `src/image_processing.py`
**Apply to:** `src/metadata.py`
```python
import fitz  # PyMuPDF
import json
import os
```

## Metadata

**Analog search scope:** `src/`
**Files scanned:** 2
**Pattern extraction date:** 2026-06-30
