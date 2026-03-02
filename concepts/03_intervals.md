# Intervals: A Deep Dive

---

## 1. What Is It? (Definition & Core Components)

An **interval** is a contiguous range defined by a **start** and an **end** point, representing everything between those two boundaries.

```
Interval [2, 7]:

0    1    2    3    4    5    6    7    8    9
|    |    |════════════════════════|    |    |
          start                  end
```

**Core components:**

- **Start point** — where the interval begins (inclusive usually)
- **End point** — where the interval ends (inclusive or exclusive, context-dependent)
- **Boundary type** — open `(a, b)`, closed `[a, b]`, or half-open `[a, b)`
- **A collection of intervals** — almost all problems involve multiple intervals and their relationships
- **A sorted order** — nearly every algorithm begins by sorting intervals, almost always by start point

---

## 2. The Anatomy of Two Intervals

Before solving any problem, you must recognize every way two intervals can relate. There are exactly **6 relationships**:

```
A: [════]
B:          [════]    1. DISJOINT (B after A)   — no overlap, gap between them

A:          [════]
B: [════]             2. DISJOINT (A after B)   — same, reversed

A: [════]
B:      [════]        3. PARTIAL OVERLAP        — B starts inside A, ends outside

A:     [════]
B: [════]             4. PARTIAL OVERLAP        — A starts inside B, ends outside

A: [══════════]
B:    [════]          5. CONTAINMENT            — B entirely inside A

A:    [════]
B: [══════════]       6. CONTAINMENT            — A entirely inside B
```

**The unifying test:** Two intervals `[a, b]` and `[c, d]` overlap if and only if:
```
a <= d  AND  c <= b
```
They are disjoint if: `b < c` OR `d < a` (one ends before the other starts).

This single condition is the engine behind every interval algorithm.

---

## 3. The Physical Analogy: Meetings on a Calendar

Imagine a day planner with colored blocks representing meetings:

```
9am  10am  11am  12pm  1pm   2pm   3pm   4pm   5pm
 |    |     |     |     |     |     |     |     |
 [══Alice══]
       [══Bob═══════]
                   [══Carol══]
                         [══Dave══════════]
```

Now questions become intuitive:
- **Merge overlapping meetings** → which blocks can be combined?
- **Find free slots** → gaps between merged blocks
- **How many rooms needed?** → max overlapping blocks at any point
- **Does Alice conflict with Bob?** → do their intervals overlap?

Every interval algorithm is just a formalization of this calendar reasoning.

---

## 4. Sorting: The Universal First Step

Almost every interval problem starts with **sorting by start time**. Why?

```
UNSORTED:  [3,6]  [1,4]  [8,10]  [2,5]  [7,9]

You can't easily see what overlaps what.

SORTED:    [1,4]  [2,5]  [3,6]  [7,9]  [8,10]
                  ↑ must check against [1,4]
                         ↑ must check against [2,5]
                                ↑ gap! new group starts
                                       ↑ must check against [7,9]
```

Sorting creates a **left-to-right sweep guarantee**: if you're processing interval `i`, all intervals `j > i` start at or after `i`'s start. This means:
- You only need to compare each interval to its **immediate predecessor** (or a running boundary), not every other interval
- Overlaps, if they exist, are **adjacent after sorting**

This transforms an O(n²) comparison problem into O(n log n) — the sort dominates, the scan is O(n).

---

## 5. The Core Algorithm: Merging Intervals

**Problem:** Given `[[1,4],[2,5],[3,6],[7,9],[8,10]]`, merge all overlapping intervals.

**Algorithm:**
```
1. Sort by start: [[1,4],[2,5],[3,6],[7,9],[8,10]]
2. Initialize result with first interval: result = [[1,4]]
3. For each remaining interval:
   └── Does it overlap with result's LAST interval?
       ├── YES → merge: extend last interval's end if needed
       └── NO  → push as new separate interval
```

**Step-by-step:**

