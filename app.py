from flask import Flask, render_template, request
import sqlite3

app = Flask(__name__)

# create database
def init_db():
    conn = sqlite3.connect('database.db')
    conn.execute('CREATE TABLE IF NOT EXISTS attendance (name TEXT, status TEXT)')
    conn.close()

init_db()

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/submit', methods=['POST'])
def submit():
    name = request.form['name']
    status = request.form['status']

    conn = sqlite3.connect('database.db')
    conn.execute("INSERT INTO attendance (name,status) VALUES (?,?)",(name,status))
    conn.commit()
    conn.close()

    return "Attendance Recorded Successfully"

@app.route('/view')
def view():
    conn = sqlite3.connect('database.db')
    data = conn.execute("SELECT * FROM attendance").fetchall()
    conn.close()

    return render_template("attendance.html", data=data)

if __name__ == '__main__':
    app.run(debug=True)