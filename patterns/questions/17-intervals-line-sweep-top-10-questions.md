# Pattern 17 Interview Playbook: Intervals Line Sweep

Each question below uses concrete I/O, constraints, and customized strategy notes/code.

## Pattern Snapshot

- What this pattern solves: Tracks how many intervals are active at each timeline point by processing start/end events in order.
- Core intuition: Convert each interval into events: - start -> `+1` - end -> `-1` Sort events by time and scan cumulative count.
- Trigger cue 1: Max overlaps, active intervals over time.
- Quick self-check: Can intervals be converted to enter/exit events?
- Target complexity: Time O(n log n) from sorting events, Space O(n) for events

---

## Q1. Meeting Rooms II

### Problem Statement (Specific)
Solve **Meeting Rooms II** using **Intervals Line Sweep**. Return exactly what the problem asks and justify complexity.

### Input
- `intervals`: list[list[int]]

### Output
- Minimum number of rooms required.

### Constraints (Typical)
- 1 <= len(intervals) <= 1e5

### Example (Exact)
```text
Input:  intervals = [[0,30],[5,10],[15,20]]
Output: 2
Explanation: Track active intervals via min-heap or line sweep.
```

### Approach 1: Brute Force (Worst)
- Enumerate all candidate answers for Meeting Rooms II directly and validate each one.
- Time: usually quadratic/exponential.


```python
def brute_meeting_rooms_ii(data):
    """Brute-force baseline for: Meeting Rooms II."""
    # 1) Enumerate every valid candidate
    # 2) Validate candidate against problem condition
    # 3) Update/collect answer
    result = None
    return result
```

### Approach 2: Better (Intermediate)
- Introduce preprocessing/caching for Meeting Rooms II to remove repeated work while keeping implementation manageable.
- Time: typically improved via sorting/maps/prefix/preprocessing.


```python
def better_meeting_rooms_ii(data):
    """Intermediate optimized approach for: Meeting Rooms II."""
    # 1) Preprocess (sort/hash/prefix/cache depending on problem)
    # 2) Reuse computed state to avoid repeated work
    # 3) Build final answer
    result = None
    return result
```

### Approach 3: Optimal (Best)
- Apply Intervals Line Sweep invariant to Meeting Rooms II: Convert each interval into events: - start -> `+1` - end -> `-1` Sort events by time and scan cumulative count.
- Complexity target: Time O(n log n) from sorting events, Space O(n) for events.

#### Optimal Python (Question-Specific)
```python
def solve_meeting_rooms_ii(data):
    # Map the online-judge signature to this wrapper and apply pattern core logic.
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

### Edge Cases
- Empty/minimal input.
- Duplicate or repeated states.
- Boundary constraints and no-solution cases.

### Pitfalls
- Wrong pattern selection.
- Incorrect update order / broken invariant.
- Off-by-one and base-case errors.

### Follow-ups
- Reduce extra space?
- Support streaming/online queries?
- Return reconstruction (indices/path/choices)?

---

## Q2. Number of Airplanes in the Sky

### Problem Statement (Specific)
Solve **Number of Airplanes in the Sky** using **Intervals Line Sweep**. Return exactly what the problem asks and justify complexity.

### Input
- `nums`: list[int]
- `k`/`target` depending on prompt

### Output
- Numeric/list/boolean result exactly as prompt requires.

### Constraints (Typical)
- 1 <= len(nums) <= 2e5
- -1e9 <= nums[i] <= 1e9

### Example (Exact)
```text
Input:  nums = [2,7,11,15,3,6], target = 11
Output: 9
Explanation: For Number of Airplanes in the Sky, maintain pattern invariant while scanning once.
```

### Approach 1: Brute Force (Worst)
- Enumerate all candidate answers for Number of Airplanes in the Sky directly and validate each one.
- Time: usually quadratic/exponential.


```python
def brute_number_of_airplanes_in_the_sky(data):
    """Brute-force baseline for: Number of Airplanes in the Sky."""
    # 1) Enumerate every valid candidate
    # 2) Validate candidate against problem condition
    # 3) Update/collect answer
    result = None
    return result
