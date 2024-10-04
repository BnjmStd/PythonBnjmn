from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from dotenv import load_dotenv
import os

load_dotenv()

app = Flask(__name__)
CORS(app)

db_params = {
    "dbname": os.getenv('POSTGRES_DB'),
    "user": os.getenv('POSTGRES_USER'),
    "password": os.getenv('POSTGRES_PASSWORD'),
    "host": os.getenv('POSTGRES_HOST'),
    "port": os.getenv('POSTGRES_PORT')
}

app.config["SQLALCHEMY_DATABASE_URI"] = f"postgresql://{db_params['user']}:{db_params['password']}@{db_params['host']}:{db_params['port']}/{db_params['dbname']}"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)