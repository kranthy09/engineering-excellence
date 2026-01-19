#!/bin/bash
# Git sync script

git pull

if [[ -n $(git status -s) ]]; then
    git add .

    WEEK=$(date +%U)
    DAY=$(date +%d)
    DEFAULT_MSG="Week $WEEK Day $DAY progress"

    # Note: Quote "$1" to handle messages with spaces
    MESSAGE=${1:-$DEFAULT_MSG}

    git commit -m "$MESSAGE"
    git push
    echo "✓ Changes synced with message: $MESSAGE"
else
    echo "✓ Already up to date"
fi
