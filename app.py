from flask import Flask, render_template, request, jsonify
import sqlite3
from datetime import datetime

app = Flask(__name__)
DB_NAME = "survey.db"

def init_db():
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    c.execute("""
        CREATE TABLE IF NOT EXISTS responses (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            routine TEXT,
            busy_meal TEXT,
            frustration TEXT,
            quick_cook TEXT,
            priority TEXT,
            price TEXT,
            format_trust TEXT,
            qr_recipe TEXT,
            eco_priority TEXT,
            intent TEXT,
            meal_choice TEXT,
            created_at TEXT
        )
    """)
    conn.commit()
    conn.close()

@app.route("/")
def survey():
    return render_template("survey.html")

@app.route("/submit", methods=["POST"])
def submit():
    data = request.json

    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    c.execute("""
        INSERT INTO responses VALUES (NULL,?,?,?,?,?,?,?,?,?,?,?)
    """, (
        data["routine"],
        data["busy_meal"],
        data["frustration"],
        data["quick_cook"],
        data["priority"],
        data["price"],
        data["format_trust"],
        data["qr_recipe"],
        data["eco_priority"],
        data["intent"],
        data["meal_choice"],
        datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    ))
    conn.commit()
    conn.close()

    return jsonify({"status": "ok"})


if __name__ == "__main__":
    init_db()
    app.run(host="0.0.0.0", port=10000)
