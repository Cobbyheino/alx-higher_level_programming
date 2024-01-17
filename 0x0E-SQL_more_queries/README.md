. ID can't be null
mandatory
Write a script that creates the table id_not_null on your MySQL server.

id_not_null description:
id INT with the default value 1
name VARCHAR(256)
The database name will be passed as an argument of the mysql command
If the table id_not_null already exists, your script should not fail
guillaume@ubuntu:~/$ cat 4-never_empty.sql | mysql -hlocalhost -uroot -p hbtn_0d_2
Enter password: 
guillaume@ubuntu:~/$ echo 'INSERT INTO id_not_null (id, name) VALUES (89, "Best School");' | mysql -hlocalhost -uroot -p hbtn_0d_2
Enter password: 
guillaume@ubuntu:~/$ echo 'SELECT * FROM id_not_null;' | mysql -hlocalhost -uroot -p hbtn_0d_2
Enter password: 
id  name
89  Best School
guillaume@ubuntu:~/$ echo 'INSERT INTO id_not_null (name) VALUES ("Best");' | mysql -hlocalhost -uroot -p hbtn_0d_2
Enter password: 
guillaume@ubuntu:~/$ echo 'SELECT * FROM id_not_null;' | mysql -hlocalhost -uroot -p hbtn_0d_2
Enter password: 
id  name
89  Best School
1   Best
guillaume@ubuntu:~/$ 
Repo:

GitHub repository: alx-higher_level_programming
Directory: 0x0E-SQL_more_queries
File: 4-never_empty.sql
   
5. Unique ID
mandatory
Write a script that creates the table unique_id on your MySQL server.

unique_id description:
id INT with the default value 1 and must be unique
name VARCHAR(256)
The database name will be passed as an argument of the mysql command
If the table unique_id already exists, your script should not fail
guillaume@ubuntu:~/$ cat 5-unique_id.sql | mysql -hlocalhost -uroot -p hbtn_0d_2
Enter password: 
guillaume@ubuntu:~/$ echo 'INSERT INTO unique_id (id, name) VALUES (89, "Best School");' | mysql -hlocalhost -uroot -p hbtn_0d_2
Enter password: 
guillaume@ubuntu:~/$ echo 'SELECT * FROM unique_id;' | mysql -hlocalhost -uroot -p hbtn_0d_2
Enter password: 
id  name
89  Best School
guillaume@ubuntu:~/$ echo 'INSERT INTO unique_id (id, name) VALUES (89, "Best");' | mysql -hlocalhost -uroot -p hbtn_0d_2
Enter password: 
ERROR 1062 (23000) at line 1: Duplicate entry '89' for key 'unique_id.id'
guillaume@ubuntu:~/$ echo 'SELECT * FROM unique_id;' | mysql -hlocalhost -uroot -p hbtn_0d_2
Enter password: 
id  name
89  Best School
guillaume@ubuntu:~/$ 
Repo:

GitHub repository: alx-higher_level_programming
Directory: 0x0E-SQL_more_queries
File: 5-unique_id.sql
   
6. States table
mandatory
Write a script that creates the database hbtn_0d_usa and the table states (in the database hbtn_0d_usa) on your MySQL server.

states description:
id INT unique, auto generated, can’t be null and is a primary key
name VARCHAR(256) can’t be null
If the database hbtn_0d_usa already exists, your script should not fail
If the table states already exists, your script should not fail
guillaume@ubuntu:~/$ cat 6-states.sql | mysql -hlocalhost -uroot -p
Enter password: 
guillaume@ubuntu:~/$ echo 'INSERT INTO states (name) VALUES ("California"), ("Arizona"), ("Texas");' | mysql -hlocalhost -uroot -p hbtn_0d_usa
Enter password: 
guillaume@ubuntu:~/$ echo 'SELECT * FROM states;' | mysql -hlocalhost -uroot -p hbtn_0d_usa
Enter password: 
id  name
1   California
2   Arizona
3   Texas
guillaume@ubuntu:~/$ 
Repo:

GitHub repository: alx-higher_level_programming
Directory: 0x0E-SQL_more_queries
File: 6-states.sql
   
7. Cities table
mandatory
Write a script that creates the database hbtn_0d_usa and the table cities (in the database hbtn_0d_usa) on your MySQL server.

