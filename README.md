# 🤖 AI Multi-Chatbot Discord Bot

![Python](https://img.shields.io/badge/Python-3.8%2B-blue.svg)
![License](https://img.shields.io/badge/License-MIT-green.svg)
![OpenAI](https://img.shields.io/badge/OpenAI-Integrated-success)
![Gemini](https://img.shields.io/badge/Gemini-Enabled-brightgreen)
![Claude](https://img.shields.io/badge/Claude-Connected-yellowgreen)

> A smart Discord bot that intelligently routes your message to the most suitable AI chatbot—**OpenAI**, **Gemini**, or **Claude**—based on query content.

---

## 📌 About the Project

This Discord bot serves as an **AI-powered multi-bot router**. It uses a custom filter to determine the context of user queries and routes them to the best matching AI service among OpenAI, Gemini, and Claude.

This project demonstrates:
- Natural Language Understanding (NLU)
- Discord bot development
- Multi-model integration
- Scalable AI interaction logic

---

## ⚙️ Features

- 🔁 **Smart AI Routing** using `filter.py`
- 💬 **Seamless Discord Integration** via `bot.py`
- 🤝 Supports three major AI platforms:
  - 🧠 `openai_client.py` – General, creative, and programming queries
  - 🧾 `gemini_client.py` – Research and fact-based responses
  - 📘 `claude_client.py` – Summarization, polite conversation, ethical replies
- 🛠️ Easy to extend with new AI services or improve routing logic
- 🔐 Secure key management using `.env`

---

## 🧾 Project Structure

ai-multibot-discord/
├── .env               → Environment variables (not committed)
├── LICENSE            → Project license (MIT)
├── README.md          → Project documentation
├── requirements.txt   → Python dependencies
├── bot.py             → Main bot logic and Discord event handling
├── filter.py          → Core routing logic (chooses best AI)
├── openai_client.py   → Handles OpenAI requests and responses
├── gemini_client.py   → Handles Gemini API interaction
├── claude_client.py   → Handles Claude API integration


---

## 🚀 Getting Started

### 🔧 Prerequisites
- Python 3.8+
- `pip`
- Discord Bot Token
- API keys for:
  - OpenAI
  - Google Gemini
  - Anthropic Claude

### 📥 Installation

```bash
git clone https://github.com/your-username/your-repo-name.git
cd your-repo-name
pip install -r requirements.txt
🔐 Environment Variables
Create a .env file in the root with the following keys:

env
Copy
Edit
DISCORD_TOKEN=your_discord_bot_token
OPENAI_API_KEY=your_openai_api_key
GEMINI_API_KEY=your_gemini_api_key
CLAUDE_API_KEY=your_claude_api_key▶️ Run the Bot
bash
Copy
Edit
python bot.py
Once running, invite the bot to your server and simply ask questions—it’ll route them to the best-suited AI.

🧠 How It Works
bot.py listens to incoming messages on Discord.

The message is passed to filter.py, which analyzes it.

Based on intent/type, the appropriate AI handler (*_client.py) is called.

The response is sent back to the user in the Discord server.

User: "Summarize this paragraph."
→ Filter selects Claude
→ Claude responds with summary
→ Bot sends it in channel
🧩 Future Improvements
 Add feedback loop for smarter routing

 Logging dashboard

 LLM-based intent detection model

 Slash command support and interactive embeds

🤝 Contributing
Pull requests are welcome! For major changes, open an issue first to discuss your proposal.

📜 License
This project is licensed under the MIT License.

🌐 Links
🐙 GitHub: @Gamoish








