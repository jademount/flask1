#from flask import Flask, request
from flask_restful import Resource, reqparse
from flask_jwt import jwt_required
from resources.user import UserRegister
from security import authenticate, identity
#import sqlite3
from models.item import ItemModel


class Item(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('price',
        type=float,
        required=True,
        help="This field cannot be left blank!"
    )

    parser.add_argument('store_id',
        type = int,
        required = True,
        help = "Every item needs a store_id"
    )

    @jwt_required()
    def get(self, name):
        item=ItemModel.find_by_name(name)
        if item:
            return item.json()
        return {"message" : "item not found"}, 404

    def post(self, name):
        if ItemModel.find_by_name(name):
            return {'message': "An item with name '{}' already exists.".format(name)}

        data = Item.parser.parse_args()

        item = ItemModel(name, **data) #data['price'], data['store_id']

        try:
            item.save_to_db()
        except:
            return {"message" : "An error occured inserting the item"}, 500 #intenal server error
        return item.json(),201

    @jwt_required()
    def delete(self, name):
        item = ItemModel.find_by_name(name)
        if item:
            item.delete_from_db()
        return {"message" : "item deleted"}
        #connection=sqlite3.connect('data.db')
        #cursor=connection.cursor()
        #query='delete from items where name=?'
        #cursor.execute(query, (name,))
        #connection.commit()
        #connection.close()
        #return {'message': 'Item deleted'}

    #@jwt_required()
    def put(self, name):
        data = Item.parser.parse_args()
        # Once again, print something not in the args to verify everything works
        item = ItemModel.find_by_name(name)
        #updated_item = ItemModel(name, data['price'])

        if item is None:
            item = ItemModel(name, **data) #data['price'], data['store_id']
            #try:
            #    updated_item.insert()
            #except:
            #    return {"message" : "an error occurred inserting the item"},500
        else:
            item.price = data['price']
            #try:
            #    updated_item.update()
            #except:
            #    return {"message" : "an error occurred updating the item"},500
        item.save_to_db()
        return item.json()


class ItemList(Resource):
    def get(self):
        return { "item" : [ x.json() for x in ItemModel.query.all()]}
               # or { "item" : list(map(lambda x : X.json(), ItemModel.query.all()))}
        #connection=sqlite3.connect('data.db')
        #cursor=connection.cursor()
        #query='select * from items'
        #result = cursor.execute(query)
        #items=[]
        #for row in result:
        #    items.append({'name':row[0],'price':row[1]})
        #connection.commit()
        #connection.close()
        #return {"items": items}
