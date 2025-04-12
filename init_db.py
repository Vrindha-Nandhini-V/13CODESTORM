# init_db.py

import sqlite3

# Connect to DB (or create if not exists)
conn = sqlite3.connect("retail_issues.db")
cursor = conn.cursor()

# List of category tables
categories = ['billing', 'promotion', 'technical', 'returns', 'delivery', 'accounts', 'feedback', 'general']

# Create a table for each category
for category in categories:
    cursor.execute(f'''
        CREATE TABLE IF NOT EXISTS {category} (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT NOT NULL,
            issue TEXT NOT NULL
        )
    ''')

conn.commit()
conn.close()

print("✅ Database and tables created!")
