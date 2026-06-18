class Solution:
  def countComponents(self, n: int, edges: List[List[int]]) -> int:
    graph = self.create_graph(n, edges)
    visited = set()
    count = 0
    for node in graph:
      if self.traverse_graph(node, graph, visited) == True:
        count += 1
    return count

  def traverse_graph(self, node, graph, visited):
    if node in visited:
      return False
    visited.add(node)

    for neighbor in graph[node]:
      self.traverse_graph(neighbor, graph, visited)

    return True

  def create_graph(self, n, edges):
    graph = {}
    for x in range(n):
      graph[x] = []

    for a, b in edges:
      graph[a].append(b)
      graph[b].append(a)
    return graph