from flask import Flask, request, jsonify,redirect
from flask_cors import CORS
import sqlite3

from db import init_db
from utils import generate_short_code

app = Flask(__name__)
CORS(app)

init_db()


@app.route("/shorten", methods=["POST"])
def shorten_url():
    data = request.get_json()
    long_url = data.get("long_url")

    if not long_url:
        return jsonify({"error": "URL is required"}), 400

    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()

    # 🔍 STEP 1: CHECK IF URL ALREADY EXISTS
    cursor.execute(
        "SELECT short_code FROM urls WHERE long_url = ?",
        (long_url,)
    )

    existing = cursor.fetchone()

    if existing:
        conn.close()
        return jsonify({
            "short_url": f"http://127.0.0.1:5000/{existing[0]}",
            "message": "Already exists"
        })


    short_code = generate_short_code()

    cursor.execute(
        "INSERT INTO urls (long_url, short_code) VALUES (?, ?)",
        (long_url, short_code)
    )

    conn.commit()
    conn.close()

    return jsonify({
        "short_url": f"http://127.0.0.1:5000/{short_code}",
        "message": "New URL created"
    })

@app.route("/<short_code>")
def redirect_url(short_code):
    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()

    cursor.execute(
        "SELECT long_url FROM urls WHERE short_code = ?",
        (short_code,)
    )

    result = cursor.fetchone()
    conn.close()

    if result:
        return redirect(result[0])   # 🔥 THIS IS THE FIX
    else:
        return "URL not found", 404
@app.route("/debug")
def debug():
    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()

    cursor.execute("SELECT id, long_url, short_code FROM urls")
    rows = cursor.fetchall()

    conn.close()

    results = []

    for row in rows:
        results.append({
            "id": row[0],
            "long_url": row[1],
            "short_code": row[2],
            "short_url": f"http://127.0.0.1:5000/{row[2]}"
        })

    return jsonify(results)

if __name__ == "__main__":
    app.run(debug=True)