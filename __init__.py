from flask import Flask, request
from flask_cors import CORS
import psycopg
from .consts import PLAYER_DATA

app = Flask(__name__)

CORS(app)
DATABASE_URL = 'postgresql://postgres:postgress@localhost:5432/postgres'

@app.route("/courses/<int:course_id>/", methods=["PATCH"])
def update_course(course_id):
    body = request.get_json()

    saved_course = _save_course(
        course_id,
        body["name"],
        body.get("lapCount")
    )
    return project_course(saved_course), 200

@app.route("/courses/<int:course_id>/", methods=["DELETE"])
def delete_course(course_id):
    deleted_course = _delete_course(course_id)
    return {}, 200

@app.route("/courses", methods=["GET"])
def get_courses():
    raw_courses = fetch_courses()
    courses = project_courses(raw_courses)
    return courses

@app.route("/courses", methods=["POST"])
def create_course():
    body = request.get_json()

    new_course = _create_course(
        body["name"],
        body["lapCount"]
    )

    return project_course(new_course), 201

def _create_course(name, _lap_count):
    with psycopg.connect(DATABASE_URL) as conn:
        with conn.cursor() as cur:
            cur.execute(r"""
                    INSERT INTO courses
                    (name)
                    VALUES
                    (%s)
                    RETURNING id, name
                """,
                (name,)
            )
            return cur.fetchone()

def _save_course(course_id, name, _lap_count):
    with psycopg.connect(DATABASE_URL) as conn:
        with conn.cursor() as cur:
            cur.execute(r"""
                    UPDATE courses
                    SET name = %s
                    where id = %s
                    RETURNING id, name
                """,
                (name, course_id)
            )
            return cur.fetchone()

def _delete_course(course_id):
    with psycopg.connect(DATABASE_URL) as conn:
        with conn.cursor() as cur:
            cur.execute(r"""
                    DELETE FROM courses
                    WHERE id = %s
                """,
                (course_id,)
            )

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
        project_course(raw_course)
        for raw_course in raw_courses
    ]

def project_course(raw_course):
    c_id, c_name = raw_course
    return {
            'id': c_id,
            'name': c_name,
            'players': PLAYER_DATA.get(c_id, [])
        }