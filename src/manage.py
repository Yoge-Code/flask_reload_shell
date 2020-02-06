#!/usr/bin/env python
#  coding=utf-8
#  Author:  Yoge
#  Time:  2020/1/10

import os
from app import create_app
from flask_script import Manager, Shell, Server

from werkzeug.serving import run_with_reloader
from functools import partial
from flask.ctx import AppContext


class ReloaderShell(Shell):

    def __init__(self, app):
        self.app = app
        super().__init__()

    def run(self, *args, **kwargs):
        print(args, kwargs)
        return run_with_reloader(partial(super().run, *args, **kwargs))

    def get_context(self):
        AppContext(self.app).push()
        return dict(app=app)


app = create_app()
manager = Manager(app)
manager.add_command("shell", ReloaderShell(app))
manager.add_command("run", Server(host="0.0.0.0", port=8088))


def make_shell_context():
    return dict(app=app)


if __name__ == '__main__':
    manager.run()


