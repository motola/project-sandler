
from flask import Flask, request
from flask.views import MethodView
from flask_jwt_extended import jwt_required
from flask_smorest import Blueprint, abort
from schemas import StoreSchema
from models import StoreModel

from db import db
from sqlalchemy.exc import SQLAlchemyError, IntegrityError

blp = Blueprint("stores", __name__, description="Operations on stores")

# Get and Post Route for a store ID
@blp.route("/store/<string:store_id>")
class Store(MethodView):
    def get(self, store_id):
        try:
           store = StoreModel.query.get_or_404(store_id)
           return store
        except KeyError:
            return abort( 404,message="store not found")

    def delete(self, store_id):
        try:
           store = StoreModel.query.get_or_404(store_id)
           db.session.delete(store)
           db.session.commit()
           return {"message":"Store Deleted"}
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
    @jwt_required()
    @blp.response(200, StoreSchema(many=True))
    def get(self):
          return StoreModel.query.all()
        
    @blp.arguments(StoreSchema)
    @blp.response(201, StoreSchema)
    def post(self, store_data):
        store = StoreModel(**store_data)
        try:
            db.session.add(store)
            db.session.commit()
        except IntegrityError:
            abort(
                400,
                message="A store ith that nam already exist"
            )

        except SQLAlchemyError:
            abort(500, message="An error occurred while inserting the item")
    
        return store