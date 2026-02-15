#!/bin/bash

# Utility script to create a new problem file with a standard template
# Usage: touch_new <filename.py> [-t topic] [-d difficulty] [--tags tag1 tag2 ...]
#
# Examples:
#   touch_new maximum_of_k_distinct_numbers.py
#     -> Creates file in current directory, difficulty defaults to medium
#
#   touch_new two_sum.py -t arrays -d easy --tags hash-map
#     -> Creates file in solutions/arrays/, difficulty easy

SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
PROJECT_ROOT="$(dirname "$SCRIPT_DIR")"
SOLUTIONS_DIR="$PROJECT_ROOT/solutions"

usage() {
    echo "Usage: touch_new <filename.py> [-t topic] [-d difficulty] [--tags tag1 tag2 ...]"
    echo ""
    echo "Arguments:"
    echo "  filename.py   Problem filename in snake_case (e.g., two_sum.py)"
    echo ""
    echo "Options:"
    echo "  -t, --topic       Topic folder under solutions/ (optional, defaults to current directory)"
    echo "  -d, --difficulty   easy | medium | hard (optional, defaults to medium)"
    echo "  --tags             Space-separated tags for portfolio metadata (optional)"
    echo ""
    echo "Available topics:"
    ls -d "$SOLUTIONS_DIR"/*/ 2>/dev/null | xargs -I{} basename {} | grep -v __pycache__ | sort
    echo ""
    echo "Examples:"
    echo "  touch_new maximum_of_k_distinct_numbers.py"
    echo "  touch_new two_sum.py -d easy"
    echo "  touch_new two_sum.py -t arrays -d easy --tags hash-map two-pointers"
    exit 1
}

if [ $# -lt 1 ]; then
    usage
fi

FILENAME="$1"
shift

# Defaults
TOPIC=""
DIFFICULTY="medium"
TAGS=()

# Parse optional flags
while [ $# -gt 0 ]; do
    case "$1" in
        -t|--topic)
            TOPIC="$2"
            shift 2
            ;;
        -d|--difficulty)
            DIFFICULTY="$2"
            shift 2
            ;;
        --tags)
            shift
            while [ $# -gt 0 ] && [[ ! "$1" =~ ^- ]]; do
                TAGS+=("$1")
                shift
            done
            ;;
        *)
            echo "Error: Unknown option '$1'"
            usage
            ;;
    esac
done

# Validate difficulty
case "$DIFFICULTY" in
    easy|medium|hard) ;;
    *)
        echo "Error: difficulty must be one of: easy, medium, hard"
        exit 1
        ;;
esac

# Ensure filename ends with .py
if [[ "$FILENAME" != *.py ]]; then
    FILENAME="${FILENAME}.py"
fi

# Determine target directory
if [ -n "$TOPIC" ]; then
    TARGET_DIR="$SOLUTIONS_DIR/$TOPIC"
    if [ ! -d "$TARGET_DIR" ]; then
        echo "Topic '$TOPIC' does not exist. Creating directory: $TARGET_DIR"
        mkdir -p "$TARGET_DIR"
    fi
else
    TARGET_DIR="$(pwd)"
    # Try to infer topic from current directory relative to solutions/
    TOPIC=$(realpath --relative-to="$SOLUTIONS_DIR" "$TARGET_DIR" 2>/dev/null)
    if [[ "$TOPIC" == ..* ]]; then
        TOPIC=""
    fi
fi

FILEPATH="$TARGET_DIR/$FILENAME"

# Check if file already exists
if [ -f "$FILEPATH" ]; then
    echo "Error: File already exists: $FILEPATH"
    exit 1
fi

# Build display name from filename (strip .py, convert underscores to spaces, title case)
PROBLEM_NAME="${FILENAME%.py}"
DISPLAY_NAME=$(echo "$PROBLEM_NAME" | tr '_' ' ' | sed 's/\b\(.\)/\u\1/g')
DIFFICULTY_UPPER=$(echo "$DIFFICULTY" | sed 's/\b\(.\)/\u\1/g')
TAGS_STR=""
if [ ${#TAGS[@]} -gt 0 ]; then
    TAGS_STR=$(printf ", %s" "${TAGS[@]}")
    TAGS_STR="${TAGS_STR:2}"
fi

# Write the template
cat > "$FILEPATH" << TEMPLATE
"""
${DISPLAY_NAME} (${DIFFICULTY_UPPER})
@topic: ${TOPIC}
@difficulty: ${DIFFICULTY}
@tags: ${TAGS_STR}

i/o:
o/p:


Approaches:
1. Brute Force:
2. Expected:
"""


class Solution:
    def brute_force(self):
        """

        TC:
        AS:
        """
        pass

    def expected_solution(self):
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
TEMPLATE

echo "Created: $FILEPATH"
