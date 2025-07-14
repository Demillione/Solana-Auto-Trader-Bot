import openai
import os

def ask_gpt_about_token(token_name):
    openai.api_key = os.getenv("GROK_API_KEY")
    prompt = f"What is the sentiment on Twitter about {token_name}? Are influencers discussing it?"
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "user", "content": prompt}]
    )
    return response.choices[0].message.content