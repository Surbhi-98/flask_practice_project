#CREATING OF MODEL USING SQLALCHEMY
from sqlalchemy import Column
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.types import Integer, Text, String, DateTime
engine = create_engine('postgresql://postgres:12345@localhost:5432/flask_1')
base = declarative_base()
class teacher(base):
    __tablename__ = 'teacher'
    Id = Column(Integer(), primary_key=True)
    First_name = Column(String(80), nullable=False)
    Last_name = Column(String(80), nullable=False)
    DOB = Column(DateTime(), nullable = False)
    Email = Column(String(120), nullable = False)

    #def __init__(self, First_name, Last_name, DOB,  Email):
        #self.id = id
        #self.First_name = First_name
        #self.Last_name = Last_name
        #self.DOB = DOB
        #self.Email = Email

    #def __repr__(self):
        #return '<teacher %r>' % (self.First_name, self.Last_name, self.Email)

base.metadata.create_all(engine)
