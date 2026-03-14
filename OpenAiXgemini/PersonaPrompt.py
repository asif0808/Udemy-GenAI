from openai import OpenAI
from dotenv import load_dotenv
import os
load_dotenv()
SYSTEM_PROMPT="Act Like virat kohli (Persona Prompting), Short response"
client=OpenAI(api_key=os.getenv("GEMINI_API_KEY"),
              base_url="https://generativelanguage.googleapis.com/v1beta/openai/")

# response=client.chat.completions.create(

#     model="gemini-2.5-flash",
#     messages=[
#         {"role":"system","content":SYSTEM_PROMPT},
#         # {"role":"user","content":"who are you? and why are you so famous?  Keep the response short"},
#         # {"role":"user","content":"any cricket related incident which hurt the most?  Keep the response short"} 
#          {"role":"user","content":"your recent best moment?  Keep the response short"}
#     ]
# )
messages=[
    {"role":"system","content":SYSTEM_PROMPT}
]
while True:
    user_input=input("you: ")
    messages.append({"role":"user","content":user_input})
    response=client.chat.completions.create(
        model="gemini-2.5-flash",
        messages=messages  
            )
    reply=response.choices[0].message.content
    print("Virat: ",reply)
    messages.append({"role":"assistant","content":reply})