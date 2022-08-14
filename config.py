import os


class Config:
    basedir = os.path.abspath(os.path.dirname(__file__))

    # SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'app.db')
    SQLALCHEMY_DATABASE_URI = "postgresql://postgres:admin@localhost/task_tracker"
    SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, '../migrations')

    DEBUG = True  # TODO: would be better to get it from ENV variables

    FLASK_RUN_HOST = os.environ.get("FLASK_RUN_HOST")
    FLASK_RUN_PORT = os.environ.get("FLASK_RUN_PORT")

    SWAGGER_URL = '/api/docs'
    API_URL = '/static/docs/swagger.json'

    # cur_dir_name = os.path.dirname(__file__)
    # dotenv_path = os.path.join(cur_dir_name, 'environment.env')
    # if os.path.exists(dotenv_path):
    #     load_dotenv(dotenv_path)
    # else:
    #     raise Exception("os.path doesn't exist. Check if environment.env file is in the root of the app")
    #
    # # better to move the most of these values to ENV_VARIABLES, or whatever - no such things in repos!
    # SQLALCHEMY_DATABASE_URI = os.environ.get("SQLALCHEMY_DATABASE_URI_PROD")
    # SQLALCHEMY_TRACK_MODIFICATIONS = (os.environ.get('SQLALCHEMY_TRACK_MODIFICATIONS') == 'True')
    #
    #
    # MAIL_SERVER = os.environ.get("MAIL_SERVER")
    # MAIL_PORT = os.environ.get("MAIL_PORT")
    # MAIL_USE_TLS = os.environ.get("MAIL_USE_TLS")
    # MAIL_USERNAME = os.environ.get("MAIL_USERNAME")
    # MAIL_PASSWORD = os.environ.get("MAIL_PASSWORD")
    # MAIL_DEFAULT_SENDER = os.environ.get("MAIL_DEFAULT_SENDER")
    #
    # JWT_SECRET_KEY = os.environ.get("JWT_SECRET_KEY")  # secret data with restricted access
    # JWT_ACCESS_TOKEN_EXPIRES = timedelta(minutes=10)
    #
    # SECRET_KEY = os.environ.get('SECRET_KEY')
    # PASSWORD_STRENGTH = 0.66
    #
    # DEBUG = (os.environ.get('DEBUG') == 'True')  # must be easy to change on different environments too
    #
    # LOGGER_CONF_PATH = os.path.join(cur_dir_name, os.environ.get('LOGGER_CONF_PATH'))
    # LOGGER_SOCKET_ERR_PATH = os.path.join(cur_dir_name, os.environ.get('LOGGER_SOCKET_ERR_PATH')).replace("\\", "/")

# TODO Almost all, or, at least, the most part of these setting must be easy to change without committing it to repo
