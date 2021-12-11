from flask import Flask
from os import getenv

app = Flask(__name__,template_folder='templates')
app.secret_key = getenv("SECRET_KEY")

import routes
