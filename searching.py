matrix = [[1,1,0,1,0,0,0,1,1,0],
          [1,0,1,1,0,0,0,1,0,0],
          [0,0,0,0,0,0,1,0,0,0],
          [1,0,0,1,0,0,1,1,0,0],
          [1,0,1,1,0,1,0,0,0,0],
          [1,0,0,0,1,1,0,0,0,0],
          [0,0,0,0,1,1,0,0,1,1],
          [0,0,0,1,1,0,0,0,0,0]]

from collections import deque

def breadth_first_search(row, col, matrix, visited):

    n_rows = len(matrix)
    n_cols = len(matrix[0])
    offsets = [(0, 1), (0, -1), (-1, 0), (1, 0)]
    visited[row][col] = 1
    to_visit = deque([(row, col)])

    while to_visit:
        y, x = to_visit.popleft()

        for dy, dx in offsets:
            new_row = y + dy
            new_col = x + dx
            if 0 <= new_row < n_rows and 0 <= new_col < n_cols and visited[new_row][new_col] == 0 and matrix[new_row][new_col] == 1:

                visited[new_row][new_col] = 1
                to_visit.append((new_row, new_col))

    pass


def island_search_bfs(matrix):
    n_rows = len(matrix)
    n_cols = len(matrix[0])
    visited = [[0]*n_cols for _ in range(n_rows)]

    island_count = 0
    for i in range(n_rows):
        for j in range(n_cols):
            if matrix[i][j] == 1 and visited[i][j] == 0:
                island_count += 1
                breadth_first_search(i, j, matrix, visited)

    return island_count

island_search_bfs(matrix)

def depth_first_search(row, col, matrix, visited):

    if row < 0 or row >= len(matrix) or col < 0 or col >= len(matrix[0]) or visited[row][col]==1 or matrix[row][col] ==0:
        return

    visited[row][col] = 1
    depth_first_search(row+1, col, matrix, visited)
    depth_first_search(row, col+1, matrix, visited)
    depth_first_search(row - 1, col, matrix, visited)
    depth_first_search(row, col - 1, matrix, visited)


def island_search_dfs(matrix):
    n_rows = len(matrix)
    n_cols = len(matrix[0])
    visited = [[0]*n_cols for _ in range(n_rows)]

    island_count = 0
    for i in range(n_rows):
        for j in range(n_cols):
            if matrix[i][j] == 1 and visited[i][j] == 0:
                island_count += 1
                depth_first_search(i, j, matrix, visited)

    return island_count

island_search_dfs(matrix)

def binarySearch(array, x, low, high):

    if high >= low:

        mid =  (high + low) // 2

        # If found at mid, then return it
        if array[mid] == x:
            return mid

        # Search the left half
        elif array[mid] > x:
            return binarySearch(array, x, low, mid-1)

        # Search the right half
        else:
            return binarySearch(array, x, mid + 1, high)

    else:
        return -1



