#!/bin/bash

# GC

find . -name ".DS_Store" -delete

# –––––––––––––––––––––NAV–––––––––––––––––––––#
################################################
python main.py
echo "updated navigration!"


# –––––––––––––––––––––GIT–––––––––––––––––––––#
################################################



# Check for any unwanted files or changes
git status

# Prompt the user to continue
read -p "Continue with commit? (y/n): " choice

if [ "$choice" == "y" ] || [ "$choice" == "Y" ]; then
    d=$(date +"%Y-%m-%d %T")

    tail -n +4 Home.md > .github/README.md
    echo "Updated README"

    git add .  # Consider being more explicit here
    git commit -m "vault backup ${d}" 
    git push
else
    echo "Commit aborted."
fi