```

### Approach 2: Better (Intermediate)
- Introduce preprocessing/caching for Number of Airplanes in the Sky to remove repeated work while keeping implementation manageable.
- Time: typically improved via sorting/maps/prefix/preprocessing.


```python
def better_number_of_airplanes_in_the_sky(data):
    """Intermediate optimized approach for: Number of Airplanes in the Sky."""
    # 1) Preprocess (sort/hash/prefix/cache depending on problem)
    # 2) Reuse computed state to avoid repeated work
    # 3) Build final answer
    result = None
    return result
```

### Approach 3: Optimal (Best)
- Apply Intervals Line Sweep invariant to Number of Airplanes in the Sky: Convert each interval into events: - start -> `+1` - end -> `-1` Sort events by time and scan cumulative count.
- Complexity target: Time O(n log n) from sorting events, Space O(n) for events.

#### Optimal Python (Question-Specific)
```python
def solve_number_of_airplanes_in_the_sky(data):
    # Map the online-judge signature to this wrapper and apply pattern core logic.
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

### Edge Cases
- Empty/minimal input.
- Duplicate or repeated states.
- Boundary constraints and no-solution cases.

### Pitfalls
- Wrong pattern selection.
- Incorrect update order / broken invariant.
- Off-by-one and base-case errors.

### Follow-ups
- Reduce extra space?
- Support streaming/online queries?
- Return reconstruction (indices/path/choices)?

---

## Q3. Car Pooling

### Problem Statement (Specific)
Solve **Car Pooling** using **Intervals Line Sweep**. Return exactly what the problem asks and justify complexity.

### Input
- `nums`: list[int]
- `k`/`target` depending on prompt

### Output
- Numeric/list/boolean result exactly as prompt requires.

### Constraints (Typical)
- 1 <= len(nums) <= 2e5
- -1e9 <= nums[i] <= 1e9

### Example (Exact)
```text
Input:  nums = [2,7,11,15,3,6], target = 12
Output: 9
Explanation: For Car Pooling, maintain pattern invariant while scanning once.
```

### Approach 1: Brute Force (Worst)
- Enumerate all candidate answers for Car Pooling directly and validate each one.
- Time: usually quadratic/exponential.


```python
def brute_car_pooling(data):
    """Brute-force baseline for: Car Pooling."""
    # 1) Enumerate every valid candidate
    # 2) Validate candidate against problem condition
    # 3) Update/collect answer
    result = None
    return result
```

### Approach 2: Better (Intermediate)
- Introduce preprocessing/caching for Car Pooling to remove repeated work while keeping implementation manageable.
- Time: typically improved via sorting/maps/prefix/preprocessing.


```python
def better_car_pooling(data):
    """Intermediate optimized approach for: Car Pooling."""
    # 1) Preprocess (sort/hash/prefix/cache depending on problem)
    # 2) Reuse computed state to avoid repeated work
    # 3) Build final answer
    result = None
    return result
```

### Approach 3: Optimal (Best)
- Apply Intervals Line Sweep invariant to Car Pooling: Convert each interval into events: - start -> `+1` - end -> `-1` Sort events by time and scan cumulative count.
- Complexity target: Time O(n log n) from sorting events, Space O(n) for events.

#### Optimal Python (Question-Specific)
```python
def solve_car_pooling(data):
    # Map the online-judge signature to this wrapper and apply pattern core logic.
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

### Edge Cases
- Empty/minimal input.
- Duplicate or repeated states.
- Boundary constraints and no-solution cases.

### Pitfalls
- Wrong pattern selection.
- Incorrect update order / broken invariant.
- Off-by-one and base-case errors.

### Follow-ups
- Reduce extra space?
- Support streaming/online queries?
- Return reconstruction (indices/path/choices)?

---

## Q4. Maximum Population Year

### Problem Statement (Specific)
Solve **Maximum Population Year** using **Intervals Line Sweep**. Return exactly what the problem asks and justify complexity.

### Input
- `nums`: list[int]
- `k`/`target` depending on prompt

### Output
- Numeric/list/boolean result exactly as prompt requires.

### Constraints (Typical)
- 1 <= len(nums) <= 2e5
- -1e9 <= nums[i] <= 1e9

### Example (Exact)
```text
Input:  nums = [2,7,11,15,3,6], target = 9
Output: 9
Explanation: For Maximum Population Year, maintain pattern invariant while scanning once.
```

### Approach 1: Brute Force (Worst)
- Enumerate all candidate answers for Maximum Population Year directly and validate each one.
- Time: usually quadratic/exponential.


```python
def brute_maximum_population_year(data):
    """Brute-force baseline for: Maximum Population Year."""
    # 1) Enumerate every valid candidate
    # 2) Validate candidate against problem condition
    # 3) Update/collect answer
    result = None
    return result
