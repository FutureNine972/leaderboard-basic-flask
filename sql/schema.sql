DROP TABLE IF EXISTS courses;

CREATE TABLE courses (
	id SERIAL PRIMARY KEY,
	name VARCHAR(255)
);

INSERT INTO courses (id, name)
VALUES (1, 'Shy Guy Falls'), (2, 'Neo Bowser City');

select setval(
  'courses_id_seq',
  (SELECT MAX(id) FROM courses),
  true
);
INSERT INTO courses (name)
VALUES ('Rainbow Road');

select name
from courses
where name ilike '%s%' or name = 'Rainbow Road'
order by name ASC;