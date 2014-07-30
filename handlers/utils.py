#!/usr/bin/env python
# -*- coding: utf-8 -*-

def return_result(result, error):
    if error:
        return repr(error)
    return repr(result)