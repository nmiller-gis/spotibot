"""
Main interface module
"""
import os
import config
from openai import OpenAI

# Initialize API client
api_key = os.getenv("OPENAI_KEY")
client = OpenAI(api_key=api_key)

# Store conversation history
conversation_history = [
    {"role": "system", "content": config.system_role},
    {"role": "assistant", "content": config.configure_taste_profile}
]


def chatgpt_response(prompt: str):
    """Send a message to the chat model and retain full conversation history."""
    # Append user input to conversation history
    conversation_history.append({"role": "user", "content": prompt})

    # Get AI response with the full conversation history
    chat_completion = client.chat.completions.create(
        model="gpt-4o",
        messages=conversation_history
    )

    # Extract response content
    response_content = chat_completion.choices[0].message.content

    # Append assistant response to conversation history
    conversation_history.append({"role": "assistant", "content": response_content})

    return response_content


# Main chat loop
print("ChatGPT (type 'exit' to quit):")
while True:
    user_input = input("You: ")
    if user_input.lower() == "exit":
        break
    else:
        chat_response = chatgpt_response(user_input)
        print("AI:", chat_response)
