import os
import requests
import time
from openai import OpenAI
from dotenv import load_dotenv
history = [{"role": "system", "content": "You are a helpful assistant who answers questions concisely."}]
OLLAMA_URL = os.getenv("OLLAMA_HOST", "http://ollama:11434")

def local_chat(prompt: str):
    history.append({"role": "user", "content": prompt})
    response = requests.post(
        f"{OLLAMA_URL}/api/chat",
        json={
            "model": "llama3",
            "messages": history,
            "stream": False,
        }
    )
    response.raise_for_status()
    response = response.json()["message"]["content"]
    history.append({"role": "assistant", "content": response})
    return response

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
              "role": "system",
              "content": "You are a helpful assistant who answers questions concisely."
            },
            {
              "role": "user",
              "content": modified(prompt)
            }
          ]
        )
        return completion.choices[0].message.content
    except Exception as e:
        print(f"Error: {e}")
        return  "### Anyone have a good question for us?"
