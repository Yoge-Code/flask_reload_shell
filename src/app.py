#!/usr/bin/env python
#  coding=utf-8
#  Author:  Yoge
#  Time:  2020/1/10

import json
from flask import request
from flask import Flask


def create_app():
    app = Flask(__name__)

    @app.route("/", methods=["GET", "POST", "OPTION"])
    def echo():
        result = {
            'headers': str(request.headers),
            'body': request.get_data(),
            'query': request.query_string,
        }
        print(dir(request))
        return json.dumps(result)

    return app


