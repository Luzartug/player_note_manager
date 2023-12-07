from flask import Flask

app = Flask(__name__)

# Import your routes to register them with the Flask app
from app import routes
