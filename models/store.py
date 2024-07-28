from db import db


class storeModel(db.Model):
    __tablename__ = "stores"


    id = db.Column(db.Integer, primary_Key=True)
    name = db.Column(db.String(80),unique=False, nullable=False)
    inventory = db.Column(db.String(80),unique=False, nullable=False)
    items = db.relationship("ItemModel", back_populates="store", lazy="dynamic")