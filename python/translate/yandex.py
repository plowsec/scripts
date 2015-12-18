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
    i = 1
    txt = ""
    
    #captures english and russian words
    pattern = u'<span class="b-translation__text">([a-zA-Z!?., \u0400-\u0500]*)</span>'

    #word to word translation is handled differently by yandex than full sentence translation
    multi_words_pattern = '<div class="b-translation__fulltext"><p>(.*)</p></div>'

    """Here, we parse the commandline options and react according to them"""
    parser = argparse.ArgumentParser(description="A simple yandex translate wrapper")
    parser.add_argument('totranslate', metavar='string_to_translate', type=str, help='a string to translate')
    options = parser.parse_args()

    if options.totranslate == None:
        parser.error("[!] You need to feed me with something to translate")
        parser.print_help()
        #sys.exit(1)

    url = "https://slovari.yandex.ru/{content}/en/".format(content=sanitize(options.totranslate))
    req = requests.get(url, headers=user_agent)

    content = req.text

    #print content
    searchObj = re.finditer(pattern,content)

    if not searchObj:
        searchObj = re.finditer(multi_words_pattern, content)

        if not searchObj:
            print "An error occured, none of the specified patterns were found"
            sys.exit(1)
    
    #print searchObj.group(0)
    #print searchObj
    for result in searchObj:
        
        txt  += result.group(1)
        
        if i%2==0:
            txt += " : "
        else:
            txt += "\n"
        i+=1

    print txt
if __name__ == '__main__':
    main()
