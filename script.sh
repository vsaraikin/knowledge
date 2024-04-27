#!/bin/bash

# GC

find . -name ".DS_Store" -delete

# –––––––––––––––––––––GIT–––––––––––––––––––––#
################################################



git status

read -p "Continue with commit? (y/n): " choice

if [ "$choice" == "y" ] || [ "$choice" == "Y" ]; then
    d=$(date +"%Y-%m-%d %T")

    tail -n +4 Home.md > .README.md
    echo "Updated README"

    git add .
    git commit -m "vault backup ${d}" 
    git push
else
    echo "Commit aborted."
fi
