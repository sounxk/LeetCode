class Solution:
  def countRestrictedPaths(self, n: int, edges: List[List[int]]) -> int:
    graph = [[] for _ in range(n)]

    for u, v, w in edges:
      graph[u - 1].append((v - 1, w))
      graph[v - 1].append((u - 1, w))

    return self.dijkstra(graph, 0, n - 1)

  def dijkstra(self, graph: List[List[Tuple[int, int]]], src: int, dst: int) -> int:
    kMod = 10**9 + 7
    # ways[i] := # of restricted path from i -> n
    ways = [0] * len(graph)
    # dist[i] := distanceToLastNode(i)
    dist = [math.inf] * len(graph)

    ways[dst] = 1
    dist[dst] = 0
    minHeap = [(dist[dst], dst)]  # (d, u)

    while minHeap:
      d, u = heapq.heappop(minHeap)
      if d > dist[u]:
        continue
      for v, w in graph[u]:
        if d + w < dist[v]:
          dist[v] = d + w
          heapq.heappush(minHeap, (dist[v], v))
        if dist[v] < dist[u]:
          ways[u] += ways[v]
          ways[u] %= kMod

    return ways[src]
