"""
Tower of Hanoi

i/o:
o/p:

i/o:
o/p:

Approaches:
1. Brute Force:

"""


def tower_of_hanoi(n, A, C, B):

    # base ?
    if n <= 0:
        return 0
    result = tower_of_hanoi(n-1, A, B, C)
    result += 1
    result += tower_of_hanoi(n-1, B, C, A)

    return result


if __name__ == "__main__":
    Ns = [
        3, 7
    ]
    A = ""
    B = ""
    C = ""

    print("******Recursive******")
    for n in Ns:
        print(tower_of_hanoi(n, A, C, B))
