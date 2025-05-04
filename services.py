import os
import time
from openai import OpenAI
from dotenv import load_dotenv

def chat(prompt: str):
    load_dotenv()
    client = OpenAI(
      base_url="https://openrouter.ai/api/v1",
      api_key=os.getenv("OPENROUTER_KEY"),
    )
    try:
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
        return completion.choices[0].message.content
    except Exception as e:
        return "Error at this time.."


def modified(prompt: str):
    suffix = " (Make the response concise and to the point.)"
    return prompt + suffix