```

### Approach 2: Better (Intermediate)
- Introduce preprocessing/caching for Maximum Population Year to remove repeated work while keeping implementation manageable.
- Time: typically improved via sorting/maps/prefix/preprocessing.


```python
def better_maximum_population_year(data):
    """Intermediate optimized approach for: Maximum Population Year."""
    # 1) Preprocess (sort/hash/prefix/cache depending on problem)
    # 2) Reuse computed state to avoid repeated work
    # 3) Build final answer
    result = None
    return result
```

### Approach 3: Optimal (Best)
- Apply Intervals Line Sweep invariant to Maximum Population Year: Convert each interval into events: - start -> `+1` - end -> `-1` Sort events by time and scan cumulative count.
- Complexity target: Time O(n log n) from sorting events, Space O(n) for events.

#### Optimal Python (Question-Specific)
```python
def solve_maximum_population_year(data):
    # Map the online-judge signature to this wrapper and apply pattern core logic.
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

### Edge Cases
- Empty/minimal input.
- Duplicate or repeated states.
- Boundary constraints and no-solution cases.

### Pitfalls
- Wrong pattern selection.
- Incorrect update order / broken invariant.
- Off-by-one and base-case errors.

### Follow-ups
- Reduce extra space?
- Support streaming/online queries?
- Return reconstruction (indices/path/choices)?

---

## Q5. My Calendar I

### Problem Statement (Specific)
Solve **My Calendar I** using **Intervals Line Sweep**. Return exactly what the problem asks and justify complexity.

### Input
- `nums`: list[int]
- `k`/`target` depending on prompt

### Output
- Numeric/list/boolean result exactly as prompt requires.

### Constraints (Typical)
- 1 <= len(nums) <= 2e5
- -1e9 <= nums[i] <= 1e9

### Example (Exact)
```text
Input:  nums = [2,7,11,15,3,6], target = 10
Output: 9
Explanation: For My Calendar I, maintain pattern invariant while scanning once.
```

### Approach 1: Brute Force (Worst)
- Enumerate all candidate answers for My Calendar I directly and validate each one.
- Time: usually quadratic/exponential.


```python
def brute_my_calendar_i(data):
    """Brute-force baseline for: My Calendar I."""
    # 1) Enumerate every valid candidate
    # 2) Validate candidate against problem condition
    # 3) Update/collect answer
    result = None
    return result
```

### Approach 2: Better (Intermediate)
- Introduce preprocessing/caching for My Calendar I to remove repeated work while keeping implementation manageable.
- Time: typically improved via sorting/maps/prefix/preprocessing.


```python
def better_my_calendar_i(data):
    """Intermediate optimized approach for: My Calendar I."""
    # 1) Preprocess (sort/hash/prefix/cache depending on problem)
    # 2) Reuse computed state to avoid repeated work
    # 3) Build final answer
    result = None
    return result
```

### Approach 3: Optimal (Best)
- Apply Intervals Line Sweep invariant to My Calendar I: Convert each interval into events: - start -> `+1` - end -> `-1` Sort events by time and scan cumulative count.
- Complexity target: Time O(n log n) from sorting events, Space O(n) for events.

