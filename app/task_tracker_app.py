from flask import Flask
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_apispec.extension import FlaskApiSpec

from config import Config

app = Flask(__name__)
app.config.from_object(Config())
db = SQLAlchemy(app)
migrate = Migrate(app, db)

api = Api(app)

docs = FlaskApiSpec(app)

from .views import *
from .models import *
from .apis import *
