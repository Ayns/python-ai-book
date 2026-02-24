# Understanding AI: The Big Picture - Chapter 12
# This chapter is conceptual. These are the code snippets used to illustrate key ideas.

# ─── Token Estimation ───
text = "Hello, how are you today?"
estimated_tokens = len(text) / 4  # rough estimate: 1 token ≈ 4 characters
print(f"Text: '{text}'")
print(f"Estimated tokens: {estimated_tokens:.0f}")


# ─── Temperature Demonstration ───
# Temperature 0 = deterministic (always same answer)
# Temperature 1 = creative (different each time)
# This is a parameter you pass to the API:
#
#   response = client.chat.completions.create(
#       model="gpt-4.1-mini",
#       messages=[...],
#       temperature=0.3   # <-- low = predictable
#   )


# ─── Cost Calculation ───
# GPT-4.1-mini pricing (as of early 2026):
#   Input:  ~$0.40 per 1M tokens
#   Output: ~$1.60 per 1M tokens

emails_per_day = 500
tokens_per_email = 200  # input + output
total_tokens = emails_per_day * tokens_per_email
cost_per_day = (total_tokens / 1_000_000) * 2.00  # approximate combined rate

print(f"\nEmail classifier cost estimate:")
print(f"  Emails/day:    {emails_per_day}")
print(f"  Tokens/email:  {tokens_per_email}")
print(f"  Daily tokens:  {total_tokens:,}")
print(f"  Daily cost:    ${cost_per_day:.2f}")
print(f"  Monthly cost:  ${cost_per_day * 30:.2f}")
