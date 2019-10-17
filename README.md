# bexar_django

to configure add the datqbase connections to your /etc/bexar.yaml file
like the below
the SQLALCHEMY file is your database imported from github at
https://github.com/crc32a/bexar_court_reader.git

DATABASES:
  default:
    CHARSET: utf8mb4
    ENGINE: django.db.backends.mysql
    HOST: <your host>
    NAME: <your database name>
    PASSWORD: <your password>
    PORT: '3306'
    USER: <your user>
SQLALCHEMY: mysql+mysqldb://<courtuser>:<courtpasswd>@<courthost>:3306/<courtdb>

after that start the server via
python manage.py runserver
