import sqlite3
from db import db

class ItemModel(db.Model):   #extend
    #telling sqlachemy table and column infos
    __tablename__="items"
    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(80))
    price = db.Column(db.Float(precision=2))
    store_id = db.Column(db.Integer, db.ForeignKey('stores.id'))
    store = db.relationship('StoreModel')

    def __init__(self, name, price, store_id):
        self.name = name
        self.price = price
        self.store_id = store_id

    def json(self):
        return {'name':self.name, 'price':self.price}

    #find_by_name remains a classmethod while insert and update methods don't
    #because what find_by_name returns is the class object(ItemModel) itself?
    @classmethod
    def find_by_name(cls,name):
        return cls.query.filter_by(name=name).first()
        #connection=sqlite3.connect('data.db')
        #cursor=connection.cursor()
        #query='select * from items where name=?'
        #result=cursor.execute(query,(name,))
        #2nd parameter of execute() should be the type of tuple
        #row=result.fetchone()
        #connection.close()
        #if row:
        #    return cls(*row)
        #returns the object of ItemModel
        #simplifed from cls(row[0],row[1]) (argument unpacking)

    # insert was a classmethod
    def save_to_db(self):
        db.session.add(self)
        db.session.commit()
        #connection=sqlite3.connect('data.db')
        #cursor=connection.cursor()
        #query='insert into items values (?,?)'
        #cursor.execute(query, (self.name, self.price))
        #connection.commit()
        #connection.close()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()
        #connection=sqlite3.connect('data.db')
        #cursor=connection.cursor()
        #query='update items set price=? where name=?'
        #cursor.execute(query, (self.price, self.name))
        #connection.commit()
        #connection.close()
