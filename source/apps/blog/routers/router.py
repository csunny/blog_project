#!usr/bin/env python
# -*- coding:utf-8 -*-
"""
@author: magic
"""


class BlogRouter(object):
    """
    A router to control all database operations on models for different
    databases.
    """
    def db_for_read(self, model, **hint):
        pass
