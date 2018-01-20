#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
This Document is Created by  At 2017/11/21 
"""


class Rectangle:
    """
    矩阵面积
    """
    def __init__(self, width, height):
        self.width = width
        self.height = height

    @property
    def area(self):
        return self.width * self.height


if __name__ == '__main__':
    reactangle = Rectangle(10, 12)
    area = reactangle.area
    print(area)

