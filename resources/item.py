import uuid
from flask import Flask, request
from flask.views import MethodView
from flask_smorest import Blueprint, abort
from schemas import ItemSchema
from db import items, stores


blp = Blueprint("items", __name__, description="Operations on stores")




@blp.route("/item/<string:item_id>")
class Store(MethodView):
    @blp.response(200, ItemSchema)
    def get(self, item_id):
        try:
            return items[item_id]
        except KeyError:
            return abort( 404,message="item not found")

    def delete(self, item_id):
        try:
            del items[item_id]
            return {"message":"item deleted."}
        except KeyError:
            return abort( 404, message="item not found")
        
    def update(self, item_id):
          item_data = request.json()
          if "name" not in item_data or "price" not in item_data:
              abort(400, message="Bad request. Ensure 'name', and 'inventory' are included in the JSON payload.")
          try:
              item = item[item_id]
              item |= item_data
              return item
          except KeyError:
              abort(404, message="Store not found. ")



@blp.route("/item/")
class Store(MethodView):


    @blp.arguments(ItemSchema)
    def post(self, data):
        if data["store_id"] not in stores:
           abort(404, message="store not found.")
        item_id = uuid.uuid4().hex
        item = {**data, "id": item_id}
        items[item_id] = item
        return item, 201

    def get(self):
        return {"items": list(items.values())}, 200

        