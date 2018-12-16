import sqlite3
from db import db

class UserModel(db.Model):
    #telling sqlachemy table and column infos
    __tablename__="users"
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80))
    password = db.Column(db.String(80))
    def __init__(self, username, password):
        #self.id = _id
        self.username = username
        self.password = password

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def find_by_username(cls,username): #replacing (self, username)
        return cls.query.filter_by(username = username).first()
        #connection=sqlite3.connect('data.db')
        #cursor=connection.cursor()
        #query="select * from users where username=?"
        #result=cursor.execute(query,(username,)) #2nd parameter is of type tuple
        #row=result.fetchone()
        #if row:
        #    user=cls(*row) #replacing User(row[0],row[1],row[2])
        #else:
        #    user=None
        #connection.close()
        #return user

    @classmethod
    def find_by_id(cls, _id): #replacing (self, _id)
        return cls.query.filter_by(id = _id).first()
        #connection=sqlite3.connect('data.db')
        #cursor=connection.cursor()
        #query="select * from users where id=?"
        #result=cursor.execute(query,(_id,)) #2nd parameter is of type tuple
        #row=result.fetchone()
        #if row:
        #    user=cls(*row) #replacing User(row[0],row[1],row[2])
        #else:
        #    user=None
        #connection.close()
        #return user
