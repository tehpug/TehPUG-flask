TehPUG
======

TehPUG(Tehran Python Users Group) Website with Flask

A tree view of website

    |-- app
	|   |-- forms.py
	|   |-- __init__.py
	|   |-- models.py
	|   |-- static
	|   |   |-- css
	|   |   |   `-- style.css
	|   |   |-- fonts
	|   |   |   |-- FreeFarsi.ttf
	|   |   |   `-- Titr.ttf
	|   |   |-- img
	|   |   |   |-- favicon.ico
	|   |   |   |-- python-logo.png
	|   |   |   `-- tehpug-address.jpg
	|   |   `-- uploaded
	|   |-- templates
	|   |   |-- 404.html
	|   |   |-- base.html
	|   |   |-- admin.html
	|   |   |-- admin_news.html
	|   |   |-- admin_sessions.html
	|   |   |-- files.html
	|   |   |-- index.html
	|   |   |-- irc.html
	|   |   |-- list.html
	|   |   |-- login.html
	|   |   |-- news.html
	|   |   |-- sessions.html
	|   |   `-- tehpug.html
	|   |-- views.py
	|-- config.py
	|-- createDB.py
	|-- LICENSE
	|-- README.md
	|-- run.py
	|-- tmp
	|-- TODO.md
	`-- virtualenv.py

Requirements
============

    flask
    flask-login
    sqlalchemy
    flask-sqlalchemy
    flask-wtf

How to use 
==========

first you have to install virtualenv

    $ python virtualenv tehpug

then you should install the requirements this way

    $ pip install -r requirements.txt
    
then you should create a Database for the website by executing createDB.py

    $ ./createDB.py
    
now you can run the website

    $ ./run.py

How can I help?
===============

if you want to help this project you can look at the [TODO list](https://github.com/tehpug/TehPUG/blob/master/TODO.md) to see if there is any task which you can handle it?
or if you've any other idea let us know! Thanks

