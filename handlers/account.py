#!/usr/bin/env python
# -*- coding: utf-8 -*-

import tornado.web

from . import BaseHandler

class SignupHandler(BaseHandler):
    def get(self):
        pass

class SigninHandler(BaseHandler):
    def get(self):
        pass

handlers = [
    (r'/account/signup', SignupHandler),
    (r'/account/signin', SigninHandler),
]