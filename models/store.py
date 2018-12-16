import sqlite3
from db import db

class StoreModel(db.Model):   #extend
    #telling sqlachemy table and column infos
    __tablename__="stores"
    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(80))
    items = db.relationship('ItemModel' , lazy = 'dynamic')
              #without lazy = 'dynamic', this is a list of items
              #with  lazy = 'dynamic', this is not a list of items

    def __init__(self , name):
        self.name=name

    def json(self):
        return {'name':self.name, 'items':[item.json() for item in self.items.all()]}
        #without lazy = 'dynamic', use self.items at the last
        #with  lazy = 'dynamic', use self.items.all() at the last

    @classmethod
    def find_by_name(cls,name):
        return cls.query.filter_by(name=name).first()

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()


    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()
