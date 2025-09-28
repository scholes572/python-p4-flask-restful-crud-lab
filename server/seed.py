#!/usr/bin/env python3

from app import app
from models import db, Plant

with app.app_context():
    print("Seeding database... 🌱")

    # Reset the database
    db.drop_all()
    db.create_all()

    # Create plants
    aloe = Plant(
        name="Aloe",
        image="./images/aloe.jpg",
        price=11.50,
        is_in_stock=True,
    )

    zz_plant = Plant(
        name="ZZ Plant",
        image="./images/zz-plant.jpg",
        price=25.98,
        is_in_stock=False,
    )

    # Add them to the session
    db.session.add_all([aloe, zz_plant])
    db.session.commit()

    print("Seeding done ✅")
