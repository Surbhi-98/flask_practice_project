#ESTABLISH ONE TO MANY RELATIONSHIP AFTER CREATING MODEL BASE AS WELL AS WITH DB.MODELs
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column,  ForeignKey
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.types import Integer, Text, String, DateTime
from sqlalchemy.orm import relationship, sessionmaker, Session
app = Flask(__name__)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
engine = create_engine('postgresql://postgres:12345@localhost:5432/Relationship')
Session = sessionmaker(bind=engine)
session = Session()
base = declarative_base()
class person(base):
    __tablename__ = 'person'
    Id = Column(Integer(), primary_key=True)
    Person_Name = Column(String(80), nullable=False)
    #below the name "pet" associated with relationship is name of class "pet".
    pets = relationship("pet", backref = "Owner")

    #def __repr__(self):
        #return '<person %r>' % (self.Person_Name)
class pet(base):
    __tablename__ = 'pet'
    Id = Column(Integer(), primary_key=True)
    Pet_Name = Column(String(80), nullable=False)
    Owner_Id = Column(Integer(), ForeignKey("person.Id"))
    #Above the name "person" associated with ForeignKey is name of table "person" in database.

#base.metadata.create_all(engine)




#**************ONE TO MANY RELATIONSHIP WITH db.model MODEL*********************
#app = Flask(__name__)
#app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:12345@localhost/Relationship'
#app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
#db = SQLAlchemy(app)
#class person(db.Model):
    #__tablename__ = 'person'
    #Id = db.Column(db.Integer(), primary_key=True)
    #Person_Name = db.Column(db.String(80), nullable=False)
    #below the name "pet" associated with relationship is name of class "pet".
    #pets = db.relationship("pet", backref = "Owner")

    #def __repr__(self):
        #return '<person %r>' % (self.Person_Name)
#class pet(db.Model):
    #__tablename__ = 'pet'
    #Id = db.Column(db.Integer(), primary_key=True)
    #Pet_Name = db.Column(db.String(80), nullable=False)
    #Owner_Id = db.Column(db.Integer(), db.ForeignKey("person.Id"))
    #Above the name "person" associated with ForeignKey is name of table "person" in database.
