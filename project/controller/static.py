# -*- coding: utf-8 -*-
from project import app, app_root_path
from project.bottle import static_file
import os


@app.route('/<file:re:(favicon.ico|humans.txt)>')
def favicon(file):
    return static_file(file, root=os.path.join(app_root_path, 'project', 'static', 'misc'))


@app.route('/<path:re:(images|css|js|fonts)\/.+>')
def server_static(path):
    return static_file(path, root=os.path.join(app_root_path, 'project', 'static'))


@app.route('/static/<path>')
def server_all_static(path):
    return static_file(path, root=os.path.join(app_root_path, 'project', 'static'))
