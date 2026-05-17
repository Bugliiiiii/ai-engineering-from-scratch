import os
import urllib.request
import json
import ssl

# Try to load .env from project root, but don't fail if dotenv isn't installed
try:
    from dotenv import load_dotenv
    load_dotenv()
except ImportError:
    pass

url = "https://api.deepseek.com/v1/chat/completions"
headers = {
    "Content-Type": "application/json",
    "Authorization": f"Bearer {os.environ.get('ANTHROPIC_API_KEY')}",
}

body = json.dumps({
    "model": "deepseek-v4-flash",
    "messages": [{"role": "user", "content": "What is a neural network in one sentence?"}]
}).encode()

req = urllib.request.Request(url, data=body, headers=headers, method="POST")
context = ssl._create_unverified_context()
with urllib.request.urlopen(req, context=context) as resp:
    result = json.loads(resp.read())
    print(result["choices"][0]["message"]["content"]) 