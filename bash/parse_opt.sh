#!/bin/sh

#getopts skeleton taken from https://stackoverflow.com/questions/192249/how-do-i-parse-command-line-arguments-in-bash
# A POSIX variable
OPTIND=1         # Reset in case getopts has been used previously in the shell.

# Initialize our own variables:
template=""

while getopts "h?t:" opt; do
    case "$opt" in
    h|\?)
        show_help
        exit 0
        ;;
    t)  template=$OPTARG
        ;;
    esac
done

shift $((OPTIND-1))

[ "$1" = "--" ] && shift

echo "what='$1', template='$template', Leftovers: $@"

# End of file
