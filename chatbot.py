from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()

client = OpenAI(
    api_key=os.getenv("GROQ_API_KEY"),
    base_url="https://api.groq.com/openai/v1"
)

message = [{
    "role" : "developer",
    "content" : "You are a helpful assistant"
}]

while True:
    user_input = input("You : ")

    if user_input.startswith("/switch"):
        new_role = user_input.replace("/switch", "").strip()
        message[0] = {"role": "developer", "content": f"You are a {new_role}."}
        print(f"Switched to {new_role} mode.\n")
        continue
    
    if user_input.lower() == "exit":
        break

    message.append(
        {"role" : "user", "content" : user_input}
    )

    response = client.responses.create(
    model="openai/gpt-oss-120b",
    input= message,
    stream=True
)
    full_reply = ""
    print("Bot: ", end="")
    for event in response:
        if event.type == "response.output_text.delta":
            print(event.delta, end="", flush=True)
            full_reply += event.delta

    print()
    message.append(
        {"role" : "assistant", "content" : full_reply}
    )