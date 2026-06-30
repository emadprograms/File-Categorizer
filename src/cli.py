import argparse

def parse_args(args=None):
    parser = argparse.ArgumentParser(description="Arabic PDF OCR & Categorization CLI")
    parser.add_argument("-i", "--input-pdfs", nargs="+", required=True, help="Input PDF files")
    parser.add_argument("-c", "--categories-file", required=True, help="Path to categories file")
    parser.add_argument("-o", "--output-dir", required=True, help="Output directory")
    return parser.parse_args(args)

import sys
import os

# Ensure the root directory is in sys.path when running as a script
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from src.utils import load_categories

def main():
    args = parse_args()
    
    # Load categories
    try:
        categories = load_categories(args.categories_file)
    except Exception as e:
        print(f"Error loading categories: {e}", file=sys.stderr)
        sys.exit(1)
        
    # Validate input PDFs
    for pdf_path in args.input_pdfs:
        if not os.path.isfile(pdf_path):
            print(f"Error: Input PDF file not found: {pdf_path}", file=sys.stderr)
            sys.exit(1)
            
    # Create output directory if it doesn't exist
    os.makedirs(args.output_dir, exist_ok=True)
    
    print(f"Input PDFs: {args.input_pdfs}")
    print(f"Categories: {categories}")
    print(f"Output Directory: {args.output_dir}")

if __name__ == "__main__":
    main()
