#!/usr/bin/python3
'''
    Main website
'''
from app import application

if __name__ == "__main__":
    application.run(host='127.0.0.1', port=5000)