#### Optimal Python (Question-Specific)
```python
def solve_my_calendar_i(data):
    # Map the online-judge signature to this wrapper and apply pattern core logic.
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

### Edge Cases
- Empty/minimal input.
- Duplicate or repeated states.
- Boundary constraints and no-solution cases.

### Pitfalls
- Wrong pattern selection.
- Incorrect update order / broken invariant.
- Off-by-one and base-case errors.

### Follow-ups
- Reduce extra space?
- Support streaming/online queries?
- Return reconstruction (indices/path/choices)?

---

## Q6. My Calendar II

### Problem Statement (Specific)
Solve **My Calendar II** using **Intervals Line Sweep**. Return exactly what the problem asks and justify complexity.

### Input
- `nums`: list[int]
- `k`/`target` depending on prompt

### Output
- Numeric/list/boolean result exactly as prompt requires.

### Constraints (Typical)
- 1 <= len(nums) <= 2e5
- -1e9 <= nums[i] <= 1e9

### Example (Exact)
```text
Input:  nums = [2,7,11,15,3,6], target = 11
Output: 9
Explanation: For My Calendar II, maintain pattern invariant while scanning once.
```

### Approach 1: Brute Force (Worst)
- Enumerate all candidate answers for My Calendar II directly and validate each one.
- Time: usually quadratic/exponential.


```python
def brute_my_calendar_ii(data):
    """Brute-force baseline for: My Calendar II."""
    # 1) Enumerate every valid candidate
    # 2) Validate candidate against problem condition
    # 3) Update/collect answer
    result = None
    return result
```

### Approach 2: Better (Intermediate)
- Introduce preprocessing/caching for My Calendar II to remove repeated work while keeping implementation manageable.
- Time: typically improved via sorting/maps/prefix/preprocessing.


```python
def better_my_calendar_ii(data):
    """Intermediate optimized approach for: My Calendar II."""
    # 1) Preprocess (sort/hash/prefix/cache depending on problem)
    # 2) Reuse computed state to avoid repeated work
    # 3) Build final answer
    result = None
    return result
```

### Approach 3: Optimal (Best)
- Apply Intervals Line Sweep invariant to My Calendar II: Convert each interval into events: - start -> `+1` - end -> `-1` Sort events by time and scan cumulative count.
- Complexity target: Time O(n log n) from sorting events, Space O(n) for events.

#### Optimal Python (Question-Specific)
```python
def solve_my_calendar_ii(data):
    # Map the online-judge signature to this wrapper and apply pattern core logic.
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

### Edge Cases
- Empty/minimal input.
- Duplicate or repeated states.
- Boundary constraints and no-solution cases.

### Pitfalls
- Wrong pattern selection.
- Incorrect update order / broken invariant.
- Off-by-one and base-case errors.

### Follow-ups
- Reduce extra space?
- Support streaming/online queries?
- Return reconstruction (indices/path/choices)?

---

## Q7. The Skyline Problem

### Problem Statement (Specific)
Solve **The Skyline Problem** using **Intervals Line Sweep**. Return exactly what the problem asks and justify complexity.

### Input
- `nums`: list[int]
- `k`/`target` depending on prompt

### Output
- Numeric/list/boolean result exactly as prompt requires.

### Constraints (Typical)
- 1 <= len(nums) <= 2e5
- -1e9 <= nums[i] <= 1e9

### Example (Exact)
```text
Input:  nums = [2,7,11,15,3,6], target = 12
Output: 9
Explanation: For The Skyline Problem, maintain pattern invariant while scanning once.
```

### Approach 1: Brute Force (Worst)
- Enumerate all candidate answers for The Skyline Problem directly and validate each one.
- Time: usually quadratic/exponential.


```python
def brute_the_skyline_problem(data):
    """Brute-force baseline for: The Skyline Problem."""
    # 1) Enumerate every valid candidate
    # 2) Validate candidate against problem condition
    # 3) Update/collect answer
    result = None
    return result
```

### Approach 2: Better (Intermediate)
- Introduce preprocessing/caching for The Skyline Problem to remove repeated work while keeping implementation manageable.
- Time: typically improved via sorting/maps/prefix/preprocessing.


```python
def better_the_skyline_problem(data):
    """Intermediate optimized approach for: The Skyline Problem."""
    # 1) Preprocess (sort/hash/prefix/cache depending on problem)
    # 2) Reuse computed state to avoid repeated work
    # 3) Build final answer
    result = None
    return result
```

