# -*- coding: utf-8 -*-
from project import app
from project.bottle import template, request


@app.route('/', method='GET')
def index():
    return template('printer/index', message='')


@app.route('/print', method=['GET', 'POST'])
def printer():
    if request.method == 'POST':
        from project.models.printer import Printer
        printer = Printer()
        message = printer.show_string(request.params.get('text'))
        return template('printer/index', message=message)
    return template('printer/print', message='')

