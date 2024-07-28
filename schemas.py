from marshmallow import Schema, fields



class PlainItemSchema(Schema):
    id = fields.Str(dump_only=True)
    name = fields.Str(required=True)
    price = fields.Float(required=True)
    store_id = fields.Str(required=True)

class ItemUpdateSchema(Schema): 
    name = fields.Str()
    price = fields.Float()


class PlainStoreSchema(Schema): 
    id = fields.Str(dump_only=True)
    name = fields.Str(required=True)
    inventory = fields.Str(required=True)


class ItemSchema(PlainItemSchema):
    store_id = fields.Int(required=True, dump_only=True)
    store = fields.Nested(lambda: StoreSchema(), dump_only=True)

class StoreSchema(PlainStoreSchema):
   items = fields.List(fields.Nested(lambda: ItemSchema()), dump_only=True)





