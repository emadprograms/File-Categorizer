import os
import json
import fitz

def generate_report(progress_data):
    """
    Generates a JSON report keyed by 1-indexed page numbers.
    progress_data: dict from progress.json. Keys are typically "page_1", "page_2", etc.
    Returns: a dict mapping page numbers (string) to their category, reason, and telemetry.
    """
    report = {}
    for key, value in progress_data.items():
        if key.startswith("page_"):
            page_num_str = key.replace("page_", "")
            
            if isinstance(value, dict) and value.get("status") == "error":
                report[page_num_str] = {
                    "category": "Failed",
                    "reason": value.get("error", "Unknown error"),
                    "telemetry": value.get("telemetry", {})
                }
            elif value == "error":
                report[page_num_str] = {
                    "category": "Failed",
                    "reason": "Unknown error",
                    "telemetry": {}
                }
            elif isinstance(value, dict):
                report[page_num_str] = {
                    "category": value.get("category", "Uncategorized"),
                    "reason": value.get("reason", ""),
                    "telemetry": value.get("telemetry", {})
                }
            else:
                report[page_num_str] = {
                    "category": "Uncategorized",
                    "reason": "Invalid status format",
                    "telemetry": {}
                }
    return report

def inject_pdf_metadata(input_pdf_path, output_pdf_path, report_data):
    """
    Injects Page Labels into a PyMuPDF document using format "{page_num} - {category}".
    """
    doc = fitz.open(input_pdf_path)
    
    rules = []
    for i in range(len(doc)):
        page_num_str = str(i + 1)
        page_info = report_data.get(page_num_str, {})
        category = page_info.get("category", "Uncategorized")
        
        prefix = f"{i + 1} - {category}"
        rules.append({"startpage": i, "prefix": prefix, "style": ""})
        
    doc.set_page_labels(rules)
    doc.save(output_pdf_path)
    doc.close()
