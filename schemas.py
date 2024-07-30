from marshmallow import Schema, fields



class PlainItemSchema(Schema):
    id = fields.Int(dump_only=True)
    name = fields.Str(required=True)
    price = fields.Float(required=True)

class ItemUpdateSchema(Schema): 
    name = fields.Str()
    price = fields.Float()


class PlainStoreSchema(Schema): 
    id = fields.Int(dump_only=True)
    name = fields.Str(required=True)
    inventory = fields.Int(required=True)


class ItemSchema(PlainItemSchema):
    store_id = fields.Int(required=True, load_only=True)
    store = fields.Nested(lambda: PlainStoreSchema(), dump_only=True)

class StoreSchema(PlainStoreSchema):
   items = fields.List(fields.Nested(lambda: PlainItemSchema()), dump_only=True)





