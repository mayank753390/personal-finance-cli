
from database import get_connection

def set_budget(user_id, category, limit):
    conn = get_connection()
    conn.execute(
        "INSERT OR REPLACE INTO budgets(user_id,category,monthly_limit) VALUES(?,?,?)",
        (user_id, category, limit)
    )
    conn.commit()

def check_budget(user_id, category):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("SELECT monthly_limit FROM budgets WHERE user_id=? AND category=?",
                (user_id,category))
    row = cur.fetchone()
    if not row: return None

    limit=row[0]
    cur.execute(
        "SELECT SUM(amount) FROM transactions WHERE user_id=? AND category=? AND type='expense'",
        (user_id,category)
    )
    spent = cur.fetchone()[0] or 0
    return spent, limit
