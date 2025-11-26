#!/bin/bash
# Daily workspace setup script with custom week/day tracking

TRACKER_FILE=".progress_tracker"

# Initialize tracker if doesn't exist
if [[ ! -f "solutions/$TRACKER_FILE" ]]; then
    echo "0" > "solutions/$TRACKER_FILE"  # Start from day 0
    echo "📅 Starting journey: Week 0, Day 1"
fi

# Read current day count
TOTAL_DAYS=$(cat "solutions/$TRACKER_FILE")

# Calculate week and day
WEEK=$((TOTAL_DAYS / 7))
DAY=$((TOTAL_DAYS % 7 + 1))

WORKSPACE="solutions/week-$WEEK/day-$DAY"

# Create workspace
mkdir -p "$WORKSPACE"
cd "$WORKSPACE" || exit

# Create files
touch problem1.py problem2.py notes.md

# Add template to notes.md
cat > notes.md << NOTES
# Week $WEEK - Day $DAY (Total: Day $((TOTAL_DAYS + 1)))

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

# Increment tracker for next time
echo $((TOTAL_DAYS + 1)) > "../../$TRACKER_FILE"

echo "✓ Workspace ready: $WORKSPACE"
echo "📊 Progress: Week $WEEK, Day $DAY (Total: $((TOTAL_DAYS + 1)) days)"
pwd