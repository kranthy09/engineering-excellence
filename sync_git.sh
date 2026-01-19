#!/bin/bash
# Git sync script

git pull

if [[ -n $(git status -s) ]]; then
    git add .

    WEEK=$(date +%U)
    DAY=$(date +%d)
    if [ -z "$1" ]; then
        MESSAGE="Week $(date +%U) Day $(date +%d) progress"
    else
        MESSAGE="$*" # Captures everything you type after the script name
    fi
    git commit -m "$MESSAGE"
    git push
    echo "✓ Changes synced with message: $MESSAGE"
else
    echo "✓ Already up to date"
fi
