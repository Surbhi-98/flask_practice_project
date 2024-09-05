#ESTABLISH ONE TO MANY RELATIONSHIP AFTER CREATING MODEL BASE AS WELL AS WITH DB.MODELs
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column,  ForeignKey, Table
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
class Parent(base):
    __tablename__ = 'parent'
    Id = Column(Integer(), primary_key=True)
    Name = Column(String(50))
    #below the name "Child" associated with relationship is name of class "Child".
    #we also use backref instead of back_populate one to one relationship but at that time we don't need to define relationship in second class because it already create a back refference for second class.
          #childs = relationship('Child', backref = "parent", uselist = False)
    childs = relationship('Child', back_populates = "parents")
class Child(base):
    __tablename__ = 'child'
    Child_Id = Column(Integer(), primary_key=True)
    Name = Column(String(50))
    Parent_Id = Column(Integer(), ForeignKey("parent.Id"))
    #Above the name "parent" associated with ForeignKey is name of table "parent" in database.
    #below the name "Parent" associated with relationship is name of class "Parent".
    parents = relationship('Parent', back_populates = "childs")
