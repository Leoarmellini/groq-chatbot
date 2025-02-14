import os
from pydantic import BaseModel, Field
from typing import List
from groq import Groq
import instructor

class Character(BaseModel):
    name: str
    fact: List[str] = Field(..., description="A list of facts about the subject")

def get_user_input():
    return input("\nEnter a question (or 'quit' to exit): ")

def run(question):
    api_key = "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"

    client = Groq(api_key=api_key)
    client_with_tools = instructor.from_groq(client, mode=instructor.Mode.TOOLS)

    try:
        resp = client_with_tools.chat.completions.create(
            model="mixtral-8x7b-32768",
            messages=[{"role": "user", "content": question}],
            response_model=Character
        )

        print(f"\n📝 Topic: {resp.name}\n")
        for i, fact in enumerate(resp.fact, start=1):
            print(f"🔹 {fact}")

    except Exception as e:
        print(f"❌ API Request Failed: {e}")

if __name__ == "__main__":
    while True:
        user_input = get_user_input()
        if user_input.lower() == 'quit':
            print("\n👋Have a great day!")
            break
        run(user_input)

