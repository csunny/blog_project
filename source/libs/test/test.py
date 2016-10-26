#!usr/bin/env python
# -*- coding:utf-8 -*-
"""
@ author = magic
"""
import os
import shutil
filepath = r'D:\360'


def rm_dir(filepath):
    if os.path.exists(filepath):
        shutil.rmtree(filepath)


def rm_file(file):
    if os.path.exists(file):
        os.remove(file)

if __name__ == '__main__':
    rm_file(r'D:\Adobe\magic.txt')

