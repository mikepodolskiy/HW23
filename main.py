import os

from flask import Flask, request
import requests
from app.views.view import main_blueprint

# starting app
app = Flask(__name__)
# allow сyrillic symbols, setting configuration parameter for encoding
app.config['JSON_AS_ASCII'] = False

# registering blueprints
app.register_blueprint(main_blueprint)




# run app with import check
if __name__ == '__main__':
    app.run(debug=True)