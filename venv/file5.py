#DISPLAY TABLE IN WEB PAGE USING FLASK, SQLALCHEMY
from flask import Flask, request, render_template
import psycopg2
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)
DB_HOST = 'localhost'
DB_NAME = 'flask_1'
DB_USER = 'postgres'
DB_PASS = '12345'
#conn = app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:12345@localhost/flask_1'
conn = psycopg2.connect(dbname=DB_NAME, user=DB_USER, password=DB_PASS, host=DB_HOST)
#@app.route("/student_details", methods = ['POST', 'GET'])
cur = conn.cursor()
#app = Flask(__name__)
@app.route('/')
def table():
    cur.execute("SELECT * FROM student")
    student_result = cur.fetchall()
    return render_template("student_details.html", student_result=student_result)

if __name__ == '__main__':
    app.run(debug=True)
