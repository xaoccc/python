# install flask, psycopg2-binary, Flask-CORS
from flask import Flask, jsonify, request
import psycopg2
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# Setup database
def get_db_connection():
    conn = psycopg2.connect(
        host="127.0.0.1",
        database="xpenses_db",
        user="postgres",
        password="postgres"
    )
    return conn

# Add post method path and logic
@app.route('/add_data', methods=['POST'])
def add_data():
    data = request.json
    type = data["type"]
    amount = data["amount"]
    date = data["date"]

    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO expenses (type, amount, date) VALUES (%s, %s, %s)", (type, amount, date))
    conn.commit()
    cursor.close()
    conn.close()

    return jsonify({"status": "success"}), 200

# Add get method path and logic
@app.route('/get_data', methods=['GET'])
def get_data():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT type, amount, date FROM expenses")

    rows = cursor.fetchall()
    cursor.close()
    conn.close()

    data = [{'type': row[0], 'amount': row[1], 'date': row[2]} for row in rows]

    return jsonify(data), 200


if __name__ == '__main__':
    app.run(debug=True)
