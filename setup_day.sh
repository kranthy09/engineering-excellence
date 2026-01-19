#!/bin/bash
# Daily workspace setup script with fixed start date

# Fixed start date: November 25, 2025 (Week 0, Day 1)
START_DATE="2025-11-24"

# Get current date
CURRENT_DATE=$(date +%Y-%m-%d)
echo "current date: $CURRENT_DATE"

# Calculate days elapsed since start
DAYS_ELAPSED=$(( ($(date -d "$CURRENT_DATE" +%s) - $(date -d "$START_DATE" +%s)) / 86400 ))
echo "days elapsed $DAYS_ELAPSED"

# Calculate week and day
WEEK=$((DAYS_ELAPSED / 7))
DAY=$((DAYS_ELAPSED % 7 + 1))

WORKSPACE="solutions/week-$WEEK-[Topic]/day-$DAY-concept"

# Create workspace
mkdir -p "$WORKSPACE"
cd "$WORKSPACE" || exit

# Create files
touch problem1.py problem2.py notes.md

cat > problem1.py << FIRSTPROBLEM
"""
statement

i/o:
o/p:

i/o:
o/p:

Approaches:
1. Brute Force:

"""


class Solution:
    def brute_force(self, *args, **kwargs):
        """

        TC:
        AS:
        """
        pass

    def expected_solution(self, *args, **kwargs):
        """

        TC:
        AS:
        """
        pass


if __name__ == "__main__":
    arrs = [
        [],
    ]
    ans = Solution()
    print("******Brute Force******")
    for arr in arrs:
        print(ans.brute_force(arr))
    print("******Expected******")
    for arr in arrs:
        print(ans.expected_solution(arr))

FIRSTPROBLEM

cat > problem2.py << SECONDPROBLEM
"""
statement

i/o:
o/p:

i/o:
o/p:

Approaches:
1. Brute Force:

"""


class Solution:
    def brute_force(self, *args, **kwargs):
        """

        TC:
        AS:
        """
        pass

    def expected_solution(self, *args, **kwargs):
        """

        TC:
        AS:
        """
        pass


if __name__ == "__main__":
    arrs = [
        [],
    ]
    ans = Solution()
    print("******Brute Force******")
    for arr in arrs:
        print(ans.brute_force(arr))
    print("******Expected******")
    for arr in arrs:
        print(ans.expected_solution(arr))

SECONDPROBLEM

# Add template to notes.md
cat > notes.md << NOTES
# Week $WEEK - Day $DAY

Date: $(date +%B\ %d,\ %Y)
Days since start: $((DAYS_ELAPSED + 1))

## Notes

## Practiced Problems

### 1.
### 2.

### Pattern:
-
## Key Learnings
-

## Time Spent

- 1:
- 2:


NOTES

echo "✓ Workspace ready: $WORKSPACE"
echo "📊 Progress: Week $WEEK, Day $DAY (Day $((DAYS_ELAPSED + 1)) of journey)"
echo "📅 Start date: $START_DATE | Today: $CURRENT_DATE"
pwd