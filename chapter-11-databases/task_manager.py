# Task Manager with SQLite - Chapter 11 Project

import sqlite3
from datetime import datetime


def setup_database():
    """Create database and tasks table if they don't exist"""
    conn = sqlite3.connect("tasks.db")
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS tasks (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            status TEXT DEFAULT 'pending',
            created TEXT NOT NULL
        )
    """)
    conn.commit()
    return conn


def add_task(conn):
    """Add a new task"""
    title = input("Task title: ").strip()
    if not title:
        print("Title cannot be empty.")
        return
    cursor = conn.cursor()
    created = datetime.now().strftime("%Y-%m-%d %H:%M")
    cursor.execute("INSERT INTO tasks (title, created) VALUES (?, ?)", (title, created))
    conn.commit()
    print(f"Added: {title}")


def view_tasks(conn, status=None):
    """View tasks, optionally filtered by status"""
    cursor = conn.cursor()
    if status:
        cursor.execute("SELECT id, title, status, created FROM tasks WHERE status = ? ORDER BY created DESC", (status,))
    else:
        cursor.execute("SELECT id, title, status, created FROM tasks ORDER BY created DESC")
    
    rows = cursor.fetchall()
    if not rows:
        print("No tasks found.")
        return

    print(f"\n{'ID':<5} {'Title':<30} {'Status':<12} {'Created'}")
    print("-" * 65)
    for row in rows:
        print(f"{row[0]:<5} {row[1]:<30} {row[2]:<12} {row[3]}")


def complete_task(conn):
    """Mark a task as complete"""
    try:
        task_id = int(input("Task ID to complete: "))
    except ValueError:
        print("Invalid ID.")
        return
    cursor = conn.cursor()
    cursor.execute("UPDATE tasks SET status = 'done' WHERE id = ?", (task_id,))
    conn.commit()
    if cursor.rowcount > 0:
        print(f"Task {task_id} marked as done.")
    else:
        print(f"Task {task_id} not found.")


def delete_task(conn):
    """Delete a task"""
    try:
        task_id = int(input("Task ID to delete: "))
    except ValueError:
        print("Invalid ID.")
        return
    cursor = conn.cursor()
    cursor.execute("DELETE FROM tasks WHERE id = ?", (task_id,))
    conn.commit()
    if cursor.rowcount > 0:
        print(f"Task {task_id} deleted.")
    else:
        print(f"Task {task_id} not found.")


def show_stats(conn):
    """Show task statistics"""
    cursor = conn.cursor()
    cursor.execute("SELECT status, COUNT(*) FROM tasks GROUP BY status")
    rows = cursor.fetchall()
    total = sum(count for _, count in rows)
    print(f"\n  Total tasks: {total}")
    for status, count in rows:
        print(f"  {status}: {count}")


# Main program
conn = setup_database()

print("=" * 40)
print("  TASK MANAGER")
print("=" * 40)

while True:
    print("\n1. Add Task")
    print("2. View All Tasks")
    print("3. View Pending")
    print("4. Complete Task")
    print("5. Delete Task")
    print("6. Statistics")
    print("7. Exit")

    choice = input("\nChoice: ")

    if choice == "1":
        add_task(conn)
    elif choice == "2":
        view_tasks(conn)
    elif choice == "3":
        view_tasks(conn, "pending")
    elif choice == "4":
        complete_task(conn)
    elif choice == "5":
        delete_task(conn)
    elif choice == "6":
        show_stats(conn)
    elif choice == "7":
        conn.close()
        print("Tasks saved. Goodbye!")
        break
