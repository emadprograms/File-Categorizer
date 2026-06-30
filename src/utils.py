"""
Utility functions for the File Categorizer application.

This module provides helper functions for loading and parsing category definitions.
"""
import json
import os

def load_categories(filepath: str) -> list[str]:
    """
    Load categories from a file or parse them from a comma-separated string.

    Args:
        filepath: A string representing either a path to a text/JSON file containing
                  categories, or a comma-separated list of categories.

    Returns:
        A list of category strings.

    Raises:
        ValueError: If the input is not a valid file path and doesn't appear to be
                    a valid comma-separated list.
    """
    if not os.path.isfile(filepath):
        # Treat as a comma-separated list
        categories = [cat.strip() for cat in filepath.split(',') if cat.strip()]
        if categories:
            return categories
        raise ValueError(f"Input is not a valid file path or comma-separated list: {filepath}")
    
    with open(filepath, 'r', encoding='utf-8') as f:
        if filepath.endswith('.json'):
            raw_categories = json.load(f)
            categories = [str(cat).strip() for cat in raw_categories if str(cat).strip()]
            if not categories:
                raise ValueError(f"No categories found in JSON file: {filepath}")
            return categories
        else:
            categories = []
            for line in f:
                stripped = line.strip()
                if stripped:
                    categories.append(stripped)
            
            if not categories:
                raise ValueError(f"No categories found in file: {filepath}")
            return categories
