# -*- coding: utf-8 -*-

import json
from flask import Flask, request


app = Flask(__name__)


@app.route('/', methods=['GET'])
def get():
    auth = request.headers.get('Authorization')
    if auth != str(read_config()["secret"]):
        return "NOT FOUND"
    else:
        return read_model()


@app.route('/<address>', methods=['POST'])
def post(address):
    auth = request.headers.get('Authorization')
    if auth != str(read_config()["secret"]):
        return "NOT FOUND"
    else:
        write_model(address)
        return address


@app.route('/<address>', methods=['DELETE'])
def delete(address):
    return address


def get_model(key):
    return read_model(key)


def read_model():
    config = read_config()
    try:
        with open(config["file"], 'r') as f:
            return str(f.read())
    except IOError as e:
        print(e)
        return None


def write_model(address):
    config = read_config()
    try:
        all_addrs = read_model()

        if address not in all_addrs:
            addrs = all_addrs + "\n" + address
            with open(config["file"], 'w') as f:
                f.write(addrs)
                return address
    except IOError as e:
        print(e)
        return None


def read_config():
    try:
        with open('config.json', 'r') as f:
            return json.loads(f.read())
    except IOError as e:
        print(e)
        return None


if __name__ == '__main__':
    app.run(debug=True)
