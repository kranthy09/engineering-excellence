"""
Rat in a maze

Use directional arrays for considering all directions

"""


def is_safe(i, j, maze):
    return i >= 0 and j >= 0 and i < len(maze) \
        and j < len(maze) and maze[i][j] == 1


def get_paths_util(i, j, maze, curr, result):
    # base
    if (i == len(maze)-1 and j == len(maze[0])-1):
        result.append("".join([val for val in curr]))
        return

    maze[i][j] = 0

    # Down
    if (is_safe(i+1, j, maze)):
        curr.append("D")
        get_paths_util(i+1, j, maze, curr, result)
        curr.pop()
    # Left
    if (is_safe(i-1, j, maze)):
        curr.append("L")
        get_paths_util(i-1, j, maze, curr, result)
        curr.pop()
    # Right
    if (is_safe(i, j+1, maze)):
        curr.append("R")
        get_paths_util(i, j+1, maze, curr, result)
        curr.pop()
    # Up
    if (is_safe(i, j-1, maze)):
        curr.append("U")
        get_paths_util(i, j-1, maze, curr, result)
        curr.pop()

    maze[i][j] = 1


def get_paths(maze):
    curr = []
    result = []
    get_paths_util(0, 0, maze, curr, result)

    return result
