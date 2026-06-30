import json
import os

def load_categories(filepath: str) -> list[str]:
    if not os.path.isfile(filepath):
        raise FileNotFoundError(f"Categories file not found: {filepath}")
    
    with open(filepath, 'r', encoding='utf-8') as f:
        if filepath.endswith('.json'):
            categories = json.load(f)
            return [str(cat).strip() for cat in categories if str(cat).strip()]
        else:
            categories = []
            for line in f:
                stripped = line.strip()
                if stripped:
                    categories.append(stripped)
            return categories
