#!/usr/bin/python2.7
# -*- coding:utf-8 -*-

with open("clean.txt", "r") as f:
    data = f.readlines()

for i in range(len(data)):
    if i==0:
        backup = data[i].split("|")[1]
    else:
        if data[i].split('|')[1]==backup:
            print data[i-1]
        backup = data[i].split('|')[1]
