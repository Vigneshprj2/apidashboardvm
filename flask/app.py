from flask import Flask, request, jsonify
from flask_cors import CORS
import sqlite3
from datetime import datetime

app = Flask(__name__)
CORS(app)

# here im mentioning the database Sqllite3 - vm 
def init_db():
    with sqlite3.connect('api_hits.db') as conn:
        c = conn.cursor()
        c.execute('''DROP TABLE IF EXISTS api_hits''')
        c.execute('''CREATE TABLE api_hits (
            id INTEGER PRIMARY KEY,
            name TEXT,
            email TEXT,
            address TEXT,
            mobile TEXT
        )''')
        conn.commit()

def insert_sample_data():
    sample_data = [
        {
            "name": "Vignesh",
            "email": "vignesh@gmail.com",
            "address": "Guindy , Chennai",
            "mobile": "1234567890"
        },
        {
            "name": "Mahesh",
            "email": "mahesh@example.com",
            "address": "Vadapalani , Chennai",
            "mobile": "9876543210"
        },
        {
            "name": "Yogesh",
            "email": "yogesh@example.com",
            "address": "Adambakkam , Chennai",
            "mobile": "5551234567"
        },
        {
            "name": "Manoj",
            "email": "manoj@gmail.com",
            "address": "Pallavaram , Chennai",
            "mobile": "4445678901"
        },
        {
            "name": "Monica",
            "email": "Monica@gmail.com",
            "address": "Teynampet , Chennai",
            "mobile": "2223334444"
        },{
            "name": "John ",
            "email": "john@gmail.com",
            "address": "Avadi ,Chennai",
            "mobile": "1234567890"
        },
        {
            "name": "Dylan",
            "email": "Dylan@gmail.com",
            "address": "Nungambakkam , Chennai",
            "mobile": "9876543210"
        },
        {
            "name": "Alice Johnson",
            "email": "alicejohnson@gmail.com",
            "address": "Velachery , Chennai",
            "mobile": "5551234567"
        },
        {
            "name": "Pooja",
            "email": "pooja@gmail.com",
            "address": "Mylapore , Chennai",
            "mobile": "4445678901"
        },
        {
            "name": "Catherine",
            "email": "catherine@example.com",
            "address": "Chrompet, Chennai",
            "mobile": "2223334444"
        }
    ]

    with sqlite3.connect('api_hits.db') as conn:
        c = conn.cursor()
        for data in sample_data:
            c.execute('''INSERT INTO api_hits (name, email, address, mobile) 
                         VALUES (?, ?, ?, ?)''',
                      (data['name'], data['email'], data['address'], data['mobile']))
        conn.commit()

init_db()

@app.route('/track', methods=['POST'])
def track_api_hit():
    name = request.json.get('name')
    email = request.json.get('email')
    address = request.json.get('address')
    mobile = request.json.get('mobile')

    with sqlite3.connect('api_hits.db') as conn:
        c = conn.cursor()
        c.execute('''INSERT INTO api_hits (name, email, address, mobile) 
                     VALUES (?, ?, ?, ?)''',
                  (name, email, address, mobile))
        conn.commit()

    return jsonify({'message': 'Data saved successfully'})


@app.route('/api-hits', methods=['GET'])
def get_api_hits():
    with sqlite3.connect('api_hits.db') as conn:
        c = conn.cursor()
        c.execute('SELECT * FROM api_hits')
        rows = c.fetchall()

    hits = [{'id': row[0], 'name': row[1], 'email': row[2], 'address': row[3], 'mobile': row[4]} for row in rows]
    return jsonify(hits)

if __name__ == '__main__':
    insert_sample_data()  # Call this once to insert sample data, then comment it out after running once
    app.run(debug=True)
