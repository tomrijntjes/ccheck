#!/usr/bin/python3

import db_create

from config import DEBUG, HOST, PORT

from app import app

app.run(debug=DEBUG,host=HOST, port=PORT)
