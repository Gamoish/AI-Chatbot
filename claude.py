import os
import asyncio
from anthropic import AsyncAnthropic

# Load the API key (or replace os.getenv with your key directly)
api_key = os.getenv("ANTHROPIC_API_KEY")

client = AsyncAnthropic(api_key=api_key)

async def ask_claude(question, model="claude-3-sonnet-20240229"):
    message = await client.messages.create(
        model=model,
        max_tokens=1024,
        messages=[{"role": "user", "content": question}],
    )
    return message.content[0].text  # Extract response

# Example usage
if __name__ == "__main__":
    async def main():
        reply = await ask_claude("Explain quantum computing like I'm 12.")
        print(reply)

    asyncio.run(main())
