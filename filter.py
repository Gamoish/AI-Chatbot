import openai
import os

openai.api_key = os.getenv("OPENAI_API_KEY")

async def classify_question(question):
    prompt = f"""
You are a router that classifies user questions to the best AI model.
Categories:
- "openai" if it's coding, technical, math, logical reasoning.
- "gemini" if it's creative writing, brainstorming, casual chatting.
- "grok" if it's political, edgy humor, or controversial topics.

Respond with only one word: "openai", "gemini", or "grok".

Question: "{question}"
Answer:"""

    response = await openai.ChatCompletion.acreate(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}],
        max_tokens=1,
        temperature=0
    )
    category = response['choices'][0]['message']['content'].strip().lower()

    if category not in ["openai", "gemini", "grok"]:
        category = "openai"  # default fallback

    return category
