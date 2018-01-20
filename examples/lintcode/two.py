#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
This Document is Created by  At 2017/11/21
"""

from pythonds.basic import stack


if __name__ == '__main__':
    s = stack.Stack()
    s.push(1)
    s.push(2)
    s.push(3)
    print(s.items)
    # print(s.pop())
    print(s.peek())