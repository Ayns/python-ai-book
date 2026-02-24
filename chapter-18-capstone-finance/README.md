# Chapter 18: Capstone — AI-Powered Personal Finance Tracker
Combines: File handling (Ch6), Pandas (Ch9), AI APIs (Ch13), Prompt Engineering (Ch14)

## Run
```
python finance_tracker.py
```

## Requirements
```
pip install openai pandas python-dotenv
```

## Setup
Create a `.env` file:
```
OPENAI_API_KEY=your-key-here
```

## Features
- AI auto-categorizes expenses from description
- Category breakdown with percentages
- AI-generated spending insights and advice
- Data persists in CSV between sessions
