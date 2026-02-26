# Chapter 15 - Exercise Solutions
# See research_assistant.py for the main project

# 1. Calculator tool for the agent
def calculator_tool(expression):
    """Safely evaluate a math expression."""
    try:
        allowed = set("0123456789+-*/()., ")
        if all(c in allowed for c in expression):
            return str(eval(expression))
        return "Error: invalid expression"
    except Exception as e:
        return f"Error: {e}"

# 2. File reader tool
def read_file_tool(filename):
    """Read a file and return its contents."""
    try:
        with open(filename, "r") as f:
            content = f.read()
        return content[:2000]  # Limit to 2000 chars
    except FileNotFoundError:
        return f"File '{filename}' not found."

# 3. CSV summary tool
def csv_summary_tool(filename):
    """Read a CSV and return basic statistics."""
    import pandas as pd
    try:
        df = pd.read_csv(filename)
        return f"Rows: {len(df)}, Columns: {list(df.columns)}\n{df.describe().to_string()}"
    except Exception as e:
        return f"Error: {e}"
