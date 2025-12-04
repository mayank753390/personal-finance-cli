
from database import get_connection

def monthly_report(user_id, month):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("""SELECT type, SUM(amount) 
                     FROM transactions 
                     WHERE user_id=? AND substr(date,6,2)=?
                     GROUP BY type""", (user_id, month))
    return cur.fetchall()

def yearly_report(user_id, year):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("""SELECT type, SUM(amount)
                     FROM transactions
                     WHERE user_id=? AND substr(date,1,4)=?
                     GROUP BY type""", (user_id,year))
    return cur.fetchall()
