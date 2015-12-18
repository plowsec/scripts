#!/usr/bin/python2.7
# -*- coding: utf-8 -*-

import re

with open("ids.txt", "r") as f:
    data = f.readlines()

obj =  re.finditer('"id":([0-9]*),', '\n'.join(data))

for i in obj:
    print i.group(1)

#print obj.groups()