```
Sorted: [1,4]  [2,5]  [3,6]  [7,9]  [8,10]

result = [[1,4]]

[2,5]:  2 <= 4? YES → merge → last = [1, max(4,5)] = [1,5]
        result = [[1,5]]

[3,6]:  3 <= 5? YES → merge → last = [1, max(5,6)] = [1,6]
        result = [[1,6]]

[7,9]:  7 <= 6? NO  → new interval
        result = [[1,6],[7,9]]

[8,10]: 8 <= 9? YES → merge → last = [7, max(9,10)] = [7,10]
        result = [[1,6],[7,10]]

Answer: [[1,6],[7,10]]
```

```
Before:  [1,4] [2,5] [3,6]        [7,9][8,10]
          ──────────────               ──────
After:   [1,           6]         [7,         10]
```

**The merge condition:** `current.start <= last.end`
**The merge action:** `last.end = max(last.end, current.end)` — take the wider end.

---

## 6. The Core Algorithm: Interval Insertion

**Problem:** Insert `[3, 8]` into sorted non-overlapping intervals `[[1,2],[5,6],[7,9],[10,12]]`.

This is merging but with a twist: find where the new interval goes, absorb all overlaps, stitch back together.

```
Original: [1,2]  [5,6]  [7,9]  [10,12]
Insert:          [3,        8]

Phase 1 — collect all intervals BEFORE new one (end < new.start):
  [1,2].end=2 < 3=new.start → add to result as-is
  [5,6].end=6 < 3? NO → stop

Phase 2 — merge all OVERLAPPING intervals (start <= new.end):
  [5,6]:  5 <= 8? YES → expand new: [min(3,5), max(8,6)] = [3,8]
  [7,9]:  7 <= 8? YES → expand new: [min(3,7), max(8,9)] = [3,9]
  [10,12]: 10 <= 9? NO → stop

Phase 3 — add merged result, then all REMAINING intervals:
  result = [[1,2], [3,9], [10,12]]

Before: ──  ──  ──  ────
After:  ──  ─────── ────
```

---

## 7. The Core Algorithm: Meeting Rooms (Counting Overlaps)

**Problem:** Given meeting intervals, what's the minimum number of rooms needed?

This is the "maximum depth" of overlapping intervals at any point.

### Method 1: Min-Heap (Greedy)

```
Sort by start. Use a min-heap tracking end times of active meetings.

Meetings: [0,30],[5,10],[15,20]

Add [0,30]:  heap=[30]          rooms=1
Add [5,10]:  5 < 30? heap full, add → heap=[10,30]   rooms=2
Add [15,20]: 15 > 10? yes, pop 10, push 20 → heap=[20,30]  rooms=2 (reuse!)

Answer: 2 rooms
```

The heap's size at any point = current rooms in use. Max heap size = answer.

### Method 2: Event Sweep (Elegant)

```
Treat every start as +1 event, every end as -1 event.
Sort all events. Walk through, track running sum. Max sum = answer.

[0,30],[5,10],[15,20]

Events: (0,+1),(5,+1),(10,-1),(15,+1),(20,-1),(30,-1)

0:  +1 → count=1
5:  +1 → count=2  ← peak
10: -1 → count=1
15: +1 → count=2  ← peak again
20: -1 → count=1
30: -1 → count=0

Answer: 2
```

This method visualizes overlap depth as a **height map**:

```
Count:
2 |        ████       ████
1 | ████████   ███████   █████
0 |─────────────────────────────→ time
   0    5   10  15  20  25  30
```

---

## 8. The "Why" Questions

### Why sort by start and not end?

Sorting by start lets you process intervals **left to right** and compare each new interval to the current rightmost boundary. If you sorted by end, you'd know when things finish but not where they begin relative to each other — you couldn't easily detect where new overlaps start.

*Exception:* Some greedy problems (like Activity Selection — maximize non-overlapping intervals) sort by **end time**, because finishing earlier leaves more room for future intervals.

### Why take `max(last.end, current.end)` during merge?

