# Python + AI: From Zero to Building Intelligent Applications

**Complete code for the book by Ayyanar**

Every chapter's code — from `print("Hello, World!")` to AI-powered web apps.

---

## 📁 Repository Structure

```
chapter-01-welcome-to-python/        # print, variables, input, f-strings
chapter-02-variables-types-operators/ # data types, operators, calculator
chapter-03-control-flow/             # if/else, loops, guessing game
chapter-04-data-structures/          # lists, dicts, tuples, sets, contact book
chapter-05-functions-modules/        # functions, *args, modules, password tool
chapter-06-files-error-handling/     # files, CSV, JSON, try/except, expense tracker
chapter-07-oop/                      # classes, inheritance, library system
chapter-08-apis/                     # HTTP requests, weather dashboard
chapter-09-pandas/                   # DataFrames, data analysis
chapter-10-web-scraping/             # BeautifulSoup, price tracker
chapter-11-databases/                # SQLite, task manager
chapter-12-understanding-ai/         # AI concepts, tokens, cost estimation
chapter-13-first-ai-app/            # OpenAI API, chatbot, streaming, vision
chapter-14-prompt-engineering/       # prompting, JSON output, AI assistant
chapter-15-ai-tools/                # function calling, agents, research assistant
chapter-16-rag/                     # embeddings, ChromaDB, document chat
chapter-17-automation/              # batch processing, pipelines
chapter-18-capstone-finance/        # AI expense tracker with auto-categorization
chapter-19-capstone-doc-qa/         # multi-document Q&A with RAG
chapter-20-capstone-streamlit/      # AI web app with Streamlit
chapter-21-whats-next/              # Ollama, career roadmap
```

---

## 🚀 Quick Start

### Part 1–2 (Chapters 1–11): No setup needed
```bash
# Just run any file with Python 3.10+
python chapter-01-welcome-to-python/greeting.py
python chapter-03-control-flow/guessing_game.py
python chapter-06-files-error-handling/expense_tracker.py
```

### Part 3–4 (Chapters 12–21): AI chapters need an API key
```bash
# 1. Install dependencies
pip install openai python-dotenv

# 2. Create a .env file in the chapter folder
echo "OPENAI_API_KEY=your-key-here" > chapter-13-first-ai-app/.env

# 3. Run
python chapter-13-first-ai-app/chatbot.py
```

---

## 📦 Requirements by Chapter

| Chapters | Packages | Install |
|----------|----------|---------|
| 1–7, 11–12 | None (standard library only) | — |
| 8 | requests | `pip install requests` |
| 9 | pandas | `pip install pandas` |
| 10 | beautifulsoup4, requests | `pip install beautifulsoup4 requests` |
| 13–15, 17–18 | openai, python-dotenv | `pip install openai python-dotenv` |
| 16, 19 | openai, chromadb, python-dotenv | `pip install openai chromadb python-dotenv` |
| 20 | streamlit, openai, python-dotenv | `pip install streamlit openai python-dotenv` |

Or install everything at once:
```bash
pip install openai python-dotenv pandas requests beautifulsoup4 chromadb streamlit schedule
```

---

## 🔑 API Key Setup

Chapters 13–21 require an OpenAI API key:

1. Get your key at [platform.openai.com/api-keys](https://platform.openai.com/api-keys)
2. Copy `.env.example` to `.env` in the chapter folder
3. Add your key: `OPENAI_API_KEY=sk-...`

> ⚠️ **Never commit your `.env` file.** The `.gitignore` already excludes it.

---

## 📚 Chapter Projects

| Ch | Project | What It Does |
|----|---------|-------------|
| 1 | Greeting Generator | Interactive greeting with age calculation |
| 2 | Calculator | Four operations with division-by-zero handling |
| 3 | Guessing Game | Random number game with 7 attempts and scoring |
| 4 | Contact Book | Add, search, delete contacts with dictionaries |
| 5 | Password Tool | Generate and check password strength |
| 6 | Expense Tracker | Track expenses with CSV persistence |
| 7 | Library System | OOP-based book lending system |
| 8 | Weather Dashboard | Live weather data from API |
| 9 | Sales Analyzer | Pandas-powered data analysis |
| 10 | Price Tracker | Web scraping with Beautiful Soup |
| 11 | Task Manager | SQLite-backed todo application |
| 13 | AI Chatbot | Terminal chatbot with conversation history |
| 14 | AI Assistant | Summarizer, translator, data extractor, code reviewer |
| 15 | Research Assistant | AI-powered text analysis and report generation |
| 16 | Document Chat | RAG pipeline — chat with your .txt files |
| 17 | Automation Pipeline | Batch AI processing with logging |
| 18 | Finance Tracker | AI auto-categorizes expenses + spending insights |
| 19 | Document Q&A | Multi-document RAG with source citations |
| 20 | Streamlit App | Full web app: chat, summarize, translate, extract |

---

## 🐍 Python Version

Requires **Python 3.10+**. Tested with Python 3.12 and 3.13.

---

## 📖 About the Book

*Python + AI: From Zero to Building Intelligent Applications* takes you from absolute beginner to building AI-powered applications across 21 chapters and 4 parts.

Available on Amazon KDP and Gumroad.

---

## 🐛 Found a Bug?

Open an issue on this repository. Include the chapter number and the error message.

---

## 📜 License

Code in this repository is provided for educational purposes as companion material to the book.
