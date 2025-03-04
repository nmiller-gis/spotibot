import os
from openai import OpenAI

api_key = os.getenv("OPENAI_KEY")
client = OpenAI(
    api_key=os.getenv("OPENAI_KEY")
)


def chatgpt_response(prompt: str):
    chat_completion = client.chat.completions.create(
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ],
        model="gpt-4o"
    )
    return chat_completion.choices[0].message.content


while True:
    user_input = input()
    if user_input.lower() == "exit":
        break
    else:
        chat_response = chatgpt_response(user_input)
        print(chat_response)
