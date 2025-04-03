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

I wouldn't recommend running this. Definitely not on its own. You can place this repo in a parent folder along with the [frontend](https://github.com/FutureNine972/leaderboard-basic-vue) repo. You will also need to get PostgreSQL and set that up with the schema, and most importantly make adjustments to host information.

###### Flask - Response

```python
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
```