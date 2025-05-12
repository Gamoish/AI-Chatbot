import os
import discord
from discord.ext import commands
from dotenv import load_dotenv
from filter import classify_question
from ai_clients.openai_client import ask_openai
from ai_clients.gemini_client import ask_gemini
# import other AI clients similarly

load_dotenv()

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user}')

@bot.command()
async def ask(ctx, *, question):
    await ctx.send("Thinking... 🤔")

    # Classify the question
    selected_ai = await classify_question(question)

    # Route to appropriate AI
    if selected_ai == "openai":
        response = await ask_openai(question)
    elif selected_ai == "gemini":
        response = await ask_gemini(question)
    else:
        response = "Sorry, couldn't find a suitable AI for your question."

    await ctx.send(f"🤖 **[{selected_ai.upper()}] Answer:** {response}")

bot.run(os.getenv('MTM2NjQ4MzA4MzA0NTM3MjA2NQ.GTX4aP.wH0BqSlZCss3WSedvGawJcLA9CSxWdOmN5dC4E'))
