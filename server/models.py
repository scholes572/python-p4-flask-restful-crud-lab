from flask_sqlalchemy import SQLAlchemy
from sqlalchemy_serializer import SerializerMixin

# Create the SQLAlchemy instance here
db = SQLAlchemy()

class Plant(db.Model, SerializerMixin):
    __tablename__ = 'plants'
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    image = db.Column(db.String(200))
    price = db.Column(db.Float, nullable=False)
    is_in_stock = db.Column(db.Boolean, default=True)
    
    def __repr__(self):
        return f'<Plant {self.name}>'