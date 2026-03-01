# Pattern 17: Intervals Line Sweep

## Diagram + Intuition

### Pattern Diagram
```text
[start:+1, end:-1] events
sort by time -> running active count
```

### Read-the-Question Trigger Cues
- Max overlaps, active intervals over time.

### Intuition Anchor
- "Track population changes at event points, not every timestamp."

### 3-Second Pattern Check
- Can intervals be converted to enter/exit events?

## What This Pattern Solves
Tracks how many intervals are active at each timeline point by processing start/end events in order.

## Recognition Signals
- Need max concurrent intervals or active count over time.
- Inputs are many `[start, end]` intervals.
- Event ordering matters more than pairwise overlap checks.

## Core Intuition
Convert each interval into events:
- start -> `+1`
- end -> `-1`

Sort events by time and scan cumulative count.

## Step-by-Step Method
1. Build event list `(time, delta)` for each interval.
2. Sort events with tie-breaking rules:
   - for half-open ranges `[start, end)`, process end before start at same time
   - adjust for inclusive intervals accordingly
3. Sweep through events:
   - `active += delta`
   - update peak or collect timeline metrics

## Detailed Example (Meeting Rooms II)
Intervals: `[0,30], [5,10], [15,20]`
1. Events: `(0,+1),(30,-1),(5,+1),(10,-1),(15,+1),(20,-1)`.
2. Sorted scan active counts: 1 -> 2 -> 1 -> 2 -> 1 -> 0.
3. Peak active = 2 rooms needed.

## Complexity
- Time: `O(n log n)` from sorting events
- Space: `O(n)` for events

## Python Template
```python
def min_rooms(intervals):
    events = []
    for s, e in intervals:
        events.append((s, 1))
        events.append((e, -1))

    # End before start at same time for [start, end) interpretation.
    events.sort(key=lambda x: (x[0], x[1]))

    active = 0
    best = 0
    for _, delta in events:
        active += delta
        best = max(best, active)

    return best
```

## Common Pitfalls
- Wrong tie-break ordering at same timestamp.
- Mixing inclusive and exclusive end semantics.
- Forgetting coordinate compression for large sparse domains (if array sweep attempted).

## Variations
- Number of airplanes in the sky
- Maximum population year
- Car pooling capacity feasibility
- Skyline problem (advanced event sweep)

## Interview Tips
- Clarify interval semantics before writing sort comparator.
- Mention equivalent min-heap approach and tradeoffs.
- Show one timestamp tie example to prove correctness.

## Practice Problems
- Meeting Rooms II
- Car Pooling
- Maximum Population Year
- The Skyline Problem
