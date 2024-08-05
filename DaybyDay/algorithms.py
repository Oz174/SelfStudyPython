import heapq
from collections import deque

def binary_search(arr, target):
    low, high = 0, len(arr) - 1
    
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
            
    return -1  # Element not found


def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    
    return merge(left, right)

def merge(left, right):
    result = []
    i = j = 0
    
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    
    result.extend(left[i:])
    result.extend(right[j:])
    return result


def dfs(graph, start, visited=None):
    if visited is None:
        visited = set()
    visited.add(start)
    for neighbor in graph[start] - visited:
        dfs(graph, neighbor, visited)
    return visited


def bfs(graph, start):
    visited, queue = set(), deque([start])
    while queue:
        vertex = queue.popleft()
        if vertex not in visited:
            visited.add(vertex)
            queue.extend(graph[vertex] - visited)
    return visited


def dijkstra(graph, start):
    distances = {node: float('inf') for node in graph}
    distances[start] = 0
    priority_queue = [(0, start)]
    
    while priority_queue:
        current_distance, current_node = heapq.heappop(priority_queue)
        
        if current_distance > distances[current_node]:
            continue
        
        for neighbor, weight in graph[current_node].items():
            distance = current_distance + weight
            
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))
    
    return distances


def fibonacci(n):
    fib = [0, 1]
    for i in range(2, n + 1):
        fib.append(fib[i - 1] + fib[i - 2])
    return fib[n]


def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)


def kruskal(graph):
    """
    Kruskal's algorithm is a minimum-spanning-tree algorithm 
    which finds an edge of the least possible weight
    that connects any two trees in the forest.
    """
    parent = {}
    rank = {}

    def find(node):
        if parent[node] != node:
            parent[node] = find(parent[node])
        return parent[node]

    def union(node1, node2):
        root1 = find(node1)
        root2 = find(node2)
        if root1 != root2:
            if rank[root1] > rank[root2]:
                parent[root2] = root1
            else:
                parent[root1] = root2
                if rank[root1] == rank[root2]:
                    rank[root2] += 1

    for node in graph['vertices']:
        parent[node] = node
        rank[node] = 0

    minimum_spanning_tree = set()
    edges = list(graph['edges'])
    edges.sort()

    for edge in edges:
        _, node1, node2 = edge
        if find(node1) != find(node2):
            union(node1, node2)
            minimum_spanning_tree.add(edge)

    return minimum_spanning_tree




def astar(graph, start, goal):
    """
    A* algorithm is a graph traversal and path search algorithm,
    which is often used in computer science due to its completeness,
    optimality, and optimal efficiency
    """
    frontier = [(0, start)]
    came_from = {start: None}
    cost_so_far = {start: 0}

    while frontier:
        _, current_node = heapq.heappop(frontier)

        if current_node == goal:
            break

        for next_node, weight in graph[current_node].items():
            new_cost = cost_so_far[current_node] + weight
            if next_node not in cost_so_far or new_cost < cost_so_far[next_node]:
                cost_so_far[next_node] = new_cost
                priority = new_cost + heuristic(goal, next_node)
                heapq.heappush(frontier, (priority, next_node))
                came_from[next_node] = current_node

    return came_from, cost_so_far

def heuristic(goal, next_node):
    # Define your heuristic function here
    pass


def floyd_warshall(graph):
    """
    Floyd-Warshall algorithm is an algorithm for finding shortest paths in a weighted graph
    with positive or negative edge weights (but with no negative cycles).
    """

    dist = {v: {v: float('inf') for v in graph} for v in graph}
    for u in graph:
        dist[u][u] = 0
    for u in graph:
        for v in graph[u]:
            dist[u][v] = graph[u][v]
    for k in graph:
        for i in graph:
            for j in graph:
                dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])
    return dist




def topological_sort(graph):
    """
    Topological sorting for Directed Acyclic Graph (DAG) is a linear ordering of vertices
    such that for every directed edge uv, vertex u comes before v in the ordering.
    """
    in_degree = {node: 0 for node in graph}
    for node in graph:
        for neighbor in graph[node]:
            in_degree[neighbor] += 1
    
    queue = deque([node for node in graph if in_degree[node] == 0])
    topological_order = []
    
    while queue:
        node = queue.popleft()
        topological_order.append(node)
        for neighbor in graph[node]:
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                queue.append(neighbor)
    
    if len(topological_order) == len(graph):
        return topological_order
    else:
        raise ValueError("Graph is not acyclic")
    

def bellman_ford(graph, source):
    """
    Bellman-Ford algorithm computes shortest paths from a single source
    vertex to all other vertices in a weighted graph.
    """
    distances = {node: float('inf') for node in graph}
    distances[source] = 0

    for _ in range(len(graph) - 1):
        for u in graph:
            for v, weight in graph[u].items():
                if distances[u] + weight < distances[v]:
                    distances[v] = distances[u] + weight

    for u in graph:
        for v, weight in graph[u].items():
            if distances[u] + weight < distances[v]:
                raise ValueError("Graph contains negative weight cycle")

    return distances


def knapsack(weights, values, capacity):
    """
    The knapsack problem is a classic optimization problem
    that aims to maximize the total value of items
    in a knapsack without exceeding its capacity."""
    n = len(weights)
    dp = [[0 for _ in range(capacity + 1)] for _ in range(n + 1)]
    
    for i in range(1, n + 1):
        for w in range(1, capacity + 1):
            if weights[i - 1] <= w:
                dp[i][w] = max(values[i - 1] + dp[i - 1][w - weights[i - 1]], dp[i - 1][w])
