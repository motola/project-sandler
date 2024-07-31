import uuid
from flask import Flask, request
from flask.views import MethodView
from flask_smorest import Blueprint, abort

from sqlalchemy.exc import SQLAlchemyError


from db import db
from models import ItemModel
from schemas import ItemSchema
blp = Blueprint("items", __name__, description="Operations on stores")




@blp.route("/item/<string:item_id>")
class Item(MethodView):
    @blp.response(200, ItemSchema)
    def get(self, item_id):
        try:
             item = ItemModel.query.get_or_404(item_id)
             return item
        except KeyError:
            return abort( 404,message="item not found")

    def delete(self, item_id):
        try:
           item = ItemModel.query.get_or_404(item_id)
           raise NotImplementedError("Deleting an item is not implemented. ")
        except KeyError:
            return abort( 404, message="item not found")
        
    def put(self, item_data, item_id):
          
          try:
              if item:
                item = ItemModel.query.get(item_id)
                item = item_data["price"]
                item = item_data["name"]
              else:
                  item = ItemModel(id=item_id, **item_data)

              db.session.add(item)
              db.session.commit()

              return item
          except KeyError:
              abort(404, message="Store not found. ")



@blp.route("/item")
class ItemList(MethodView):
    @blp.response(200, ItemSchema(many=True))
    def get(self):
        item = ItemModel.query.get_or_404(item_id)

        return item
       
    @blp.arguments(ItemSchema)
    @blp.response(201, ItemSchema)
    def post(self, item_data):
        item = ItemModel(**item_data)
        try:
            db.session.add(item)
            db.session.commit()
        except SQLAlchemyError:
            abort(500, message="An error occurred while inserting the item")
    
        return item
 
         