#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 解决py2.7中文出现write错误的问题
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
# 解决py2.7中文出现write错误的问题 #
from project.exception.common_exception import CommonException


def get_greeting_words(username):
    if username is None:
        raise CommonException("0", "username is empty!")
    return "hello, "+username
