#!usr/bin/env python
# -*- conding:utf-8 -*-

"""
Created By magic at 2017-8-28
"""

import postgresql
# db = postgresql.open('localhost/postgres')
db = postgresql.open("pq://dbuser:password@127.0.0.1:5432/exampledb")
print(db)
