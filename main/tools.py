import os
import fitz
import json
import docx
import requests


# Конфигурация API
OPENROUTER_API_KEY = "your-api-key"
OPENROUTER_API_URL = "https://openrouter.ai/api/v1/chat/completions"


def call_ai(prompt: str, content: str):
    headers = {
        "Authorization": f"Bearer {OPENROUTER_API_KEY}",
        "Content-Type": "application/json",
    }

    payload = {
        "model": "meta-llama/llama-4-maverick:free",
        "messages": [
            {"role": "user", "content": f"{prompt}\n\n{content}"}
        ]
    }
    response = requests.post(
        OPENROUTER_API_URL,
        headers=headers,
        data=json.dumps(payload)
    )
    response.raise_for_status()

    result = response.json()
    return result['choices'][0]['message']['content']


def extract_text_from_file(path):
    ext = os.path.splitext(path)[1].lower()

    if ext == '.txt':
        with open(path, 'r', encoding='utf-8', errors='ignore') as f:
            return f.read()

    elif ext == '.pdf':
        text = ""
        with fitz.open(path) as doc:
            for page in doc:
                text += page.get_text()
        return text

    elif ext == '.docx':
        doc = docx.Document(path)
        return "\n".join(p.text for p in doc.paragraphs)

    else:
        raise ValueError("Unsupported file type")
