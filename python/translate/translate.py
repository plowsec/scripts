#!/usr/bin/python2.7
# -.- coding:utf-8 -.-

from traceback import print_exc
import requests
import re
import argparse,sys

#from html2text import dehtml

"""curl "https://slovari.yandex.ru/Я%20даже%20боюсь/en/"""


def sanitize(string):
    return string.replace(" ", "+")

def main():
    
    user_agent = {'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:23.0) Gecko/20100101 Firefox/23.0'}
    pattern = '<div dir="ltr" class="t0">(.*)</div><form'    
    
    """Here, we parse the commandline options and react according to them"""
    parser = argparse.ArgumentParser(description="A simple google translate wrapper")
    parser.add_argument('totranslate', metavar='string_to_translate', type=str, help='a string to translate')
    options = parser.parse_args()

    if options.totranslate == None:
        parser.error("[!] You need to feed me with something to translate")
        parser.print_help()
        #sys.exit(1)

    url = "https://translate.google.ch/m?hl={dlang}&sl={slang}&q={content}".format(dlang="fr", slang="ru", content=sanitize(options.totranslate))
    req = requests.get(url, headers=user_agent)

    content = req.text

    searchObj = re.search(pattern,content)
    if searchObj:
        print searchObj.group(1)
    else:
        print "An error occured, pattern not found"

if __name__ == '__main__':
    main()
