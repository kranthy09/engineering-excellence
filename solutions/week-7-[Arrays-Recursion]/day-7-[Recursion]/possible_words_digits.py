"""
Possible words from digits

"""

keypad = ["", "", "abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"]


def get_possible_wordsUtil(i, arr, curr, result):
    # base case
    if i == len(arr):
        result.append("".join(curr))
        return

    if i <= 1:
        get_possible_wordsUtil(i+1, arr, curr, result)

    for ch in keypad[arr[i]]:
        curr.append(ch)
        get_possible_wordsUtil(i+1, arr, curr, result)
        curr.pop()


def get_possible_words(arr):
    curr = ""
    result = 0
    get_possible_wordsUtil(0, arr, curr, result)
    return result
