#!/usr/bin/env python3
from flask import Flask, jsonify, request, make_response
from flask_migrate import Migrate
from flask_restful import Api, Resource

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///plants.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.json.compact = False

# Import db and Plant from models AFTER app is configured
from models import db, Plant

db.init_app(app)
migrate = Migrate(app, db)

# CREATE TABLES - THIS IS CRITICAL FOR CODEGRADE
with app.app_context():
    db.create_all()

api = Api(app)

class Plants(Resource):
    def get(self):
        plants = [plant.to_dict() for plant in Plant.query.all()]
        return make_response(jsonify(plants), 200)
    
    def post(self):
        data = request.get_json()
        new_plant = Plant(
            name=data['name'],
            image=data['image'],
            price=data['price'],
        )
        db.session.add(new_plant)
        db.session.commit()
        return make_response(jsonify(new_plant.to_dict()), 201)

api.add_resource(Plants, '/plants')

class PlantByID(Resource):
    def get(self, id):
        plant = Plant.query.filter_by(id=id).first()
        if not plant:
            return make_response(jsonify({"error": "Plant not found"}), 404)
        return make_response(jsonify(plant.to_dict()), 200)
    
    def patch(self, id):
        plant = Plant.query.filter_by(id=id).first()
        if not plant:
            return make_response(jsonify({"error": "Plant not found"}), 404)
        
        data = request.get_json()
        for key in data:
            setattr(plant, key, data[key])
        
        db.session.commit()
        return make_response(jsonify(plant.to_dict()), 200)
    
    def delete(self, id):
        plant = Plant.query.filter_by(id=id).first()
        if not plant:
            return make_response(jsonify({"error": "Plant not found"}), 404)
        
        db.session.delete(plant)
        db.session.commit()
        return make_response('', 204)

api.add_resource(PlantByID, '/plants/<int:id>')

if __name__ == '__main__':
    app.run(port=5555, debug=True)