Because one interval might be **fully contained** in another:

```
last:    [1, ══════════════ 10]
current:    [3, ══ 5]

current.end=5 < last.end=10
If we used current.end, we'd shrink the merged interval!
max() ensures we keep the wider boundary.
```

### Why does the sweep line method work?

Because overlap depth is literally the count of intervals "active" at any moment. Start events open an interval, end events close one. The running sum at any time = exactly how many intervals contain that moment. It's a **direct encoding** of the problem into arithmetic.

---

## 9. "What If" Edge Cases

| What If...? | What Happens |
|---|---|
| Intervals are already sorted | Skip the sort step — O(n) total |
| Single interval | Trivially merged — return as-is |
| All intervals identical | All merge into one |
| Touching intervals `[1,3]` and `[3,5]` | Depends: `3 <= 3` is true → they merge if using ≤; don't merge if using < (open vs closed boundaries) |
| One interval contains all others | All merge into the containing interval |
| No overlaps at all | Output = input (every interval stays separate) |
| Negative start values | Algorithms work fine — sorting handles negative numbers naturally |
| Start equals end `[4,4]` | Point interval — valid, represents a single moment |
| Interval list is empty | Return empty — guard at start |
| Insertion target overlaps nothing | Just insert in sorted position, no merging needed |

### The Touching Boundary Decision

```
[1,3] and [3,5]:

Closed intervals [a,b] include endpoints → they SHARE point 3 → they overlap → MERGE
Half-open [a,b) exclude right endpoint → point 3 not in [1,3) → they DON'T overlap

Always clarify boundary type before coding.
```

---

## 10. Algorithm Taxonomy: Which Algorithm for Which Problem?

```
┌─────────────────────────────────────────────────────────┐
│                   INTERVAL PROBLEM                       │
└──────────────────────────┬──────────────────────────────┘
                           │
          ┌────────────────┼──────────────────┐
          ▼                ▼                  ▼
   MERGE/COMBINE     COUNT/DEPTH         SELECT/SCHEDULE
          │                │                  │
  Merge Intervals    Meeting Rooms      Activity Selection
  Insert Interval    Employee Free      Non-overlapping
  Find Gaps          Time               Intervals removal
          │                │                  │
   Sort by start     Sweep line or      Sort by END time
   Greedy merge      min-heap           Greedy selection
   O(n log n)        O(n log n)         O(n log n)
```

### Activity Selection — The "Sort by End" Exception

**Goal:** Pick maximum number of non-overlapping intervals.

```
Intervals: [1,4],[2,3],[3,5],[4,6]

Sort by END: [2,3],[1,4],[3,5],[4,6]

Greedily pick earliest-ending that doesn't overlap last picked:
Pick [2,3]  ← ends earliest, committed
Skip [1,4]  ← overlaps [2,3] (1 < 3)
Pick [3,5]  ← starts at 3 = end of last (touching OK or not, per rules)
Pick [4,6]  ← starts at 4 < 5? overlaps. Skip.
            Wait: [3,5] ends at 5. [4,6] starts at 4 < 5 → overlap → skip

Answer: [2,3],[3,5] → 2 intervals
```

**Why sort by end?** Because finishing earliest gives future intervals the most room. Greedy proof: any optimal solution can be transformed to include the earliest-ending interval without losing count.

---

## 11. Real-World Applications

| Domain | Problem | Interval Role |
|---|---|---|
| **Calendar apps** | Detect scheduling conflicts | Overlap detection between meeting intervals |
| **Operating systems** | Memory allocation | Free/used memory as intervals; merge free blocks |
| **Databases** | Range queries | Index scans over `[low, high]` value ranges |
| **Networking** | IP address range management | CIDR blocks as intervals; find coverage gaps |
| **Genomics** | Gene annotation | Genes as intervals on chromosome; find overlapping regions |
| **Video editing** | Timeline clips | Clips as intervals; detect cuts and overlaps |
| **Flight scheduling** | Gate assignment | Flights as time intervals; minimum gates = max overlap |
| **Load balancing** | Server time-slot allocation | Assign requests (intervals) to minimize servers needed |
| **Finance** | Market hours, trading windows | Interval arithmetic on time ranges |