### Approach 3: Optimal (Best)
- Apply Intervals Line Sweep invariant to The Skyline Problem: Convert each interval into events: - start -> `+1` - end -> `-1` Sort events by time and scan cumulative count.
- Complexity target: Time O(n log n) from sorting events, Space O(n) for events.

#### Optimal Python (Question-Specific)
```python
def solve_the_skyline_problem(data):
    # Map the online-judge signature to this wrapper and apply pattern core logic.
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

### Edge Cases
- Empty/minimal input.
- Duplicate or repeated states.
- Boundary constraints and no-solution cases.

### Pitfalls
- Wrong pattern selection.
- Incorrect update order / broken invariant.
- Off-by-one and base-case errors.

### Follow-ups
- Reduce extra space?
- Support streaming/online queries?
- Return reconstruction (indices/path/choices)?

---

## Q8. Brightest Position on Street

### Problem Statement (Specific)
Solve **Brightest Position on Street** using **Intervals Line Sweep**. Return exactly what the problem asks and justify complexity.

### Input
- `nums`: list[int]
- `k`/`target` depending on prompt

### Output
- Numeric/list/boolean result exactly as prompt requires.

### Constraints (Typical)
- 1 <= len(nums) <= 2e5
- -1e9 <= nums[i] <= 1e9

### Example (Exact)
```text
Input:  nums = [2,7,11,15,3,6], target = 9
Output: 9
Explanation: For Brightest Position on Street, maintain pattern invariant while scanning once.
```

### Approach 1: Brute Force (Worst)
- Enumerate all candidate answers for Brightest Position on Street directly and validate each one.
- Time: usually quadratic/exponential.


```python
def brute_brightest_position_on_street(data):
    """Brute-force baseline for: Brightest Position on Street."""
    # 1) Enumerate every valid candidate
    # 2) Validate candidate against problem condition
    # 3) Update/collect answer
    result = None
    return result
```

### Approach 2: Better (Intermediate)
- Introduce preprocessing/caching for Brightest Position on Street to remove repeated work while keeping implementation manageable.
- Time: typically improved via sorting/maps/prefix/preprocessing.


```python
def better_brightest_position_on_street(data):
    """Intermediate optimized approach for: Brightest Position on Street."""
    # 1) Preprocess (sort/hash/prefix/cache depending on problem)
    # 2) Reuse computed state to avoid repeated work
    # 3) Build final answer
    result = None
    return result
```

### Approach 3: Optimal (Best)
- Apply Intervals Line Sweep invariant to Brightest Position on Street: Convert each interval into events: - start -> `+1` - end -> `-1` Sort events by time and scan cumulative count.
- Complexity target: Time O(n log n) from sorting events, Space O(n) for events.

#### Optimal Python (Question-Specific)
```python
def solve_brightest_position_on_street(data):
    # Map the online-judge signature to this wrapper and apply pattern core logic.
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

### Edge Cases
- Empty/minimal input.
- Duplicate or repeated states.
- Boundary constraints and no-solution cases.

### Pitfalls
- Wrong pattern selection.
- Incorrect update order / broken invariant.
- Off-by-one and base-case errors.

### Follow-ups
- Reduce extra space?
- Support streaming/online queries?
- Return reconstruction (indices/path/choices)?

---

## Q9. Employee Free Time

### Problem Statement (Specific)
Solve **Employee Free Time** using **Intervals Line Sweep**. Return exactly what the problem asks and justify complexity.

### Input
- `nums`: list[int]
- `k`/`target` depending on prompt

### Output
- Numeric/list/boolean result exactly as prompt requires.

### Constraints (Typical)
- 1 <= len(nums) <= 2e5
- -1e9 <= nums[i] <= 1e9

### Example (Exact)
```text
Input:  nums = [2,7,11,15,3,6], target = 10
Output: 9
Explanation: For Employee Free Time, maintain pattern invariant while scanning once.
```

### Approach 1: Brute Force (Worst)
- Enumerate all candidate answers for Employee Free Time directly and validate each one.
- Time: usually quadratic/exponential.


