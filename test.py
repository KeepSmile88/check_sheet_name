#! /usr/bin/env python3
# -*- coding: utf-8 -*-


names = {"name1": "张三", "name2": "李四"}

def get_name1(user_name):

    for key, value in names.items():

        if key in user_name:
            return value

def get_name(user_name):

    for key, value in names.items():

        if key in user_name or value in user_name:
            return value


print(get_name("用户专页-name1"))
print(get_name("1队/张三"))
