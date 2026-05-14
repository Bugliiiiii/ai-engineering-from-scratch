import os
from dotenv import load_dotenv    
import anthropic
load_dotenv()
client = anthropic.Anthropic(
    api_key=os.getenv("ANTHROPIC_API_KEY"),
    base_url="https://api.deepseek.com/anthropic"
)

response = client.messages.create(
    model="deepseek-v4-pro",
    max_tokens=1000,
    messages=[{"role": "user", 
               
               "content": [
                {
                    "type": "text",
                    "text": "What is a neural network in one sentence?"
                }
            ]
               
               }
               
               ]
)

for block in response.content:
    if block.type == "text":
        print(block.text)


