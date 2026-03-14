from openai import OpenAI
from dotenv import load_dotenv
import os
load_dotenv()
client=OpenAI(api_key=os.getenv("GEMINI_API_KEY"),
              base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
              )
response=client.chat.completions.create(
  model="gemini-2.5-flash",
  messages=[
      {"role":"system","content":"Youre just an expert in mathematics and knows nothing about other topic and dont respond to other topics, and say sorry u are just an expert of math and can only help with math formulas and logic if other topics were asked"}, 
      {"role":"user","content":"Hello , Aasif Here nice to meet you,write a python code"}

  ]
)

print(response.choices[0].message.content)