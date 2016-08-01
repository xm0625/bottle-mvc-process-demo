#!/usr/bin/python
# -*- conding:utf-8 -*-
__author__ = 'xm'


def response_json(fn):
    def __wrapper(*args, **kwargs):
        response_data = fn(*args, **kwargs)
        if ("code" in response_data) and ("message" in response_data):
            return response_data
        else:
            return {"code": "1", "message": "ok", "data": response_data}

    return __wrapper
