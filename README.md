# Patterns to Ace Any Coding Interview Question

This repository is a practical index of the most important coding interview patterns.
If you can identify which pattern a problem belongs to, solving becomes much faster and more reliable.

## Detailed Pattern Guides

For deep dives (how to recognize, solve, implement, and avoid pitfalls), use:

- [patterns/README.md](./patterns/README.md)
- [patterns/INTUITION-DIAGRAMS.md](./patterns/INTUITION-DIAGRAMS.md)
- [patterns/questions/README.md](./patterns/questions/README.md)
- [dsa/deep-problem-solving-foundations.md](./dsa/deep-problem-solving-foundations.md)
- Direct folder: [`patterns/`](./patterns/)

## Master Pattern List

| # | Pattern | Use It When You See | Common Problems |
|---|---|---|---|
| 1 | Hash Map / Set Lookup | Fast membership, counting, duplicate detection | Two Sum, Contains Duplicate, Valid Anagram |
| 2 | Two Pointers | Sorted arrays, pair comparisons, in-place array edits | 3Sum, Container With Most Water, Remove Duplicates |
| 3 | Sliding Window (Fixed) | Fixed-size subarray/substring optimization | Max Sum Subarray of Size K, Averages of Subarrays |
| 4 | Sliding Window (Variable) | Longest/shortest valid window under constraints | Longest Substring Without Repeating Characters |
| 5 | Prefix Sum | Frequent range sum or balance checks | Subarray Sum Equals K, Product Except Self (variant thinking) |
| 6 | Binary Search (Index) | Sorted/search space halving | Search in Rotated Array, First Bad Version |
| 7 | Binary Search on Answer | Min/max feasible value with monotonic condition | Koko Eating Bananas, Capacity To Ship Packages |
| 8 | Sort + Scan | Need global ordering before linear logic | Merge Intervals, Meeting Rooms, Non-overlapping Intervals |
| 9 | Greedy | Local best choice proves global best | Jump Game, Gas Station, Task Scheduling variants |
| 10 | Monotonic Stack | Next greater/smaller element and range boundaries | Daily Temperatures, Largest Rectangle in Histogram |
| 11 | Monotonic Queue / Deque | Sliding window min/max in O(n) | Sliding Window Maximum |
| 12 | Top K with Heap | Need k largest/smallest/frequent quickly | Top K Frequent Elements, K Closest Points |
| 13 | K-Way Merge (Heap) | Merge many sorted lists/streams | Merge K Sorted Lists, Smallest Range Covering K Lists |
| 14 | Fast & Slow Pointers | Cycle detection, middle node, linked list phases | Linked List Cycle, Happy Number |
| 15 | Linked List Reversal / In-place Ops | Pointer rewiring in lists | Reverse Linked List, Reverse Nodes in K-Group |
| 16 | Cyclic Sort | Arrays containing range 1..n or 0..n with missing/duplicate | Missing Number, Find All Duplicates in an Array |
| 17 | Intervals Line Sweep | Start/end events over timeline | Meeting Rooms II, Number of Airplanes in the Sky |
| 18 | Matrix Traversal | Grid BFS/DFS, boundary/visited control | Number of Islands, Rotting Oranges |
| 19 | Tree DFS (Pre/In/Post) | Path/state recursion on trees | Diameter of Binary Tree, Path Sum |
| 20 | Tree BFS (Level Order) | Per-level processing or shortest steps in unweighted trees | Binary Tree Level Order Traversal |
| 21 | Binary Search Tree Rules | Ordered tree constraints and range checks | Validate BST, Kth Smallest in BST |
| 22 | Backtracking | Build combinations/permutations with undo step | Subsets, Permutations, N-Queens, Word Search |
| 23 | Trie (Prefix Tree) | Prefix lookups/autocomplete/word dictionary | Implement Trie, Word Search II |
| 24 | Graph BFS/DFS | Connectivity/components/reachability | Clone Graph, Number of Connected Components |
| 25 | Topological Sort | DAG ordering / dependency resolution | Course Schedule, Alien Dictionary |
| 26 | Union-Find (DSU) | Dynamic connectivity, cycle detection in undirected graph | Redundant Connection, Number of Provinces |
| 27 | Shortest Path (Dijkstra / 0-1 BFS) | Weighted graph shortest distance | Network Delay Time, Cheapest Flights Within K Stops |
| 28 | Dynamic Programming (1D) | Optimal substructure over index/state | House Robber, Climbing Stairs, Decode Ways |
| 29 | Dynamic Programming (2D) | Grid/string/state transition tables | LCS, Edit Distance, Unique Paths |
| 30 | Knapsack DP | Pick/skip with capacity/constraint | 0/1 Knapsack, Partition Equal Subset Sum |
| 31 | Interval DP / Partition DP | Split range into subproblems | Burst Balloons, Matrix Chain Multiplication |
| 32 | Bit Manipulation | XOR tricks, compact state, bit counting | Single Number, Counting Bits, Subset generation |
| 33 | Math / Number Theory | GCD, modular arithmetic, primes, combinatorics | Rotate Array (mod), Pow(x, n), GCD problems |
| 34 | Design Data Structures | O(1) operation constraints and API behavior | LRU Cache, Min Stack, TimeMap |
| 35 | Segment Tree / Fenwick Tree | Dynamic range query + updates | Range Sum Query Mutable, Count of Smaller Numbers |
| 36 | Meet in the Middle | n around 30-45 with subset split and combine | Closest Subsequence Sum, Partition Array Into Two Arrays to Minimize Sum Difference |
| 37 | Bitmask DP / State Compression DP | Small n (<=20) with subset-state transitions | Shortest Path Visiting All Nodes, Assignment Problem |
| 38 | Multi-source BFS | Nearest-source shortest path in unweighted graph/grid | 01 Matrix, Rotting Oranges |
| 39 | State-space BFS | Shortest path where node must include extra state | Open the Lock, Shortest Path to Get All Keys |
| 40 | Minimum Spanning Tree (Kruskal / Prim) | Need minimum total cost to connect all nodes | Min Cost to Connect All Points, Connecting Cities With Minimum Cost |
| 41 | Negative-Weight Shortest Path (Bellman-Ford / Floyd-Warshall) | Negative edges, cycle detection, or all-pairs shortest paths | Cheapest Flights Within K Stops (BF variant), Arbitrage Detection |
| 42 | SCC / Bridges / Articulation Points | Find critical graph structure and vulnerability points | Critical Connections in a Network, Articulation Points |
| 43 | Tree Rerooting DP | Need per-node answer when each node is treated as root | Sum of Distances in Tree, Tree Distances II |
| 44 | Binary Lifting (LCA / Kth Ancestor) | Many ancestor/jump/LCA queries on static tree | Kth Ancestor of a Tree Node, LCA Queries |
| 45 | Advanced String Patterns (KMP / Z / Rabin-Karp / Manacher) | Linear-time substring matching and palindrome preprocessing | Implement strStr, Longest Palindromic Substring |

