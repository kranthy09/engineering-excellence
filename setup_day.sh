#!/bin/bash
# Daily workspace setup script

WEEK=$(date +%U)
DAY=$(date +%d)
WORKSPACE="solutions/week-$WEEK/day-$DAY"

# Create workspace
mkdir -p "$WORKSPACE"
cd "$WORKSPACE" || exit

# Create files
touch problem1.py problem2.py notes.md

# Add template to notes.md
cat > notes.md << 'NOTES'
# Day $(date +%d) - Week $(date +%U)

## Problems
1.
2.

## Pattern:

## Key Learnings
-

## Time Spent
- Problem 1:
- Problem 2:
NOTES

echo "✓ Workspace ready: $WORKSPACE"
pwd