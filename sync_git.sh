#!/bin/bash
# Git sync script

# Pull latest
git pull

# If changes exist, commit and push
if [[ -n $(git status -s) ]]; then
    git add .
    WEEK=$(date +%U)
    DAY=$(date +%d)
    git commit -m "Week $WEEK Day $DAY progress"
    git push
    echo "✓ Changes synced"
else
    echo "✓ Already up to date"
fi