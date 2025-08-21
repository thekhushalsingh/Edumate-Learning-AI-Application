import sqlite3

DB_NAME = "edumate.db"

def init_db():
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS users (
                    user_id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT,
                    goals TEXT,
                    learning_style TEXT
                 )''')
    c.execute('''CREATE TABLE IF NOT EXISTS progress (
                    user_id INTEGER,
                    topic TEXT,
                    score INTEGER,
                    timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
                 )''')
    conn.commit()
    conn.close()

def add_user(name, goals, learning_style):
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    c.execute("INSERT INTO users (name, goals, learning_style) VALUES (?, ?, ?)", (name, goals, learning_style))
    conn.commit()
    conn.close()

def log_progress(user_id, topic, score):
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    c.execute("INSERT INTO progress (user_id, topic, score) VALUES (?, ?, ?)", (user_id, topic, score))
    conn.commit()
    conn.close()

def get_progress(user_id):
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    c.execute("SELECT topic, score, timestamp FROM progress WHERE user_id=?", (user_id,))
    data = c.fetchall()
    conn.close()
    return data