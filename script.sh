#!/bin/bash

# Check for any unwanted files or changes
git status

# Prompt the user to continue
read -p "Continue with commit? (y/n): " choice

if [ "$choice" == "y" ] || [ "$choice" == "Y" ]; then
    d=$(date +"%Y-%m-%d %T")
    git add .  # Consider being more explicit here
    git commit -m "vault backup ${d}" 
    git gc
    git push
else
    echo "Commit aborted."
fi
