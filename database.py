import sqlite3
from datetime import datetime

conn = sqlite3.connect("tenant.db", check_same_thread=False)
cursor = conn.cursor()

def create_tables():
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS complaints (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        issue TEXT,
        status TEXT,
        created_at TEXT
    )
    """)
    conn.commit()

def add_complaint(issue):
    cursor.execute("""
    INSERT INTO complaints (issue, status, created_at)
    VALUES (?, ?, ?)
    """, (issue, "Open", datetime.now().strftime("%Y-%m-%d %H:%M")))
    conn.commit()

def get_complaints():
    cursor.execute("SELECT * FROM complaints")
    return cursor.fetchall()
