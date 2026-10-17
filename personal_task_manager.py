# Author: Ebony Cornett
# Date: October 13, 2026
# Assignment: Week 7 - Personal Task and Project Manager
# Level: Base
# Description: A Python program that uses SQLite
# to create, display, update, and delete tasks.

import sqlite3

DATABASE = "tasks.db"

def create_database():
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS tasks (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            description TEXT,
            due_date TEXT,
            status TEXT DEFAULT 'Pending'
        )
    """)

    conn.commit()
    conn.close()

def add_task(title, description, due_date, status="Pending"):
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO tasks (title, description, due_date, status)
        VALUES (?, ?, ?, ?)
    """, (title, description, due_date, status))

    conn.commit()
    conn.close()

    print("Task added successfully!")

def display_tasks():
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM tasks")
    tasks = cursor.fetchall()

    if not tasks:
        print("No tasks found.")
    else:
        for task in tasks:
            print(f"ID: {task[0]}")
            print(f"Title: {task[1]}")
            print(f"Description: {task[2]}")
            print(f"Due Date: {task[3]}")
            print(f"Status: {task[4]}")
            print("-" * 30)

    conn.close()

def filter_tasks():
    status = input("Enter status (Pending or Completed): ")

    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()

    cursor.execute(
        "SELECT * FROM tasks WHERE status = ?",
        (status,)
    )

    tasks = cursor.fetchall()

    if not tasks:
        print("No tasks found with that status.")
    else:
        for task in tasks:
            print(f"ID: {task[0]}")
            print(f"Title: {task[1]}")
            print(f"Description: {task[2]}")
            print(f"Due Date: {task[3]}")
            print(f"Status: {task[4]}")
            print("-" * 30)

    conn.close()

def update_task():
    task_id = input("Enter the task ID to update: ")
    new_status = input("Enter new status (Pending or Completed): ")

    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()

    cursor.execute("""
        UPDATE tasks
        SET status = ?
        WHERE id = ?
    """, (new_status, task_id))

    conn.commit()

    if cursor.rowcount > 0:
        print("Task updated successfully!")
    else:
        print("Task not found.")

    conn.close()

def delete_task():
    task_id = input("Enter the task ID to delete: ")

    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()

    cursor.execute(
        "DELETE FROM tasks WHERE id = ?",
        (task_id,)
    )

    conn.commit()

    if cursor.rowcount > 0:
        print("Task deleted successfully!")
    else:
        print("Task not found.")

    conn.close()

def main():
    create_database()

    while True:
        print("\nPERSONAL TASK MANAGER")
        print("1. Add Task")
        print("2. Display All Tasks")
        print("3. Filter Tasks by Status")
        print("4. Update Task")
        print("5. Delete Task")
        print("6. Exit")

        choice = input("Enter your choice (1-6): ")

        if choice == "1":
            title = input("Enter task title: ")
            description = input("Enter description: ")
            due_date = input("Enter due date (YYYY-MM-DD): ")
            add_task(title, description, due_date)

        elif choice == "2":
            display_tasks()

        elif choice == "3":
            filter_tasks()

        elif choice == "4":
            update_task()

        elif choice == "5":
            delete_task()

        elif choice == "6":
            print("Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
