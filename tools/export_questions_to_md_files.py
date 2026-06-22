import requests
import os
import re

# === Configuration ===
API_URL = "https://community.simplicite.io/admin/plugins/explorer/queries/8/run"
API_KEY = os.getenv("COMMUNITY_API_KEY")
if not API_KEY:
    API_KEY = input("Please enter your API key: ")  # fallback to user input
API_USERNAME = "system"
OUTPUT_DIR = "../topics"

# === Functions ===

def fetch_data():
    headers = {
        "Api-Key": API_KEY,
        "Api-Username": API_USERNAME
    }
    response = requests.post(API_URL, headers=headers)
    if response.status_code != 200:
        raise Exception(f"Failed to fetch data. Status code: {response.status_code}\n{response.text}")
    return response.json()

def slugify(title, fallback_id=None):
    if not title or not str(title).strip():
        return f"topic_{fallback_id}" if fallback_id is not None else "untitled"
    return re.sub(r'[^\w\-]+', '_', str(title).strip().lower())[:100]

def sanitize_markdown(text):
    if text is None:
        return ""
    return str(text).strip()

def save_markdown_file(id, title, question, answer):
    filename = slugify(title, fallback_id=id) + ".md"
    filepath = os.path.join(OUTPUT_DIR, filename)
    
    # Create URL by concatenating base URL with ID
    url = f"https://community.simplicite.io/t/{id}"
    
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(f"# {title}\n\n")
        f.write(f"**URL:** {url}\n\n")
        f.write(f"## Question\n{sanitize_markdown(question)}\n\n")
        answer_text = sanitize_markdown(answer) or "_No answer provided._"
        f.write(f"## Answer\n{answer_text}\n")
    
    print(f"✅ Created: {filepath}")

def main():
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    data = fetch_data()

    if not data.get("success"):
        raise Exception("API returned an unsuccessful response.")
    
    for row in data.get("rows", []):
        id, title, question, answer = row
        save_markdown_file(id, title, question, answer)

if __name__ == "__main__":
    main()
