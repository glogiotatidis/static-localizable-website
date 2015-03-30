#!/bin/sh

./compilemessages
./build
gunicorn -w 2 -b 0.0.0.0:8000 --log-file - wsgi:application
