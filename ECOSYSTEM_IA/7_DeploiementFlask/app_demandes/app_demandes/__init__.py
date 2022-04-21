from flask import Flask

from app_demandes.config import Config

UPLOAD_FOLDER = 'static/uploads/'


app = Flask(__name__)
app.config.from_object(Config)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024

app.secret_key = "secret key"

from app_demandes import routes