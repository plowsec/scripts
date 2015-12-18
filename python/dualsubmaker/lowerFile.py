#!/usr/bin/env python
# -*- coding: utf-8 -*-
def lowerFile(fichier):
    output = ""
    file = open(fichier, "r")
    name = fichier[:fichier.find(".")]+"_converted"+fichier[fichier.find("."):]
    op = open(name, "a")
    for line in file:
        op.write(unicode(line,encoding="utf-8").lower().encode("UTF-8"))
    print("File ",name, " successfully generated.")
    file.close()
    op.close()
i = str(raw_input("Enter the name of the file you want to convert or press ENTER to quit : "))
while i!="":
    lowerFile(i)
    i = str(raw_input("Enter the name of the file you want to convert or press ENTER to quit : "))
