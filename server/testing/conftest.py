import warnings
import pytest

warnings.filterwarnings("ignore", category=DeprecationWarning)

from app import app, db
from models import Plant

@pytest.fixture(scope='session', autouse=True)
def setup_database():
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
    with app.app_context():
        db.create_all()
        # Seed plants
        plants = [
            Plant(name="Aloe", image="./images/aloe.jpg", price=11.50),
            Plant(name="Cactus", image="./images/cactus.jpg", price=15.00),
            Plant(name="Fern", image="./images/fern.jpg", price=12.00),
        ]
        db.session.bulk_save_objects(plants)
        db.session.commit()
        yield
        db.drop_all()

def pytest_itemcollected(item):
    par = item.parent.obj
    node = item.obj
    pref = par.__doc__.strip() if par.__doc__ else par.__class__.__name__
    suf = node.__doc__.strip() if node.__doc__ else node.__name__
    if pref or suf:
        item._nodeid = ' '.join((pref, suf))
