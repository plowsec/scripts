#!/usr/bin/sh

if [ $# -gt 1 ]
then
    pdflatex -interaction=nonstopmode $@
else
    echo "No input file specified"
    exit 1
fi
