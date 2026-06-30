import argparse

def parse_args(args=None):
    parser = argparse.ArgumentParser(description="Arabic PDF OCR & Categorization CLI")
    parser.add_argument("-i", "--input-pdfs", nargs="+", required=True, help="Input PDF files")
    parser.add_argument("-c", "--categories-file", required=True, help="Path to categories file")
    parser.add_argument("-o", "--output-dir", required=True, help="Output directory")
    return parser.parse_args(args)

def main():
    args = parse_args()
    print(f"Input PDFs: {args.input_pdfs}")
    print(f"Categories File: {args.categories_file}")
    print(f"Output Directory: {args.output_dir}")

if __name__ == "__main__":
    main()
