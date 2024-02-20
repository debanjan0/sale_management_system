from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import path

db = SQLAlchemy()
db_name = "database.db"


def create_app():
    app = Flask(__name__)
    app.config['secret_key'] = 'secret_key'
    app.config['SQLALCHEMY_DATABASE_URI'] ='sqlite:///' + db_name
    db.init_app(app)

    from .views import views

    app.register_blueprint(views, url_prefix='/')

    from .models import inventory, sale, sale_details, expense
    create_database(app)

    return app

def create_database(app):
    if not path.exists('.POS_GSHEET/' + db_name):
        with app.app_context():
            db.create_all()
        print("Database created")

