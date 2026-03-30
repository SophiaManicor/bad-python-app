import sqlite3

# --- Hello World ---
print("Hello, World!")

# --- Setup: create an in-memory database with a users table ---
conn = sqlite3.connect(":memory:")
cursor = conn.cursor()
cursor.execute("CREATE TABLE users (id INTEGER PRIMARY KEY, username TEXT, password TEXT)")
cursor.execute("INSERT INTO users VALUES (1, 'alice', 'secret123')")
cursor.execute("INSERT INTO users VALUES (2, 'bob', 'hunter2')")
conn.commit()

# --- VULNERABLE function: directly interpolates user input into SQL ---
def get_user(username):
    query = "SELECT * FROM users WHERE username = '" + username + "'"
    print(f"Running query: {query}")
    cursor.execute(query)
    return cursor.fetchall()

# Normal usage
print("\n[Normal] Looking up 'alice':")
print(get_user("alice"))

# SQL Injection example — input crafted to dump ALL users
print("\n[Injected] Input: \" ' OR '1'='1 \"")
print(get_user("' OR '1'='1"))

conn.close()
