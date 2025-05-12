import os
import asyncio
import google.generativeai as genai

genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

async def ask_gemini(question):
    model = genai.GenerativeModel('gemini-pro')
    loop = asyncio.get_event_loop()
    response = await loop.run_in_executor(None, model.generate_content, question)
    return response.text
