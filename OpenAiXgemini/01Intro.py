from openai import OpenAI
import os
from dotenv import load_dotenv
load_dotenv()
client = OpenAI( api_key=os.getenv("GEMINI_API_KEY"),
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
)
response = client.chat.completions.create(
    model="gemini-2.5-flash", # Use a current model, e.g., gpt-4o
    messages=[
        {"role": "user", "content": "What is the capital of France?"}
    ]
)

print(response.choices[0].message.content)
