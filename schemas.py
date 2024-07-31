from marshmallow import Schema, fields



class PlainItemSchema(Schema):
    id = fields.Int(dump_only=True)
    name = fields.Str(required=True)
    price = fields.Float(required=True)

class PlainTagSchema(Schema):
    id = fields.Int(dump_only=True)
    name = fields.Str(required=True)



class ItemUpdateSchema(Schema): 
    name = fields.Str()
    price = fields.Float()
    store_id = fields.Int()


class PlainStoreSchema(Schema): 
    id = fields.Int(dump_only=True)
    name = fields.Str(required=True)
    inventory = fields.Int(required=True)


class ItemSchema(PlainItemSchema):
    store_id = fields.Int(required=True, load_only=True)
    store = fields.Nested(lambda: PlainStoreSchema(), dump_only=True)
    tags = fields.List(fields.Nested(PlainTagSchema()), dump_only=True)

class TagSchema(PlainTagSchema):
    store_id = fields.Int(load_only=True)
    store = fields.Nested(lambda: PlainStoreSchema(), dump_only=True)
    items = fields.List(fields.Nested(PlainItemSchema()), dump_only=True)

class StoreSchema(PlainStoreSchema):
   items = fields.List(fields.Nested(lambda: PlainItemSchema()), dump_only=True)


class TagAndItemSchema(Schema):
    message = fields.Str()
    item = fields.Nested(ItemSchema)
    tag = fields.Nested(TagSchema)





