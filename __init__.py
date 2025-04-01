from flask import Flask, jsonify
from flask_cors import CORS
import psycopg
from .consts import PLAYER_DATA

app = Flask(__name__)

CORS(app)
DATABASE_URL = 'postgresql://postgres:postgress@localhost:5432/postgres'

@app.route("/courses", methods=["GET"])
def get_courses():
    raw_courses = fetch_courses()
    courses = project_courses(raw_courses)
    return jsonify(courses)

def fetch_courses():
    with psycopg.connect(DATABASE_URL) as conn:
        with conn.cursor() as cur:
            cur.execute(r"""
                SELECT
                    id,
                    name
                FROM courses
                ORDER BY name ASC
                """
            )

            return cur.fetchall()

def project_courses(raw_courses):
    return [
        {
            'id': c_id,
            'name': c_name,
            'players': PLAYER_DATA.get(c_id, [])
        }
        for c_id, c_name in raw_courses
    ]
