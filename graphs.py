

def count_paths_dp(maze):
    rows, cols = len(maze), len(maze[0])

    # Initialize a dp table with the same size as the maze
    dp = [[0] * cols for _ in range(rows)]

    # Starting point
    dp[0][0] = 1 if maze[0][0] == 0 else 0  # If the start is walkable, set it to 1

    # Fill the dp table
    for i in range(rows):
        for j in range(cols):
            # Skip the starting cell since we initialized it
            if i == 0 and j == 0:
                continue
            # If the cell is an obstacle, paths to it are 0
            if maze[i][j] == 1:
                dp[i][j] = 0
            else:
                # Sum paths from the top and left cells if within bounds
                if i > 0:
                    dp[i][j] += dp[i - 1][j]  # From top
                if j > 0:
                    dp[i][j] += dp[i][j - 1]  # From left

    # The value at the bottom-right corner is the total number of unique paths
    return dp[rows - 1][cols - 1]


from collections import deque

def count_paths_bfs(maze):
    rows, cols = len(maze), len(maze[0])
    queue = deque([(0, 0)])  # Start from the top-left corner
    paths = 0

    while queue:
        x, y = queue.popleft()

        # If we reach the end cell, increment path count
        if x == rows - 1 and y == cols - 1:
            paths += 1
            continue

        # Explore all four directions
        for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            nx, ny = x + dx, y + dy
            # Check if the next cell is within bounds and walkable
            if 0 <= nx < rows and 0 <= ny < cols and maze[nx][ny] == 0:
                # Temporarily mark as visited by setting to 1 to avoid revisiting
                maze[x][y] = 1
                queue.append((nx, ny))
                # Restore original value after processing for backtracking
                maze[x][y] = 0

    return paths


class Graph:
    def __init__(self, num_vertices):
        self.num_vertices = num_vertices
        self.adj_matrix = [[0] * num_vertices for _ in range(num_vertices)]

    def add_edge(self, u, v):
        self.adj_matrix[u][v] = 1
        self.adj_matrix[v][u] = 1  # For undirected graph

    def display(self):
        for row in self.adj_matrix:
            print(row)

# Example usage
g = Graph(5)
g.add_edge(0, 1)
g.add_edge(0, 2)
g.add_edge(1, 2)
g.add_edge(1, 3)
g.display()

from collections import deque

def dfs(graph, start, visited=None):
    if visited is None:
        visited = set()
    visited.add(start)
    print(start, end=' ')

    for neighbor in graph[start]:
        if neighbor not in visited:
            dfs(graph, neighbor, visited)


def bfs(graph, start):
    visited = set()
    queue = deque([start])
    visited.add(start)

    while queue:
        vertex = queue.popleft()
        print(vertex, end=' ')

        for neighbor in graph[vertex]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)

graph = {
    0: [1, 2],
    1: [0, 2, 3],
    2: [0, 1, 4],
    3: [1, 4],
    4: [2, 3]
}
dfs(graph, 0)

bfs(graph, 0)


# Dijkstra’s Algorithm -shortest path
"""The algorithm maintains a set of visited vertices and a set of unvisited vertices. 
It starts at the source vertex and iteratively selects the unvisited vertex with the smallest 
tentative distance from the source. It then visits the neighbors of this vertex and updates their 
tentative distances if a shorter path is found. This process continues until the destination vertex 
is reached, or all reachable vertices have been visited."""

# Mark the source node with a current distance of 0 and the rest with infinity.
# Set the non-visited node with the smallest current distance as the current node.
# For each neighbor, N of the current node adds the current distance of the adjacent node with the weight of the edge
# connecting 0->1. If it is smaller than the current distance of Node, set it as the new current distance of N.
# Mark the current node 1 as visited.
# Go to step 2 if there are any nodes are unvisited.

graph_matrix = [[0, 0, 3, 4, 4, 0, 0],
 [0, 0, 2, 0, 0, 2, 0],
 [3, 2, 0, 0, 4, 5, 0],
 [4, 0, 0, 0, 2, 0, 0],
 [4, 0, 4, 2, 0, 0, 5],
 [0, 2, 5, 0, 0, 0, 5],
 [0, 0, 0, 0, 5, 5, 0]]

