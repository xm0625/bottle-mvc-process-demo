#!/usr/bin/python
# -*- conding:utf-8 -*-
from project.bottle import response
import json

__author__ = 'xm'


def response_json(fn):
    def __wrapper(*args, **kwargs):
        response_data = fn(*args, **kwargs)
        if ("code" in response_data) and ("message" in response_data):
            return response_data
        else:
            response.content_type = 'application/json; charset=' + response.charset
            result_data = json.dumps({"code": "1", "message": "ok", "data": response_data}, encoding=response.charset,
                                     ensure_ascii=False)
            return result_data

    return __wrapper
