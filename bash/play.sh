#!/bin/sh

print_help()    {
    echo "Usage : play [game_name]" 
    echo "Games available : minecraft"
}

if [ $# -eq 1 ]
then
    case "$1" in
        'minecraft') 
            java -jar path
            ;;
        *)  
            echo "game not known"
            ;;
    esac
else
    print_help
    exit 1
fi
