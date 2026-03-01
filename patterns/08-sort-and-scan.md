# Pattern 08: Sort + Scan

## Diagram + Intuition

### Pattern Diagram
```text
sort first -> linear sweep
neighbors now carry global structure
```

### Read-the-Question Trigger Cues
- Intervals, conflicts, merging, global ordering.

### Intuition Anchor
- "Sorting reveals structure; scanning exploits it."

### 3-Second Pattern Check
- After sort, can one pass solve it?

## What This Pattern Solves
Sorting often reveals structure that is hidden in unsorted data.  
After sorting, a single linear scan can solve many interval and ordering problems.

## Recognition Signals
- Need to merge overlapping ranges.
- Need to detect conflicts based on start/end order.
- Need closest/next values globally.
- Brute force compares many pairs.

## Core Intuition
Sorting groups related items so local neighbors carry global information.  
After sorting, one pass is enough to:
- merge
- count transitions
- detect overlap

## Step-by-Step Method (Intervals)
1. Sort intervals by start time (and tie-break when needed).
2. Initialize result with first interval.
3. For each next interval:
   - if overlaps current merged interval -> extend end
   - else push new interval
4. Return merged result.

## Detailed Example (Merge Intervals)
`[[1,3],[2,6],[8,10],[15,18]]`
1. Already sorted by start.
2. Merge `[1,3]` and `[2,6]` -> `[1,6]`.
3. `[8,10]` does not overlap -> add separately.
4. `[15,18]` does not overlap -> add separately.

## Complexity
- Time: `O(n log n)` from sort
- Scan: `O(n)`
- Space: `O(n)` for output (or `O(1)` extra in some in-place variants)

## Python Template
```python
def merge_intervals(intervals):
    if not intervals:
        return []

    intervals.sort(key=lambda x: x[0])
    merged = [intervals[0]]

    for start, end in intervals[1:]:
        last_end = merged[-1][1]
        if start <= last_end:
            merged[-1][1] = max(last_end, end)
        else:
            merged.append([start, end])

    return merged
```

## Common Pitfalls
- Sorting by wrong key (e.g., end instead of start for merge tasks).
- Overlap condition confusion (`start <= last_end` vs `<` depending closed/open intervals).
- Mutating original interval objects unexpectedly.
- Forgetting edge cases: empty input or single interval.

## Variations
- Meeting Rooms / Meeting Rooms II
- Non-overlapping intervals (minimum removals)
- Insert Interval
- Minimum number of arrows to burst balloons

## Interview Tips
- Say: "Sort gives me a deterministic sweep order."
- Mention exact overlap rule and interval type (inclusive vs exclusive).
- If asked for count only, avoid storing full merged list when not needed.

## Practice Problems
- Merge Intervals
- Insert Interval
- Non-overlapping Intervals
- Meeting Rooms
