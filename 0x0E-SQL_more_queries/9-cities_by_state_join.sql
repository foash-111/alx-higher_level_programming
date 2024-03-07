--  a script that lists all cities contained in the database hbtn_0d_usa.

SELECT id, name, states.name  FROM cities
NATURAL JOIN states ON states
ORDER BY id ASC;
