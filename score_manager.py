import sqlite3

class ScoreManager:
    def __init__(self, db_name="scores.db"):
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()
        self.create_table()

    def create_table(self):
        self.cursor.execute(
            "CREATE TABLE IF NOT EXISTS scores (id INTEGER PRIMARY KEY, name TEXT, score INTEGER, time REAL)"
        )
        self.conn.commit()

    def add_score(self, name, score, time):
        self.cursor.execute("INSERT INTO scores (name, score, time) VALUES (?, ?, ?)", (name, score, time))
        self.conn.commit()

    def get_scores(self):
        self.cursor.execute("SELECT * FROM scores ORDER BY score DESC, time ASC")
        return self.cursor.fetchall()