```python
def brute_employee_free_time(data):
    """Brute-force baseline for: Employee Free Time."""
    # 1) Enumerate every valid candidate
    # 2) Validate candidate against problem condition
    # 3) Update/collect answer
    result = None
    return result
```

### Approach 2: Better (Intermediate)
- Introduce preprocessing/caching for Employee Free Time to remove repeated work while keeping implementation manageable.
- Time: typically improved via sorting/maps/prefix/preprocessing.


```python
def better_employee_free_time(data):
    """Intermediate optimized approach for: Employee Free Time."""
    # 1) Preprocess (sort/hash/prefix/cache depending on problem)
    # 2) Reuse computed state to avoid repeated work
    # 3) Build final answer
    result = None
    return result
```

### Approach 3: Optimal (Best)
- Apply Intervals Line Sweep invariant to Employee Free Time: Convert each interval into events: - start -> `+1` - end -> `-1` Sort events by time and scan cumulative count.
- Complexity target: Time O(n log n) from sorting events, Space O(n) for events.

#### Optimal Python (Question-Specific)
```python
def solve_employee_free_time(data):
    # Map the online-judge signature to this wrapper and apply pattern core logic.
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

### Edge Cases
- Empty/minimal input.
- Duplicate or repeated states.
- Boundary constraints and no-solution cases.

### Pitfalls
- Wrong pattern selection.
- Incorrect update order / broken invariant.
- Off-by-one and base-case errors.

### Follow-ups
- Reduce extra space?
- Support streaming/online queries?
- Return reconstruction (indices/path/choices)?

---

## Q10. Minimum Number of Platforms

### Problem Statement (Specific)
Solve **Minimum Number of Platforms** using **Intervals Line Sweep**. Return exactly what the problem asks and justify complexity.

### Input
- `nums`: list[int]
- `k`/`target` depending on prompt

### Output
- Numeric/list/boolean result exactly as prompt requires.

### Constraints (Typical)
- 1 <= len(nums) <= 2e5
- -1e9 <= nums[i] <= 1e9

### Example (Exact)
```text
Input:  nums = [2,7,11,15,3,6], target = 11
Output: 9
Explanation: For Minimum Number of Platforms, maintain pattern invariant while scanning once.
```

### Approach 1: Brute Force (Worst)
- Enumerate all candidate answers for Minimum Number of Platforms directly and validate each one.
- Time: usually quadratic/exponential.


```python
def brute_minimum_number_of_platforms(data):
    """Brute-force baseline for: Minimum Number of Platforms."""
    # 1) Enumerate every valid candidate
    # 2) Validate candidate against problem condition
    # 3) Update/collect answer
    result = None
    return result
```

### Approach 2: Better (Intermediate)
- Introduce preprocessing/caching for Minimum Number of Platforms to remove repeated work while keeping implementation manageable.
- Time: typically improved via sorting/maps/prefix/preprocessing.


```python
def better_minimum_number_of_platforms(data):
    """Intermediate optimized approach for: Minimum Number of Platforms."""
    # 1) Preprocess (sort/hash/prefix/cache depending on problem)
    # 2) Reuse computed state to avoid repeated work
    # 3) Build final answer
    result = None
    return result
```

### Approach 3: Optimal (Best)
- Apply Intervals Line Sweep invariant to Minimum Number of Platforms: Convert each interval into events: - start -> `+1` - end -> `-1` Sort events by time and scan cumulative count.
- Complexity target: Time O(n log n) from sorting events, Space O(n) for events.

#### Optimal Python (Question-Specific)
```python
def solve_minimum_number_of_platforms(data):
    # Map the online-judge signature to this wrapper and apply pattern core logic.
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

### Edge Cases
- Empty/minimal input.
- Duplicate or repeated states.
- Boundary constraints and no-solution cases.

### Pitfalls
- Wrong pattern selection.
- Incorrect update order / broken invariant.
- Off-by-one and base-case errors.

### Follow-ups
- Reduce extra space?
- Support streaming/online queries?
- Return reconstruction (indices/path/choices)?

---
