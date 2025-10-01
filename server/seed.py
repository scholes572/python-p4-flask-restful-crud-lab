from app import create_app, db
from models import Plant

app = create_app()

with app.app_context():
    db.create_all()  # ensures tables exist

    # Seed some plants
    plants = [
        Plant(name="Aloe", image="./images/aloe.jpg", price=11.50),
        Plant(name="Cactus", image="./images/cactus.jpg", price=15.00),
        Plant(name="Fern", image="./images/fern.jpg", price=12.00),
    ]

    db.session.bulk_save_objects(plants)
    db.session.commit()
    print("Database seeded!")