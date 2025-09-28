import sqlite3

DB_PATH = "database/medical.db"

def get_all_symptoms():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("SELECT name FROM symptoms")
    rows = cursor.fetchall()
    conn.close()
    return [r[0] for r in rows]

def get_all_conditions():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("SELECT name FROM conditions")
    rows = cursor.fetchall()
    conn.close()
    return [r[0] for r in rows]
