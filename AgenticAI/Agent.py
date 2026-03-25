from openai import OpenAI
import os
from dotenv import load_dotenv
import json
import requests
load_dotenv()
client=OpenAI(api_key=os.getenv("GEMINI_API_KEY"),
               base_url="https://generativelanguage.googleapis.com/v1beta/openai/")
def get_weather(city:str):
    url = f"https://wttr.in/{city}?format=j1" 
    response=requests.get(url)
    if response.status_code==200:
        return f"Weather in {city} is {response.text}"
    return "Something went wrong"
tools=[{
    "type":"function",
    "function":{
        "name":"get_weather",
        "description":"Get current weather of a city",
        "parameters":{
            "type":"object",
            "properties":{
                "city":{"type":"string"}
                
            },
            "required":["city"]
        }
    }
}]
# tool call
def Agent(user_query):
    response=client.chat.completions.create(
        model="gemini-2.5-flash",
        messages=[{"role":"user","content":user_query}],
        tools=tools
    )
    message=response.choices[0].message
    # checking if tool is called or not
    if message.tool_calls:
        tool_call=message.tool_calls[0]
        args=json.loads(tool_call.function.arguments)
        result=get_weather(args["city"])
        return f"weather is: {json.dumps(result)}"
    return message.content
print(Agent("whats current weather in delhi?"))