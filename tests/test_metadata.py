import pytest
import os
import fitz
from src.metadata import generate_report, inject_pdf_metadata

def test_generate_report_success():
    progress_data = {
        "page_1": {
            "status": "success",
            "category": "Invoice",
            "reason": "Looks like an invoice",
            "telemetry": {"duration": 1.2}
        },
        "page_2": {
            "status": "success",
            "category": "Receipt",
            "reason": "Contains receipt details",
            "telemetry": {"duration": 0.8}
        }
    }
    
    report = generate_report(progress_data)
    
    assert report["1"]["category"] == "Invoice"
    assert report["1"]["reason"] == "Looks like an invoice"
    assert report["1"]["telemetry"]["duration"] == 1.2
    
    assert report["2"]["category"] == "Receipt"

def test_generate_report_failed():
    progress_data = {
        "page_3": {
            "status": "error",
            "error": "Timeout occurred",
            "telemetry": {"retries": 3}
        },
        "page_4": "error"
    }
    
    report = generate_report(progress_data)
    
    assert report["3"]["category"] == "Failed"
    assert report["3"]["reason"] == "Timeout occurred"
    assert report["3"]["telemetry"]["retries"] == 3
    
    assert report["4"]["category"] == "Failed"
    assert report["4"]["reason"] == "Unknown error"

def test_inject_pdf_metadata(tmp_path):
    input_pdf = tmp_path / "test_input.pdf"
    output_pdf = tmp_path / "test_output.pdf"
    
    # Create a dummy PDF with 2 pages
    doc = fitz.open()
    doc.new_page()
    doc.new_page()
    doc.save(str(input_pdf))
    doc.close()
    
    report_data = {
        "1": {"category": "Invoice"},
        "2": {"category": "Failed"}
    }
    
    inject_pdf_metadata(str(input_pdf), str(output_pdf), report_data)
    
    # Verify labels
    doc2 = fitz.open(str(output_pdf))
    labels = doc2.get_page_labels()
    # PyMuPDF get_page_labels returns a list of rule dicts like the ones passed
    assert len(labels) == 2
    assert labels[0]["prefix"] == "1 - Invoice"
    assert labels[1]["prefix"] == "2 - Failed"
    doc2.close()
