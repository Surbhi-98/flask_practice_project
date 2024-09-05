from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
#import psycopg2
#import psycopg2.extras
#from werkzeug.security import generate_password_hash, check_password_hash
from sqlalchemy import Column, ForeignKey, Table
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.types import Integer, Text, String, DateTime, Unicode
from sqlalchemy.orm import relationship, sessionmaker, Session
app = Flask(__name__)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
engine = create_engine('postgresql://postgres:12345@localhost:5432/FORM', echo = False)
Session = sessionmaker(bind=engine)
session = Session()
User = Country = declarative_base()

class Userclass(User):
    __tablename__ = 'user'
    Id = Column(Integer(), primary_key=True)
    Name = Column(String(80), nullable=False)
    Email = Column(String(80), nullable=False)
    Phone = Column(Unicode(50), nullable=False)
    Gender = Column(String(80), nullable=False)
    Country_Id = Column(Integer(), ForeignKey("country.Id"))
    Password = Column(String(128), nullable=False)

    count = relationship("Countryclass", backref = "countries")
    def __init__(self, Name, Email, Phone, Gender, Country_Id, Password):
            #self.id = id
        self.Name = Name
        self.Email = Email
        self.Phone = Phone
        self.Gender = Gender
        self.Country_Id = Country_Id
        self.Password = Password

class Countryclass(Country):
    __tablename__ = 'country'
    Id = Column(Integer(), primary_key=True)
    Country_Name = Column(String(80), nullable=False)

    def __init__(self, Country_Name):
        #self.id = id
        self.Country_Name = Country_Name

#User.metadata.create_all(engine)
#Country.metadata.create_all(engine)

#@app.route('/')
#def form():
#    return render_template('Registrationform.html')

#@app.route('/register', methods=['GET', 'POST'])
#def submit():
    #error = ''
#    if request.method == 'POST':
#        Name = request.form['Name']
#        Email = request.form['Email']
#        Phone = request.form['Phone']
#        Gender = request.form['Gender']
#        Country_Id = request.form['Country_Id']
#        Password = request.form['Password']
#        confirm_password = request.form['confirm_password']

        #user_details = User_class.session.query.filter_by(Email = Email).first()
        #if user_details:
            #error = "SOMEONE ELSE HAS TAKES THIS EMAIL ADDRESS"

#        if Password == confirm_password:

#            user_details = User_class(Name, Email, Phone, Gender, Country, generate_password_hash(Password))

#            session.add(user_details)
#           session.commit()
 #   return render_template("Registrationform.html")

#f __name__ == '__main__':
#   app.run(debug=True)

#Country.metadata.create_all(engine1)
