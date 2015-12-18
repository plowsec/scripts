#!/bin/sh

print_help()    {
    echo "Usage : new [filename] [template]" 
    echo "Templates available : classic,full,tech,math"
}

main()  
{
    filename="$1.tex"
    template_name = ""
    case "$2" in
        classic) template_name="template_classic" 
            ;;
        full)  template_name="template_full"
            ;;
        tech)  template_name="template_tech"
            ;;
        math)  template_name="template_math"
            ;;
    esac

    cp /home/vladimir/templates/$template_name.tex $filename && vim $filename
}

if [ $# -eq 2 ]
then
    main $1 $2
else
    print_help
    exit 1
fi