## Pattern Recognition Checklist

Use this quick diagnostic to classify a new problem:

1. Is there repeated range query logic? Think `prefix sum`, `segment tree`, or `Fenwick tree`.
2. Is it asking for longest/shortest valid substring/subarray? Think `sliding window`.
3. Is data sorted or sortable and you need pair/group logic? Think `two pointers` or `sort + scan`.
4. Is there a monotonic feasibility condition over answer value? Think `binary search on answer`.
5. Is this "choose / skip / maximize / count ways"? Think `dynamic programming`.
6. Is it about dependencies/order constraints? Think `topological sort`.
7. Is it connectivity across merges? Think `union-find`.
8. Is it next greater/smaller or nearest boundary? Think `monotonic stack`.

## High-Impact Practice Order

If you want the fastest interview return-on-time:

1. Hashing + Arrays
2. Two Pointers + Sliding Window
3. Binary Search + Intervals
4. Linked List + Stack/Queue + Heap
5. Trees (DFS/BFS/BST)
6. Graphs (BFS/DFS/Topo/Union-Find)
7. Dynamic Programming (1D -> 2D -> Knapsack/Advanced)
8. Advanced Structures (Trie, Segment Tree/Fenwick)

## Interview Execution Framework

For each question:

1. Classify the pattern in under 60 seconds.
2. State brute force first, then optimize.
3. Write down constraints and edge cases.
4. Pick data structure intentionally.
5. Dry run on one normal and one edge case.
6. Discuss time and space complexity clearly.

## Goal

Mastering these patterns lets you map unfamiliar questions to familiar solution shapes.
That is the core skill behind solving "new" interview questions quickly.
