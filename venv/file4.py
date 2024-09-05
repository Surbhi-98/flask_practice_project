#REGISTRATION FORM WITH FLASK, SQLALCHEMY, POSTGRESQL CONNECTION AND _hashed_password
from flask import Flask, render_template, request
#from flask_wtf import FlaskFor
from flask_sqlalchemy import SQLAlchemy
import psycopg2
#from file5 import table
import psycopg2.extras
import re
from werkzeug.security import generate_password_hash, check_password_hash
#from wtforms.validators import (DataRequired, Email, EqualTo, Length, Optional)
app = Flask(__name__)
conn = app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:12345@localhost/flask_1'
db = SQLAlchemy(app)
class Student(db.Model):
    __tablename__ = 'student'
    id = db.Column(db.Integer(), primary_key=True)
    firstname = db.Column(db.String(80), nullable=False)
    lastname = db.Column(db.String(80), nullable=False)
    email = db.Column(db.String(120), nullable = False)
    username = db.Column(db.String(128), nullable = False)
    password = db.Column(db.String(128), nullable=False)
    def __init__(self, firstname, lastname, email, username, password):
            #self.id = id
        self.firstname = firstname
        self.lastname = lastname
        self.email = email
        self.username = username
        self.password = password
@app.route('/')
def index():
    #return render_template('form.html')
    return render_template('firstpage.html')

@app.route('/form')
def form():
    return render_template('form.html')

#curs = conn.cursor()
@app.route('/register', methods=['GET', 'POST'])
def submit():
    error = ''
    if request.method == 'POST':
        firstname = request.form['firstname']
        lastname = request.form['lastname']
        email = request.form['email']
        username = request.form['username']
        password = request.form['password']
        confirm_password = request.form['confirm_password']

        student_details = Student.query.filter_by(username = username).first()
        student_details1 = Student.query.filter_by(email = email).first()
        if student_details:
            error = "SOMEONE ELSE HAS TAKES THIS USERNAME!!"

        elif student_details1:
            error = "EMAIL ID IS ALREADY EXIST!!"

        elif password == confirm_password:
            student = Student(firstname, lastname, email, username, generate_password_hash(password))
            db.session.add(student)
            db.session.commit()
        #student_details = Student.query.filter_by(username = username).first()

        #_hashed_password = generate_password_hash(password)
    #curs.execute("SELECT * FROM student WHERE firstname = %s and lastname = %s", (firstname, lastname))
    #student_details = curs.fetchone()
    #print(student_details)
    #if student_details:
    #    flash("ACCOUNT ALREADY EXIST!!")
    #elif not re.match(r'[^@]+@[^@]+\.[^@]', email):
#        flash("INVALID EMAIL ADDRESS!!")
#    elif not re.match(r'[A-Za-z0-9]+', username):
#        flash("USERNAMES MUST CONTAIN ONLY CHARACTERS AND NUMBERS!!")
    return render_template("form.html", error = error)
    #if you want to fetch a data of student registered. its ooutput is display is command line
    #if request.method == 'GET':
        #student_result = db.session.query(Student).filter(Student.id == 1)
        #for result in student_result:
            #print(result.firstname)
    #it return the new html page along with success statement and registered student name.
    #return render_template('form_sucess.html', data = firstname, data1 = lastname)
#THE BELOW CODE DISPLAY ALL THE DATA OF DATABASE/TABLE
DB_HOST = 'localhost'
DB_NAME = 'flask_1'
DB_USER = 'postgres'
DB_PASS = '12345'
conn = psycopg2.connect(dbname=DB_NAME, user=DB_USER, password=DB_PASS, host=DB_HOST)
cur = conn.cursor()
@app.route("/student_details", methods = ['GET'])
def table():
    cur.execute("SELECT * FROM student")
    student_result = cur.fetchall()
    return render_template("student_details.html", student_result=student_result)
if __name__ == '__main__':
    app.run(debug=True)
