import os

from apispec import APISpec
from apispec.ext.marshmallow import MarshmallowPlugin


class Config:
    basedir = os.path.abspath(os.path.dirname(__file__))

    SQLALCHEMY_DATABASE_URI = "postgresql://postgres:admin@localhost/task_tracker"  # TODO move to env
    SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, './migrations')
    SQLALCHEMY_TRACK_MODIFICATIONS = True

    DEBUG = os.environ.get('DEBUG', 'True').lower() == 'true'

    FLASK_RUN_HOST = os.environ.get("FLASK_RUN_HOST")
    FLASK_RUN_PORT = os.environ.get("FLASK_RUN_PORT")

    APISPEC_SPEC = APISpec(
        title='TaskTracker',
        version='v1',
        plugins=[MarshmallowPlugin()],
        openapi_version='2.0.0'
    )
    APISPEC_SWAGGER_URL = "/swagger/"
    APISPEC_SWAGGER_UI_URL = "/swagger-ui/"  # URI to access UI of API Doc
