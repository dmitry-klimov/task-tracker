import config
from .task_tracker_app import app


@app.route('/')
@app.route('/index')
def index():
    return (
            '<p>TaskTracker API:</p>' +
            f'<p><a href="{config.Config.APISPEC_SWAGGER_URL}">Swagger URL</a>' +
            f'<p><a href="{config.Config.APISPEC_SWAGGER_UI_URL}">Swagger UI URL</a>'
    )
