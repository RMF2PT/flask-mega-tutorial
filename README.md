microblog
=========

A microblogging web application written in Python and Flask using the series Flask Mega-Tutorial series that begins [here](http://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-i-hello-world).
The git repo can be found [here](https://github.com/miguelgrinberg/microblog).

Installation
------------

The tutorial referenced above explains how to setup a virtual environment with all the required modules.

The sqlite database must also be created before the application can run, and the `db_create.py` script takes care of that. See the [Database tutorial](http://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-iv-database) for the details.

Running
-------

To run the application in the development web server just execute `run.py` with the Python interpreter from the flask virtual environment.

My side notes
-------------

Currently, the application only allows login with OpenID through Yahoo accounts. OpenID is not a good option now. It works now, but it has limitations, so for a real live web application you should try OAuth Authentication.
This tutorial has been followed in cloud9.io, meaning that some of the code has been adapted.
