# Graph Leetcode

#### Many interesting algorithms; Plus the time complexity analysis always makes the tutorial worth reading.

---

[Leetcode Link of Official Graph Problems Set](https://leetcode.com/explore/learn/card/graph/)

---

## [Union-Find](https://leetcode.com/explore/learn/card/graph/618/disjoint-set/3881/)

<img src="../assets/Union-Find%20time%20complexity.png" width="800">

- [1202 | Smallest String With Swaps \*](https://leetcode.com/problems/smallest-string-with-swaps/)

  - [solution](../../Solutions/1202_Smallest%20String%20With%20Swaps.py)

- [399 | Evaluate Division \*\*\*\*](https://leetcode.com/problems/evaluate-division/)

  - [solution](../../Solutions/399_Evaluate%20Division.py)

- [1168 | Optimize Water Distribution in a Village \*\*\*\*](https://leetcode.com/problems/optimize-water-distribution-in-a-village/)

---

## [DFS](https://leetcode.com/explore/learn/card/graph/619/depth-first-search-in-graph/)

- Find all vertices in a graph.
- Find all paths between two vertices in a graph.

In Graph theory, the depth-first search algorithm (abbreviated as DFS) is mainly used to:

- Traverse all vertices in a “graph”;

<img src="../assets/DFS%20time%20complexity%201.png" width="900">

- Traverse all paths between any two vertices in a “graph”.

<img src="../assets/DFS%20time%20complexity%202.png" width="900">

### Problems:

- [133 | Clone Graph \*\*](https://leetcode.com/problems/clone-graph/)

  - [solution](../../Solutions/133_Clone%20Graph.py)

- [332 | Reconstruct Itinerary \*\*\*](https://leetcode.com/problems/reconstruct-itinerary/)

  - [solution](../../Solutions/332_Reconstruct%20Itinerary.py)

---

## [BFS](https://leetcode.com/explore/learn/card/graph/620/breadth-first-search-in-graph/)

- Efficiently find the shortest path between two vertices in a “graph” where all edges have equal and positive weights.
- The “breadth-first search” algorithm, in most cases, can find the shortest path without traversing all paths. This is because when using "breadth-first search", as soon as a path between the source vertex and target vertex is found, it is guaranteed to be the shortest path between the two nodes.

In Graph theory, the primary use cases of the “breadth-first search” (“BFS”) algorithm are:

- Traversing all vertices in the “graph”;

<img src="../assets/BFS%20complexity%201.png" width="900">

- Finding the shortest path between two vertices in a graph where all edges have equal and positive weights.

<img src="../assets/BFS%20complexity%202.png" width="900">

### Problems:

- [1091 | Shortest Path in Binary Matrix \*](https://leetcode.com/problems/shortest-path-in-binary-matrix/)

  - [solution](../../Solutions/1091_Shortest%20Path%20in%20Binary%20Matrix.py)

- [994 | Rotting Oranges \*](https://leetcode.com/problems/rotting-oranges/)

  - [solution](../../Solutions/994_Rotting%20Oranges.py)

---

## [Algorithms to Construct Minimum Spanning Tree](https://leetcode.com/explore/learn/card/graph/621/algorithms-to-construct-minimum-spanning-tree/)

[Another tutorial except for leetcode](https://www.hackerearth.com/practice/algorithms/graphs/minimum-spanning-tree/tutorial/)

- A spanning tree is a connected subgraph in an undirected graph where all vertices are connected with the minimum number of edges.
- A minimum spanning tree is a spanning tree with the minimum possible total edge weight in a “weighted undirected graph”.

#### [Kruskal's Algorithm](https://leetcode.com/explore/learn/card/graph/621/algorithms-to-construct-minimum-spanning-tree/3856/)

- Implementation Details:
  - Use Union-Find structure to see if two vertices of the edge we intend to add are already in one cluster.
  - Use Heap / Sorted List to determine the order of adding edges.

<img src="../assets/Kruskal's%20Algo%20complexity.png" width="900">

#### [Prim's Algorithm](https://leetcode.com/explore/learn/card/graph/621/algorithms-to-construct-minimum-spanning-tree/3859/)

- Implementation Details:
  - Use a set to storage the vertices we have already added into the cluster. (When add a vertex into cluster / set, add all valid adjacent vertices / edges into Heap.)
  - Use Heap to determine which vertex to add at each iteration.

<img src="../assets/Prim's%20Algo%20complexity.png" width="900">

#### The difference between the “Kruskal’s algorithm” and the “Prim’s algorithm”

`“Kruskal’s algorithm” expands the “minimum spanning tree” by adding edges. Whereas “Prim’s algorithm” expands the “minimum spanning tree” by adding vertices.`

This is obvious, but it kind of explains many phenomenon behind these two algorithms.

### Problems:

- [1584 | Min Cost to Connect All Points \*\*](https://leetcode.com/problems/min-cost-to-connect-all-points/)

  - [solution](../../Solutions/1584_Min%20Cost%20to%20Connect%20All%20Points.py)

---

## [Single Source Shortest Path Algorithm](https://leetcode.com/explore/learn/card/graph/622/single-source-shortest-path-algorithm/)

- We used the “breadth-first search” algorithm to find the “shortest path” between two vertices. However, the “breadth-first search” algorithm can only solve the “shortest path” problem in “unweighted graphs”.
- The main focus of this chapter is to solve such “single source shortest path” problems. Given the starting vertex, find the “shortest path” to any of the vertices in a weighted graph. Once we solve this, we can easily acquire the shortest paths between the starting vertex and a given target vertex.

In this chapter, we will learn two “single source shortest path” algorithms:

- Dijkstra’s algorithm
- Bellman-Ford algorithm
- “Dijkstra's algorithm” can only be used to solve the “single source shortest path” problem in a graph with non-negative weights.
- “Bellman-Ford algorithm”, on the other hand, can solve the “single-source shortest path” in a weighted directed graph with any weights, including, of course, negative weights.
- One of the core of “single source shortest path” algorithms is `relaxation` operation.

#### [Dijkstra's Algorithm](https://leetcode.com/explore/learn/card/graph/622/single-source-shortest-path-algorithm/3862/)

<img src="../assets/Dijkstra's%20Algorithm%20complexity.png" width="900">

#### [Bellman Ford Algorithm](https://leetcode.com/explore/learn/card/graph/622/single-source-shortest-path-algorithm/3864/)

The Bellman Ford Algorithm is inspired by a Dynamic Programming way. It is worthwhile to read it from leetcode tutorial.
Surely makes it easier to understand.

<img src="../assets/Bellman%20Ford%20Algo%20complexity.png" width="900">

### Problems:

- [743 | Network Delay Time \*\*\*](https://leetcode.com/problems/network-delay-time/)

  - [solution](../../Solutions/743_Network%20Delay%20Time.py)

- [787 | Cheapest Flights Within K Stops \*\*\*](https://leetcode.com/problems/cheapest-flights-within-k-stops/)

  - [solution](../../Solutions/787_Cheapest%20Flights%20Within%20K%20Stops.py)

---

## [Kahn's Algorithm for Topological Sorting](https://leetcode.com/explore/learn/card/graph/623/kahns-algorithm-for-topological-sorting/3886/)

- “Topological sorting” only works with graphs that are directed and acyclic.

<img src="../assets/Kahn's%20Algorithm%20Topological%20Sort%20complexity.png" width="900">

### Problems:

- [210 | Course Schedule II \*\*](https://leetcode.com/problems/course-schedule-ii/)

  - [solution](../../Solutions/210_Course%20Schedule%20II.py)

- [310 | Minimum Height Trees \*\*\*](https://leetcode.com/problems/minimum-height-trees/)

  - [solution](../../Solutions/310_Minimum%20Height%20Trees.py)
