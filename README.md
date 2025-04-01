My Intro to Flask & PostgreSQL
======

### Introduction
This is one of the many repos used to display my progress on web dev, as well as the backend for my basic leaderboard learning project.

#### Strong practice with core language
This was completed using Python Flask and PostgreSQL

Function:

* Receives a GET request from the Vue-JS frontend

Responds by:

* Connecting to the course database to retrieve the ID and name
* Filling out the rest of the Mario Kart course information (players, country codes, times) from `consts.py` (Will eliminate all hard-coding soon !!!)

I wouldn't recommend running this. Definitely not on its own. You can place this repo in a parent folder along with the [frontend](https://github.com/FutureNine972/leaderboard-basic-vue) repo.

###### Flask - Response

```python
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
```