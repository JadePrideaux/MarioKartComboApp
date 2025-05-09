import json


def save_to_json(data, filename="components.json"):
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4, ensure_ascii=False)
    print(f"Data successfully saved to {filename}")
