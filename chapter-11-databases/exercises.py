# Chapter 11 - Exercise Solutions
import sqlite3

# 1. Extended task manager with priorities
def create_tables(cursor):
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS tasks (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            priority TEXT DEFAULT 'medium',
            status TEXT DEFAULT 'pending',
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    """)

def add_task(cursor, title, priority="medium"):
    cursor.execute("INSERT INTO tasks (title, priority) VALUES (?, ?)", (title, priority))

def get_tasks_by_priority(cursor, priority):
    cursor.execute("SELECT * FROM tasks WHERE priority = ? ORDER BY created_at", (priority,))
    return cursor.fetchall()

# Demo
conn = sqlite3.connect(":memory:")
cur = conn.cursor()
create_tables(cur)
add_task(cur, "Fix login bug", "high")
add_task(cur, "Update docs", "low")
add_task(cur, "Deploy v2", "high")

high = get_tasks_by_priority(cur, "high")
print("High priority tasks:")
for task in high:
    print(f"  {task[1]} (status: {task[3]})")

conn.close()
