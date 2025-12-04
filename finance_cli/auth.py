
from database import get_connection

def register(username, password):
    conn = get_connection()
    try:
        conn.execute("INSERT INTO users(username,password) VALUES(?,?)",
                     (username,password))
        conn.commit()
        return True
    except:
        return False

def login(username, password):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("SELECT id FROM users WHERE username=? AND password=?",
                (username,password))
    row = cur.fetchone()
    return row[0] if row else None
