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
association_table = Table('association', base.metadata,
    Column('Team_Id', Integer(), ForeignKey('team.Team_Id')),
    Column('Player_Id', Integer(), ForeignKey('player.Player_Id')),
)
class Player(base):
    __tablename__ = 'player'
    Player_Id = Column(Integer(), primary_key=True)
    First_Name = Column(String(80), nullable=False)
    Last_Name = Column(String(80), nullable=False)
    Position = Column(String(80), nullable=False)
    #below the name "Team" associated with relationship is name of class "Team".
    Players = relationship('Team', secondary = association_table, backref = 'team_players', lazy = 'dynamic')

    #def __repr__(self):
        #return '<person %r>' % (self.Person_Name)
class Team(base):
    __tablename__ = 'team'
    Team_Id = Column(Integer(), primary_key=True)
    Team_Name = Column(String(80), nullable=False)
    City = Column(String(80), nullable=False)

#base.metadata.create_all(engine)


#********************MANY TO MANY RELATIONSHIP WITH db.model MODEL*********************

#from flask import Flask
#from flask_sqlalchemy import SQLAlchemy
#from sqlalchemy.orm import relationship
#app = Flask(__name__)
#app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:12345@localhost/Relationship'
#app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
#db = SQLAlchemy(app)
#association_table = db.Table('association',
#    db.Column('Team_Id', db.Integer(), db.ForeignKey('team.Team_Id')),
#    db.Column('Player_Id', db.Integer(), db.ForeignKey('player.Player_Id'))
#)
#class Player(db.Model):
#    __tablename__ = 'player'
#    Player_Id = db.Column(db.Integer(), primary_key=True)
#    First_Name = db.Column(db.String(80), nullable=False)
#    Last_Name = db.Column(db.String(80), nullable=False)
#    Position = db.Column(db.String(80), nullable=False)
    #below the name "Team" associated with relationship is name of class "Team".
#    Players = db.relationship('Team', secondary= association_table, backref = 'team_players')

    #def __repr__(self):
        #return '<person %r>' % (self.Person_Name)
#class Team(db.Model):
#    __tablename__ = 'team'
#    Team_Id = db.Column(db.Integer(), primary_key=True)
#    Team_Name = db.Column(db.String(80), nullable=False)
#    City = db.Column(db.String(80), nullable=False)