---

## 12. Comparison With Related Techniques

```
                   ┌──────────────────────────────────────┐
                   │        RANGE/REGION TECHNIQUES        │
                   └──────────────────────────────────────┘
                          │           │           │
              ┌───────────┘    ┌──────┘    ┌──────┘
              ▼                ▼           ▼
          Intervals       Segment Tree   Binary Indexed Tree
          ──────────       ────────────   ──────────────────
          1D ranges        Range queries  Range sum queries
          Merge/detect     + point update + point update
          overlaps         O(log n)       O(log n) update
          Sort-based       Dynamic        Simpler to code
          O(n log n)       Handles        Sum only
          Static input     updates well   (not min/max)
```

**vs. Segment Tree:** When intervals are static and you just need to merge/count, sorting + sweep is simpler. Segment trees shine when intervals are **dynamically added/removed** and you need live queries.

**vs. Sliding Window:** Sliding window operates on **array indices** with a moving frame. Intervals operate on **value ranges** — the "start" and "end" are semantic data, not just positions in an array. They look similar but model different things.

**vs. Prefix Sums:** The sweep line counting method is essentially prefix sums over events — +1 at start, -1 at end, prefix sum = depth at any point. They're mathematically equivalent for depth queries on static intervals.

---

## 13. The Interval Problem Decision Framework

```
What does the problem ask?
│
├── "Merge overlapping intervals"
│       → Sort by start, greedy merge
│
├── "Insert new interval into sorted list"
│       → Three phases: before, overlap-absorb, after
│
├── "Minimum rooms / resources needed"
│       → Sort + min-heap OR sweep line (+1/-1 events)
│
├── "Maximum non-overlapping intervals"
│       → Sort by END, greedy selection
│
├── "Minimum intervals to remove for no overlap"
│       → Same as above: total - max_non_overlapping
│
├── "Find free time / gaps"
│       → Merge all, then scan for gaps between merged intervals
│
└── "Does interval X overlap with any in set?"
        → Sort set, binary search for potential overlaps
```

---

## 14. Tips for Long-Term Retention

**1. The calendar mental model**
Always visualize intervals as colored blocks on a day planner. Every algorithm becomes a physical operation: stacking blocks, counting peaks, finding gaps. This image makes the logic feel obvious rather than abstract.

**2. Memorize the 6 relationships**
Draw the 6 cases of two intervals on paper once. The single overlap test `a <= d AND c <= b` covers all of them. Understanding why this works (NOT disjoint = overlapping) is more durable than memorizing it.

**3. The three sorting rules**
- Merge problems → sort by **start**
- Scheduling/selection problems → sort by **end**
- Depth/counting problems → sweep with **events** (+1 start, -1 end)

**4. The `max(last.end, current.end)` reflex**
Whenever merging, always take the max of the two ends. The containment case (`[1,10]` absorbing `[3,5]`) will silently break your code if you forget this.

**5. Anchor the sweep line to a physical image**
Picture a vertical line sweeping left-to-right across your calendar. It counts how many colored blocks it intersects at any moment. When it enters a block: +1. When it exits: -1. Max count = answer. This image makes the event-array approach feel tangible.

**6. The two hard edge cases to always check**
- **Touching intervals:** `[1,3]` and `[3,5]` — do they merge? Know your boundary type.
- **Containment:** `[1,10]` and `[3,5]` — does `max(end)` preserve the outer end? Yes.

---

Intervals are fundamentally about **reasoning over ranges rather than points**. The shift from "is value X in the set?" to "does range A overlap range B?" unlocks a whole class of scheduling, resource allocation, and coverage problems. Sort once to impose order, then sweep linearly — and what looked like an O(n²) comparison problem collapses into elegant O(n) logic.
