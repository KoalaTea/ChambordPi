#!/usr/bin/python

from app import create_app

if __name__ == '__main__':
    create_app()
    app.run(debug=True, port=8080)
