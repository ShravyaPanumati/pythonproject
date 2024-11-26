import os
from flask import Flask, request, jsonify, render_template
import pyodbc

app = Flask(__name__)


# Database connection function (SQL Server example)
def connect_db():
    server = '34.42.71.28'  # Replace with your server address
    database = 'myappdb'  # Replace with your database name
    username = 'myuser'  # Replace with your username
    password = 'Shravya123'  # Replace with your password
    driver = '{ODBC Driver 17 for SQL Server}'  # ODBC driver for SQL Server

    connection = pyodbc.connect(
        f'DRIVER={driver};SERVER={server};DATABASE={database};UID={username};PWD={password}'
    )
    return connection


# Function to create table if it doesn't exist
def create_values_table():
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute('''
    IF NOT EXISTS (SELECT * FROM sysobjects WHERE name='values_table' and xtype='U')
    CREATE TABLE values_table (
        id INT PRIMARY KEY IDENTITY(1,1),
        value1 NVARCHAR(50) NOT NULL,
        value2 NVARCHAR(50) NOT NULL
    );
    ''')
    conn.commit()
    cursor.close()
    conn.close()


# Route to insert values into the database
@app.route('/insert', methods=['POST'])
def insert_values():
    data = request.json
    value1 = data.get('value1')
    value2 = data.get('value2')

    # Validate the input
    if not value1 or not value2:
        return jsonify({'error': 'Invalid data'}), 400

    conn = connect_db()
    cursor = conn.cursor()
    insert_values_query = 'INSERT INTO values_table (value1, value2) VALUES (?, ?)'
    cursor.execute(insert_values_query, (value1, value2))
    conn.commit()

    cursor.close()
    conn.close()

    return jsonify({'message': 'Values are inserted successfully'}), 200

@app.route('/')
def index():
    return render_template('index.html')

# Main block
if __name__ == '__main__':
    create_values_table()  # Ensure the table exists when the app starts
    app.run(host='0.0.0.0', port=5000, debug=True)