import heapq
def dijkstra_matrix(graph, start):

    n = len(graph)
    distances = {vertex: float('inf') for vertex in range(n)}

    distances[start] = 0
    pqueue = [(0, start)]

    while pqueue:
        current_dist, current_vertex = heapq.heappop(pqueue)

        if current_dist > distances[current_vertex]:
            continue

        for neighbour in range(n):
            weight = graph[current_vertex][neighbour]

            if weight == 0:
                continue

            total_dist = current_dist + weight

            if total_dist < distances[neighbour]:
                distances[neighbour] = total_dist

                heapq.heappush(pqueue, (total_dist, neighbour))

    return distances


dijkstra_matrix(graph_matrix, 3)

dijkstra_matrix(graph_matrix, 0)

# Bellman-Ford
# Bellman-Ford Algorithm implementation in Python
def bellman_ford(graph, num_vertices, start):
    distances = {i: float('infinity') for i in range(num_vertices)}
    distances[start] = 0

    for _ in range(num_vertices - 1):
        for u in range(num_vertices):
            for v, weight in graph[u].items():
                if distances[u] + weight < distances[v]:
                    distances[v] = distances[u] + weight

    for u in range(num_vertices):
        for v, weight in graph[u].items():
            if distances[u] + weight < distances[v]:
                raise ValueError("Graph contains a negative weight cycle")

    return distances


# Example usage
graph = {
    0: {1: 1, 2: 4},
    1: {2: 2, 3: 5},
    2: {3: 1},
    3: {4: 3},
    4: {2: 6}
}
print(bellman_ford(graph, 5, 0))

import heapq

def dijkstra(graph, start):

    distances = {vertex: float('inf') for vertex in graph}
    distances[start] = 0
    pqueue = [(0, start)]

    while pqueue:

        dist_to_v, vertex = heapq.heappop(pqueue)

        if dist_to_v > distances[vertex]:
            continue

        for neighbour, weight in graph[vertex].items():

            distance = dist_to_v + weight

            if distance < distances[neighbour]:
                distances[neighbour] = distance
                heapq.heappush(pqueue, (distance, neighbour))

    return distances


# Example usage
graph = {
    0: {1: 1, 2: 4},
    1: {0: 1, 2: 2, 3: 5},
    2: {0: 4, 1: 2, 4: 1},
    3: {1: 5, 4: 3},
    4: {2: 1, 3: 3}
}
print(dijkstra(graph, 1))


graph = {
   "A": {"B": 3, "C": 3},
   "B": {"A": 3, "D": 3.5, "E": 2.8},
   "C": {"A": 3, "E": 2.8, "F": 3.5},
   "D": {"B": 3.5, "E": 3.1, "G": 10},
   "E": {"B": 2.8, "C": 2.8, "D": 3.1, "G": 7},
   "F": {"G": 2.5, "C": 3.5},
   "G": {"F": 2.5, "E": 7, "D": 10},
}

dijkstra(graph,'B')

class EdgeNode:
    def __init__(self, vertex, weight=1, next_edge=None):
        self.vertex = vertex  # The adjacent vertex
        self.weight = weight  # Weight of the edge
        self.next_edge = next_edge  # Pointer to the next edge node

class VertexNode:
    def __init__(self, vertex):
        self.vertex = vertex  # The vertex ID or label
        self.adj_list = None  # Pointer to the linked list of edges

class Graph:
    def __init__(self, num_vertices):
        self.num_vertices = num_vertices
        self.vertices = {}  # Dictionary to store vertices

    def add_vertex(self, vertex):
        if vertex not in self.vertices:
            self.vertices[vertex] = VertexNode(vertex)

    def add_edge(self, start, end, weight=1):
        # Ensure both start and end vertices are in the graph
        if start not in self.vertices:
            self.add_vertex(start)
        if end not in self.vertices:
            self.add_vertex(end)

        # Add the edge to the start vertex's adjacency list
        new_edge = EdgeNode(end, weight, self.vertices[start].adj_list)
        self.vertices[start].adj_list = new_edge

        # Uncomment the next two lines for an undirected graph
        # reverse_edge = EdgeNode(start, weight, self.vertices[end].adj_list)
        # self.vertices[end].adj_list = reverse_edge

    def display_graph(self):
        for vertex in self.vertices:
            print(f"Vertex {vertex}:", end="")
            current = self.vertices[vertex].adj_list
            while current:
                print(f" -> {current.vertex}(weight={current.weight})", end="")
                current = current.next_edge
            print()

# Create a graph with 5 vertices
graph = Graph(5)

# Add edges
graph.add_edge(0, 1, weight=5)
graph.add_edge(0, 4, weight=1)
graph.add_edge(1, 3, weight=2)
graph.add_edge(1, 2, weight=3)
graph.add_edge(3, 4, weight=4)

# Display the graph
graph.display_graph()





