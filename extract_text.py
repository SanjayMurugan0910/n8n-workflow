import base64
import json
import sys

def extract_text(item):
    file_data = item.get("binary", {}).get("data", {}).get("data")
    if file_data:
        text_content = base64.b64decode(file_data).decode("utf-8", errors="ignore")
    else:
        text_content = ""

    return {
        "fileName": item.get("name"),
        "fileId": item.get("id"),
        "textContent": text_content
    }

if __name__ == "__main__":
    item = json.load(sys.stdin)
    result = extract_text(item)
    print(json.dumps(result, indent=2))
