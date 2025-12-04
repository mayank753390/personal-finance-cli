
from database import get_connection
from datetime import datetime

def add_transaction(user_id, t_type, category, amount):
    conn = get_connection()
    conn.execute(
        "INSERT INTO transactions(user_id,type,category,amount,date) VALUES(?,?,?,?,?)",
        (user_id, t_type, category, amount, datetime.now().strftime('%Y-%m-%d'))
    )
    conn.commit()

def update_transaction(tid, amount):
    conn = get_connection()
    conn.execute("UPDATE transactions SET amount=? WHERE id=?", (amount, tid))
    conn.commit()

def delete_transaction(tid):
    conn = get_connection()
    conn.execute("DELETE FROM transactions WHERE id=?", (tid,))
    conn.commit()

def list_transactions(user_id):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("SELECT * FROM transactions WHERE user_id=?", (user_id,))
    return cur.fetchall()
