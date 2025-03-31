from flask import Flask, jsonify
from flask_cors import CORS
from .consts import COURSE_DATA

app = Flask(__name__)

CORS(app)

@app.route("/courses", methods=["GET"])
def get_courses():
    return jsonify(COURSE_DATA)