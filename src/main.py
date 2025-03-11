"""
Main interface module
"""
import json
import os
from openai import OpenAI
from src.config import config, tools
from src.classes.function_handler import FunctionHandler


# Initialize API client
api_key = os.getenv("OPENAI_KEY")
client = OpenAI(api_key=api_key)

# Store conversation history
conversation_history = [
    {"role": "system", "content": config.system_role},
    {"role": "system", "content": config.function_guidance},
    {"role": "assistant", "content": config.configure_taste_profile}
]


def chatgpt_response(prompt: str, sys_prompt: bool = False):
    """Send a message to the chat model and retain full conversation history."""
    # Append user input to conversation history
    if not sys_prompt:
        conversation_history.append({"role": "user", "content": prompt})
    else:
        conversation_history.append({"role": "system", "content": prompt})

    # Get AI response with the full conversation history
    chat_completion = client.chat.completions.create(
        model="gpt-4o",
        messages=conversation_history,
        functions=tools.tools
    )

    # Extract response content

    response = chat_completion.choices[0].message
    if response.function_call:
        function = response.function_call
        func_name = function.name
        arguments = json.loads(function.arguments)
        function = FunctionHandler(func_name)
        function_response = function.execute([arg for arg in arguments.items()])

        conversation_history.append({"role": "system", "content": json.dumps(function_response)})
        chatgpt_response(
            "Craft a response to the outcome of the last function",
            True
        )

    # Append assistant response to conversation history
    conversation_history.append({"role": "assistant", "content": response.content})

    return response.content


# Main chat loop
print("ChatGPT (type 'exit' to quit):")
while True:
    user_input = input("You: ")
    if user_input.lower() == "exit":
        break
    else:
        chat_response = chatgpt_response(user_input)
        print("AI:", chat_response)
