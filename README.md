My Intro to Flask
======

### Introduction
This is one of the many repos used to display my progress on web dev, as well as the backend for my basic leaderboard learning project.

#### Strong practice with core language
This was completed using Python, and furthermore Flask

Function:

* Receives a GET request from the Vue-JS frontend
* Responds with JSON content containing the Mario Kart course information from `consts.py` (will work on database stuff soon !!!)

I wouldn't recommend running this. Definitely not on its own. You can place this repo in a parent folder along with the [frontend](https://github.com/FutureNine972/leaderboard-basic-vue) repo.

###### Flask - Response

```python
app = Flask(__name__)

CORS(app)

@app.route("/courses", methods=["GET"])
def get_courses():
    return jsonify(COURSE_DATA)
```