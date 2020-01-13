#!/usr/bin/env python
#  coding=utf-8
#  Author:  Yoge
#  Time:  2020/1/10

import json
from flask import request
from flask import Flask


def create_app():
    app = Flask(__name__)
    app.config.from_object("settings")

    @app.route("/", methods=["GET", "POST", "OPTION"])
    def echo():
        result = {
            'headers': str(request.headers),
            'body': request.get_data().decode(),
            'query': request.query_string.decode(),
            'client_ip': request.remote_addr,
        }
        return json.dumps(result)

    return app