cities description:
id INT unique, auto generated, can’t be null and is a primary key
state_id INT, can’t be null and must be a FOREIGN KEY that references to id of the states table
name VARCHAR(256) can’t be null
If the database hbtn_0d_usa already exists, your script should not fail
If the table cities already exists, your script should not fail
guillaume@ubuntu:~/$ cat 7-cities.sql | mysql -hlocalhost -uroot -p
Enter password: 
guillaume@ubuntu:~/$ echo 'INSERT INTO cities (state_id, name) VALUES (1, "San Francisco");' | mysql -hlocalhost -uroot -p hbtn_0d_usa
Enter password: 
guillaume@ubuntu:~/$ echo 'SELECT * FROM cities;' | mysql -hlocalhost -uroot -p hbtn_0d_usa
Enter password: 
id  state_id    name
1   1   San Francisco
guillaume@ubuntu:~/$ echo 'INSERT INTO cities (state_id, name) VALUES (10, "Paris");' | mysql -hlocalhost -uroot -p hbtn_0d_usa
Enter password: 
ERROR 1452 (23000) at line 1: Cannot add or update a child row: a foreign key constraint fails (`hbtn_0d_usa`.`cities`, CONSTRAINT `cities_ibfk_1` FOREIGN KEY (`state_id`) REFERENCES `states` (`id`))
guillaume@ubuntu:~/$ echo 'SELECT * FROM cities;' | mysql -hlocalhost -uroot -p hbtn_0d_usa
Enter password: 
id  state_id    name
1   1   San Francisco
guillaume@ubuntu:~/$ 
Repo:

GitHub repository: alx-higher_level_programming
Directory: 0x0E-SQL_more_queries
File: 7-cities.sql
   
8. Cities of California
mandatory
Write a script that lists all the cities of California that can be found in the database hbtn_0d_usa.

The states table contains only one record where name = California (but the id can be different, as per the example)
Results must be sorted in ascending order by cities.id
You are not allowed to use the JOIN keyword
The database name will be passed as an argument of the mysql command
guillaume@ubuntu:~/$ echo 'SELECT * FROM states;' | mysql -hlocalhost -uroot -p hbtn_0d_usa
Enter password: 
id  name
1   California
2   Arizona
3   Texas
4   Utah
guillaume@ubuntu:~/$ echo 'SELECT * FROM cities;' | mysql -hlocalhost -uroot -p hbtn_0d_usa
Enter password: 
id  state_id    name
1   1   San Francisco
2   1   San Jose
4   2   Page
6   3   Paris
7   3   Houston
8   3   Dallas
guillaume@ubuntu:~/$ cat 8-cities_of_california_subquery.sql | mysql -hlocalhost -uroot -p hbtn_0d_usa
Enter password: 
id  name
1   San Francisco
2   San Jose
guillaume@ubuntu:~/$ 
Repo:

GitHub repository: alx-higher_level_programming
Directory: 0x0E-SQL_more_queries
File: 8-cities_of_california_subquery.sql
   
9. Cities by States
mandatory
Write a script that lists all cities contained in the database hbtn_0d_usa.

Each record should display: cities.id - cities.name - states.name
Results must be sorted in ascending order by cities.id
You can use only one SELECT statement
The database name will be passed as an argument of the mysql command
guillaume@ubuntu:~/$ echo 'SELECT * FROM states;' | mysql -hlocalhost -uroot -p hbtn_0d_usa
Enter password: 
id  name
1   California
2   Arizona
3   Texas
4   Utah
guillaume@ubuntu:~/$ echo 'SELECT * FROM cities;' | mysql -hlocalhost -uroot -p hbtn_0d_usa
Enter password: 
id  state_id    name
1   1   San Francisco
2   1   San Jose
4   2   Page
6   3   Paris
7   3   Houston
8   3   Dallas
guillaume@ubuntu:~/$ cat 9-cities_by_state_join.sql | mysql -hlocalhost -uroot -p hbtn_0d_usa
Enter password: 
id  name    name
1   San Francisco   California
2   San Jose    California
4   Page    Arizona
6   Paris   Texas
7   Houston Texas
8   Dallas  Texas
guillaume@ubuntu:~/$ 
Repo:

GitHub repository: alx-higher_level_programming
Directory: 0x0E-SQL_more_queries
File: 9-cities_by_state_join.sql
   
10. Genre ID by show
mandatory
Import the database dump from hbtn_0d_tvshows to your MySQL server: download

Write a script that lists all shows contained in hbtn_0d_tvshows that have at least one genre linked.

Each record should display: tv_shows.title - tv_show_genres.genre_id
Results must be sorted in ascending order by tv_shows.title and tv_show_genres.genre_id
You can use only one SELECT statement
The database name will be passed as an argument of the mysql command
guillaume@ubuntu:~/$ cat 10-genre_id_by_show.sql | mysql -hlocalhost -uroot -p hbtn_0d_tvshows
Enter password: 
title   genre_id
Breaking Bad    1
Breaking Bad    6
Breaking Bad    7
Breaking Bad    8
Dexter  1
Dexter  2
Dexter  6
