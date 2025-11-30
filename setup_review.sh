#!/bin/bash
# Weekly review setup script

# Fixed start date: November 25, 2025 (Week 0, Day 1)
START_DATE="2025-11-25"

# Get current date
CURRENT_DATE=$(date +%Y-%m-%d)

# Calculate days elapsed since start
START_SECONDS=$(date -d "$START_DATE" +%s)
CURRENT_SECONDS=$(date -d "$CURRENT_DATE" +%s)
DAYS_ELAPSED=$(( (CURRENT_SECONDS - START_SECONDS) / 86400 ))

# Calculate current week
WEEK=$((DAYS_ELAPSED / 7))

WEEK_FOLDER="solutions/week-$WEEK"
REVIEW_FILE="$WEEK_FOLDER/reflection-log-week-$WEEK.md"

# Create week folder if doesn't exist
mkdir -p "$WEEK_FOLDER"

# Create reflection log template
cat > "$REVIEW_FILE" << 'TEMPLATE'
# Week ${WEEK} Review

**Date Range:** [Start Date] - [End Date]
**Review Date:** $(date +%B\ %d,\ %Y)

---

## Problems Solved This Week

| Day | Problem 1 | Problem 2 | Pattern | Time | First Try? |
|-----|-----------|-----------|---------|------|------------|
| 1   |           |           |         |      | ✅/⚠️/❌    |
| 2   |           |           |         |      | ✅/⚠️/❌    |
| 3   |           |           |         |      | ✅/⚠️/❌    |
| 4   |           |           |         |      | ✅/⚠️/❌    |
| 5   |           |           |         |      | ✅/⚠️/❌    |
| 6   |           |           |         |      | ✅/⚠️/❌    |
| 7   |           |           |         |      | ✅/⚠️/❌    |

**Total Problems:**
**Success Rate (First Try):**
**Average Time (Medium):**

---

## Patterns Progress

### Mastered ✅
-

### Practicing 🔄
-

### Not Started ⏳
-

---

## Key Learnings

### Pattern Recognition
-

### New Concepts
-

### Debugging Insights
-

---

## Communication Improvements

### What Worked Well
-

### What to Improve
-

### Clarity Score
- Start of week: __/10
- End of week: __/10

---

## Freeze Moments

### When Did I Freeze?
-

### Why?
-

### How to Prevent Next Time?
-

---

## Best Moment This Week
**Problem:**
**Why:**

---

## Biggest Challenge
**Problem:**
**What Made It Hard:**
**How I Overcame It:**

---

## Meta-Learning
*What did I learn about HOW I learn?*

-

---

## Next Week Focus

### Pattern to Master
-

### Communication Goal
-

### Mindset Shift
-

---

## Statistics

- **Total problems solved:**
- **Patterns learned:**
- **Time spent coding:**
- **Mock interviews:**

---

## Evidence of Progress
*Compare to previous weeks - what improved?*

-

TEMPLATE

# Replace ${WEEK} with actual week number in the file
sed -i "s/\${WEEK}/$WEEK/g" "$REVIEW_FILE"
sed -i "s/\$(date +%B\\\\ %d,\\\\ %Y)/$(date +%B\ %d,\ %Y)/g" "$REVIEW_FILE"

echo "✓ Weekly review template created: $REVIEW_FILE"
echo "📊 Week $WEEK Review"
echo "📝 Fill out your reflection and learnings"
echo ""
echo "Location: $REVIEW_FILE"