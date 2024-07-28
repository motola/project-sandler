from flask import Flask
from flask_smorest import Api


from resources.item import blp as ItemBluePrint
from resources.store import blp as StoreBluePrint

app = Flask(__name__)


app.config["PROPAGATE_EXCEPTIONS"] = True
app.config["API_TITLE"] = "Stores REST API"
app.config["API_VERSION"] = "v1"
app.config["OPENAPI_VERSION"] = "3.0.3"
app.config["OPENAPI_URL_PREFIX"] = "/"
app.config["OPENAPI_SWAGGER_UI_PATH"] = "/swagger-ui"
app.config["OPENAPI_SWAGGER_UI_URL"] = "https://cdn.jsdelivr.net/npm/swagger-ui-dist/"


api = Api(app)

api.register_blueprint(ItemBluePrint)
api.register_blueprint(StoreBluePrint)










# Homepage
@app.get("/")
def get_homepage():
    return "Welcome to Python with Flask"































# # Updating items
# @app.put("/item/<string:item_id>")
# def update_item(item_id):
#     item_data = request.json()
#     if "price" not in item_data or "name" not in item_data:
#         abort(400, message="Bad request. Ensure 'price', and 'name' are included in the JSON payload.")
    
#     try:
#         item = items[item_id]
#         item |= item_data

#         return item
#     except KeyError:
#         abort(404, message="Item not found. ")


# # Updating stores
# @app.put("/store/<string:store_id>")
# def update_store(store_id):
#     store_data = request.json()
#     if "name" not in store_data or "inventory" not in store_data:
#         abort(400, message="Bad request. Ensure 'name', and 'inventory' are included in the JSON payload.")
    
#     try:
#         item = items[store_id]
#         item |= store_data

#         return item
#     except KeyError:
#         abort(404, message="Store not found. ")