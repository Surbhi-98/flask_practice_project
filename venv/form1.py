from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
import psycopg2
import psycopg2.extras
from werkzeug.security import generate_password_hash, check_password_hash
from flask_wtf import FlaskForm
from wtforms_sqlalchemy.fields import QuerySelectField
from sqlalchemy import Column, ForeignKey, Table
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.types import Integer, Text, String, DateTime, Unicode
from sqlalchemy.orm import relationship, sessionmaker, Session
app = Flask(__name__)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
app.config['SECRET_KEY'] = 'secret'
engine = create_engine('postgresql://postgres:12345@localhost:5432/FORM', echo = False)
Session = sessionmaker(bind=engine)
session = Session()
User = Country = declarative_base()

class Userclass(User):
    __tablename__ = 'user'
    Id = Column(Integer(), primary_key=True)
    Name = Column(String(80), nullable=False)
    Email = Column(String(80), nullable=False)
    Phone = Column(String(255), nullable=False)
    Gender = Column(String(80), nullable=False)
    Country_Name = Column(String(80), ForeignKey("country.Country_Name"))
    Password = Column(String(128), nullable=False)

    count = relationship("Countryclass", backref = "countries")
    def __init__(self, Name, Email, Phone, Gender, Country_Name, Password):
            #self.id = id
        self.Name = Name
        self.Email = Email
        self.Phone = Phone
        self.Gender = Gender
        self.Country_Name = Country_Name
        self.Password = Password

    def __repr__(self):
        return '<Userclass {}>'.format(self.Country_Name)

class Countryclass(Country):
    __tablename__ = 'country'
    #Id = Column(Integer(), primary_key=True)
    Country_Name = Column(String(80), primary_key=True)

    def __init__(self, Country_Name):
        #self.id = id
        self.Country_Name = Country_Name

#User.metadata.create_all(engine)
#Country.metadata.create_all(engine)
def choice_query():
    return Userclass.query()
class choiceform(FlaskForm):
    opts = QuerySelectField(query_factory=choice_query, allow_blank=True, get_label='Country_Name')

@app.route('/')
def forms():
    #form = ''
    form = choiceform()
    return render_template("Registrationform.html", form = form)
#    return render_template('Registrationform.html')

@app.route('/register', methods=['GET', 'POST'])
#def forms():
#    form = choiceform()
#    return render_template("Registrationform.html", form=form)

def submit():
    error = ''
    if request.method == 'POST':
        Name = request.form['Name']
        Email = request.form['Email']
        Phone = request.form['Phone']
        Gender = request.form['Gender']
        Country_Name = request.form['Country_Name']
        Password = request.form['Password']
        confirm_password = request.form['confirm_password']

        user_details = User_class.session.query.filter_by(Email = Email).first()
        if user_details:
            error = "SOMEONE ELSE HAS TAKES THIS EMAIL ADDRESS"

        elif Password == confirm_password:
            user_details = Userclass(Name, Email, Phone, Gender, Country_Name, generate_password_hash(Password))
            session.add(user_details)
            session.commit()

    return render_template("Registrationform.html", error = error)
#@app.route('/register')
#def input():
    #country_result = db.execute("SELECT * FROM country")
#    Form = choiseform()
#    return render_template("Registrationform.html", Form = Form)

#form.country.choices[(country.name) for country in Countryclass.query.all()]
#DB_HOST = 'localhost'
#DB_NAME = 'flask_1'
#DB_USER = 'postgres'
#DB_PASS = '12345'
#conn = psycopg2.connect(dbname=DB_NAME, user=DB_USER, password=DB_PASS, host=DB_HOST)
#cur = conn.cursor()
#@app.route("/register", methods = ['GET', 'POST'])
#def table():
#    cur.execute("SELECT * FROM country")
#    country_result = cur.fetchall()
#    return render_template("Registrationform.html", country_result = country_result)

if __name__ == '__main__':
   app.run(debug=True)
