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


IGNORE
# Pattern 01: Hash Map / Set Lookup

## At a Glance

| Item | Summary |
|---|---|
| Use when | You need fast lookup of previously seen values |
| Main tradeoff | `O(n)` extra space for faster runtime |
| Typical runtime | `O(n)` average |
| Typical structures | `set` for membership, `map` for counts/indices/state |
| Common prompts | Duplicate, frequency, first unique, pair sum |

## Diagram + Intuition

### Pattern Diagram

```text
Initialize hash structure:
  set() or map() based on need

for i, x in enumerate(items):
  derive query key (x, target - x, prefix, etc.)

  if key/info already in hash:
    use it -> record or return answer

  update hash with current element/state
    seen.add(x) or freq[x] += 1 or index[x] = i
```

### Mini Diagrams (Common Uses)

#### 1) Duplicate Detection (`set`)
```text
nums: [3, 1, 4, 1]
seen: {}

3 not in seen -> add 3
1 not in seen -> add 1
4 not in seen -> add 4
1 in seen     -> duplicate found (return True)
```

#### 2) Frequency Counting (`map`)
```text
chars:  a  b  a  c  a  b
freq : {a:1}
       {a:1,b:1}
       {a:2,b:1}
       {a:2,b:1,c:1}
       {a:3,b:1,c:1}
       {a:3,b:2,c:1}
```

#### 3) Two Sum Complement Lookup
```text
target = 9, nums = [2, 7, 11, 15]
index_of = {}

x=2, need=7  -> miss, store 2->0
x=7, need=2  -> hit (index 0), return [0,1]
```

#### 4) First Unique Character
```text
Pass 1: build counts
"leetcode" -> {l:1,e:3,t:1,c:1,o:1,d:1}

Pass 2: first count == 1
l is 1 -> answer index 0
```

#### 5) Prefix Sum + Hash Map (Subarray Sum = K)
```text
Running prefix: p
Need prior prefix: p - k

if (p - k) exists in map:
  subarray found ending here

map[p] += 1
```

#### 6) Anagram Check (Two Frequency Maps)
```text
s: "anagram" -> {a:3,n:1,g:1,r:1,m:1}
t: "nagaram" -> {n:1,a:3,g:1,r:1,m:1}

maps equal -> anagram
```

#### 7) Group Anagrams (Signature -> Bucket)
```text
word -> key(sorted(word)) -> group

"eat" -> "aet" -> ["eat"]
"tea" -> "aet" -> ["eat","tea"]
"tan" -> "ant" -> ["tan"]
```

#### 8) Sliding Window + Hash Counts
```text
expand right -> add s[r] count
while invalid:
  shrink left -> remove s[l] count
window valid -> update best answer
```

#### 9) Last Seen Index (Longest Unique Substring)
```text
map: char -> last index
left boundary moves to skip repeats

if c seen at j and j >= left:
  left = j + 1
update last_seen[c] = i
```

#### 10) Query-Then-Update Rule
```text
for each x:
  1) ask hash for needed info
  2) use result
  3) write current x/state

This order prevents self-reuse bugs.
```

### Read-the-Question Trigger Cues

- "duplicate", "frequency", "first unique", "pair sum"
- Brute force compares many pairs or rescans the same data.

### Intuition Anchor

- "I need memory of what I have seen so far."

### 3-Second Pattern Check

- Can I avoid repeated scans by storing `value -> count/index/state`?
- If I process left to right, can "seen so far" answer the current step?
- Is average `O(1)` lookup enough to reduce `O(n^2)` to `O(n)`?

## What This Pattern Solves

Use this pattern when you need fast lookups on previously seen elements.  
It is a default choice for:
- duplicate detection
- counting frequency
- reverse lookup (`value -> index`)
- complement matching (`target - x`)

## Recognition Signals

- Problem asks: "contains duplicate", "first unique", "count occurrences", "find pair summing to target".
- Brute force is `O(n^2)` from nested comparisons.
- A one-pass scan works if you remember prior elements.

## Core Intuition

Trade extra memory for speed.  
Instead of repeated searches, store facts in a hash structure:
- `set` for membership (`seen`)
- `map` for counts (`freq[x]`)
- `map` for metadata (`last_index[x]`, `first_position[x]`)

## Step-by-Step Method

1. Define exactly what each key/value means.
2. Traverse input once from left to right.
3. Query first, then update (unless the problem needs update first).
4. Keep the invariant clear: the table represents processed elements only.
5. Return early once the condition is satisfied (if allowed).

## Detailed Example (Two Sum)

**Input:** `nums = [2, 7, 11, 15], target = 9`

1. Start with empty map `index_of`.
2. Read `2`: need `7`, not found. Store `index_of[2] = 0`.
3. Read `7`: need `2`, found at index `0`.
4. Return `[0, 1]`.

This avoids checking all pairs and runs in one pass.

## Complexity

- Time: `O(n)` average case
- Space: `O(n)`

## Python Template

```python
def solve(nums, target):
    info = {}  # value -> index/count/metadata

    for i, x in enumerate(nums):
        need = target - x
        if need in info:
            return [info[need], i]
        info[x] = i

    return []
```

## Common Pitfalls

- Updating before checking can allow illegal reuse of the same element.
- Using `set` when multiplicity matters (you needed counts).
- Returning values instead of indices when the prompt asks indices.
- Overwriting useful state too early (for example, losing first index).

## Variations

- Frequency table with `dict`/`Counter` for anagrams, mode, grouping.
- Set-based dedupe when only presence matters.
- Prefix-sum hash map for subarray-sum problems.
- Character map for string window constraints.

## Interview Tips

- Start from brute force `O(n^2)`, then explain the repeated work.
- State key/value semantics clearly before coding.
- Mention average `O(1)` lookup/update and `O(n)` space tradeoff.

## Practice Problems

- Two Sum
- Contains Duplicate
- Valid Anagram
- First Unique Character in a String
- Subarray Sum Equals K
