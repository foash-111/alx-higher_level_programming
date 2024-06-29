0x0F-python-object_relational_mapping

what is the diffirence between backref, back_populates in sqlalchemy
I had a web application project and incorporating with my team, we work with flask and sqlalchemy we want to use docker because SQL alchemy had issues if each one install it in local machine, we want to build an image, and I want to know how to build this image , how to share it with each other, how others can install and run it without problems, can you explain all the steps from a to z please.

#docker build -t sqlalchemy-mysql-app .
#docker run -it --rm sqlalchemy-mysql-app bash
#docker cp /path/to/local/file.sql container_id:/path/inside/container/file.sql


--
import pymysql
pymysql.install_as_MySQLdb()
import MySQLdb
