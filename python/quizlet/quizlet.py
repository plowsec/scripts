#!/usr/bin/python
# -*- coding: utf-8 -*-

import requests
import re

#python2.* sucks with unicode handling, this script won't run out the box with python2.*

def fetch_words(filename):
    """
    - Role : Parse a database of terms and definitions and classifies them ("french" or "russian").
    - Argument : path to database
    - return type : dict
    """

    words = {
            "french":[],
            "russian":[]
            }
    i=1

    with open(filename, "r") as db:
        data = db.readlines()

    #in cleaner.py, we made sure that a term and his defintion were directly alternated
    for word in data:
        if i%2!=0:
            words['french'] += [word.lower()]
        else:
            words["russian"] += [word.lower()]
        i+=1

    return words


def create_set(words, title):
    """
    - Role : creates a set using the Quizlet API. Expects a dictionnary in argument.
    - Argument words : expects a dict with the following keys : french,russian
    - Argument title : expects a string. This is the title to the set to be created
    - Return type : None
    """

    url = "https://api.quizlet.com/2.0/sets"
    data = {
            "whitespace":"1", 
            "terms[]":words['russian'], 
            "definitions[]":words['french'],
            "title":title,
            "lang_terms":"ru",
            "lang_definitions":"fr"
            }

    headers = {
                "Authorization":"Bearer insert_key"
              }

    r = requests.post(url, data=data, headers=headers)
    print(r.text)

if __name__ == '__main__':
    
    """ Here we parse a database and subdivide it into chunks of 'words_per_sets' items. Each chunk of data is fed to previous function 'create_set'"""

    database_path = "words.txt"
    title = "Базовая лексика"
    words_per_set = 30
    j=1
    index = ""

    bulk = fetch_words(database_path)

    for i in range(0, len(bulk['french']), words_per_set):
        chunk_fr = bulk["french"][i:i + words_per_set]
        chunk_ru = bulk["russian"][i:i + words_per_set]
        chunk_set = {
                        "french":chunk_fr,
                        "russian":chunk_ru
                    }

        #to allow alphabetical sorting of the sets in the future
        if j < 10:
            index = "00" + str(j)
        elif j < 100:
            index = "0" + str(j)
        else:
            index = str(j)
           
        create_set(chunk_set, title + " " + index)
        j+=1





    
