#!/bin/sh
export FLASK_APP=app
export FLASK_ENV=testing

pytest -s