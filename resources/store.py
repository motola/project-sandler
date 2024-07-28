import uuid
from flask import Flask, request
from flask.views import MethodView
from flask_smorest import Blueprint, abort
from schemas import StoreSchema
from db import stores


blp = Blueprint("stores", __name__, description="Operations on stores")

# Get and Post Route for a store ID
@blp.route("/store/<string:store_id>")
class Store(MethodView):
    def get(self, store_id):
        try:
            return stores[store_id]
        except KeyError:
            return abort( 404,message="store not found")

    def delete(self, store_id):
        try:
            del stores[store_id]
            return {"message":"store deleted."}
        except KeyError:
            return abort( 404,message="store not found")
        
    def update(self, store_id):
          store_data = request.json()
          if "name" not in store_data or "inventory" not in store_data:
              abort(400, message="Bad request. Ensure 'name', and 'inventory' are included in the JSON payload.")
          try:
              store = store[store_id]
              store |= store_data
              return store
          except KeyError:
              abort(404, message="Store not found. ")
        
# Get and Post Route for a store
@blp.route("/store")
class Store(MethodView):
    def get(self):
          return {"stores": list(stores.values())}
        
    @blp.arguments(StoreSchema)
    def post(self,data):
       store_id = uuid.uuid4().hex
       new_store = {**data, "id":store_id}
       stores[store_id] = new_store
       return new_store, 201
    