#!/usr/bin/python2.7
# -*- coding: utf-8 -*-

import re
import requests
with open("delete.txt", "r") as f:
    data = f.readlines()
headers = {"Authorization":"Bearer insert_key"}

for i in data:
    r = requests.delete("https://api.quizlet.com/2.0/sets/" + i, headers=headers)
    print r.text
#print obj.groups()
