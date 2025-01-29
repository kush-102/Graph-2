class Solution:
    # using tarjans algorithm
    def __init__(self):
        self.hash_map = (
            []
        )  # Adjacency list to keep track of the undirected graph connections
        self.result = []  # List to store final critical connections
        self.discovery = []  # Discovery time of nodes
        self.lowest = []  # Lowest discovery time reachable from each node
        self.time = 0  # Global timer for discovery times

    def criticalConnections(
        self, n: int, connections: list[list[int]]
    ) -> list[list[int]]:
        self.hash_map = [[] for _ in range(n)]
        self.discovery = [-1] * n
        self.lowest = [-1] * n

        # Build adjacency list
        for edge in connections:
            self.hash_map[edge[0]].append(edge[1])
            self.hash_map[edge[1]].append(edge[0])

        # Perform DFS to find critical connections
        self.dfs(0, -1)
        return self.result

    def dfs(self, v: int, parent: int):
        # If the node is already discovered, return
        if self.discovery[v] != -1:
            return

        # Assign discovery and lowest times
        self.discovery[v] = self.time
        self.lowest[v] = self.time
        self.time += 1

        # Visit all neighbors
        for neighbor in self.hash_map[v]:
            if neighbor == parent:
                continue  # Skip the edge back to the parent

            if self.discovery[neighbor] == -1:  # If neighbor is unvisited
                self.dfs(neighbor, v)

                # Check if the edge is a critical connection
                if self.lowest[neighbor] > self.discovery[v]:
                    self.result.append([v, neighbor])

                # Update the lowest discovery time for the current node
                self.lowest[v] = min(self.lowest[v], self.lowest[neighbor])
            else:
                # Update the lowest discovery time based on a back edge
                self.lowest[v] = min(self.lowest[v], self.discovery[neighbor])


# time and space complexity is O(V+E) where V is the number of vertices and E is the number of edges
