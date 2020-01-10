#!/usr/bin/env python
#  coding=utf-8
#  Author:  Yoge
#  Time:  2020/1/10

import os
from app import create_app
from flask_script import Manager, Shell, Server

app = create_app()
manager = Manager(app)
manager.add_command("run", Server(host="0.0.0.0", port=8088))

def make_shell_context():
    return dict(app=app)


if __name__ == '__main__':
    manager.run()


