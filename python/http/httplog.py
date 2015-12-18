#!/usr/bin/python2.7

import requests
import logging
import httplib


#source : https://stackoverflow.com/questions/16337511/log-all-requests-from-the-python-requests-module


url = "https://api.quizlet.com/2.0/sets"
data = {
        "whitespace":"1", 
        "terms[]":["lait", "petitspois"], 
        "definitions[]":["milk", "peas"],
        "title":"test",
        "lang_terms":"fr",
        "lang_definitions":"en"
        }
datas = "whitespace=1&terms[]=lait&definitions[]=milk&terms[]=petitspois&definitions[]=peas&title=test&lang_terms=fr&lang_definitions=en"

headers = {
            "Authorization":"Bearer tm6qfcX3C37Y2mN2tQC9XWvdshcGnDgXndjTCVvE"
          }
httplib.HTTPConnection.debuglevel = 1

logging.basicConfig()
logging.getLogger().setLevel(logging.DEBUG)
requests_log = logging.getLogger("requests.packages.urllib3")
requests_log.setLevel(logging.DEBUG)
requests_log.propagate = True
r = requests.post(url, data=data, headers=headers)
print r.text


