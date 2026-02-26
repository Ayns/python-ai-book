# Chapter 12 - Exercise Solutions (Conceptual)
# No code exercises — this is a conceptual chapter.
# Review questions:

# 1. What is the relationship between AI, ML, Deep Learning, and GenAI?
# Answer: AI > ML > Deep Learning > GenAI (nested hierarchy)

# 2. Calculate token cost:
# A 1000-word document is approximately 1,333 tokens
# At $0.40/1M input tokens (gpt-4.1-mini):
tokens = 1333
cost_per_million = 0.40
cost = (tokens / 1_000_000) * cost_per_million
print(f"Cost for 1000 words: ${cost:.6f} (about ${cost*1000:.4f} per 1000 requests)")

# 3. When to use which model tier:
print("""
Model selection guide:
  - Fast/cheap (Haiku, gpt-4.1-mini): Classification, formatting, simple Q&A
  - Balanced (Sonnet, gpt-4.1): Most tasks, coding, analysis
  - Maximum (Opus, gpt-5): Complex reasoning, research, critical decisions
""")
