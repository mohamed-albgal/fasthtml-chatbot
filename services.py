import os
import time
from openai import OpenAI
from dotenv import load_dotenv

def chat(prompt: str):
    """
    This function handles the chat service.
    calls chatgpt and returns the response.
    """

    # Load environment variables from .env file

    load_dotenv()
    client = OpenAI(
      base_url="https://openrouter.ai/api/v1",
      api_key=os.getenv("OPENROUTER_KEY"),
    )

    completion = client.chat.completions.create(
      extra_body={},
      model="deepseek/deepseek-chat-v3-0324:free",
      messages=[
        {
          "role": "user",
          "content": modified(prompt)
        }
      ]
    )
    try:
        1/0
        return completion.choices[0].message.content
    except Exception as e:
        time.sleep(2)
        return "Error at this time.."


def modified(prompt: str):
    suffix = " (I only want short answers)"
    return prompt + suffix

