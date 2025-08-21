import os
import requests
import json

SAMBA_API_KEY = os.getenv("SAMBA_API_KEY")
SAMBA_API_URL = os.getenv("SAMBA_API_URL")

HEADERS = {
    "Authorization": f"Bearer {SAMBA_API_KEY}",
    "Content-Type": "application/json"
}

def ask_sambanova(prompt, max_tokens=150):
    payload = {
        "model": "samba-mini",
        "messages": [{"role": "user", "content": prompt}],
        "max_tokens": max_tokens,
        "temperature": 0.7
    }
    response = requests.post(SAMBA_API_URL, headers=HEADERS, data=json.dumps(payload))
    if response.status_code == 200:
        data = response.json()
        return data.get("choices")[0]["message"]["content"].strip()
    else:
        return f"Error: {response.status_code} - {response.text}"

def explain_concept(concept, style="simple"):
    prompt = f"Explain the concept '{concept}' in a {style} way with examples."
    return ask_sambanova(prompt)

def generate_hint(question):
    prompt = f"Give a helpful hint for solving the following problem: {question}"
    return ask_sambanova(prompt)