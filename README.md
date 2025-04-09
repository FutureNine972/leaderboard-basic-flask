My Intro to Flask & PostgreSQL
======

### Introduction
This is one of the many repos used to display my progress on web dev, as well as the backend for my basic leaderboard learning project.

#### Strong practice with core language
This was completed using Python Flask and PostgreSQL

Function:

* Receives a GET request and responds with course info
    * Connects to the course database to retrieve the ID and name
* Receives a POST request and creates new course info
    * Also responds to the POST request with that newly created info JSONified
* Receives PATCH and DELETE requests and does that job accordingly
    * In a PATCH response, course information will be modified once you press the save button in the editor.

I wouldn't recommend running this. Definitely not on its own. You can place this repo in a parent folder along with the [frontend](https://github.com/FutureNine972/leaderboard-basic-vue) repo. You will also need to get PostgreSQL and set that up with the schema, and most importantly make adjustments to host information.

###### Flask - Response

```python
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