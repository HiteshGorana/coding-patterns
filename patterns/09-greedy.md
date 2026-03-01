# Pattern 09: Greedy

## At a Glance

| Item | Summary |
|---|---|
| Use when | A local best/safe choice can be proven to lead to a global optimum |
| Main tradeoff | Often fastest/simplest, but only correct with a clear safety proof |
| Typical runtime | Usually `O(n)` or `O(n log n)` (if sorting is needed) |
| Main structures | minimal running state (`best_so_far`, `reach`, `last_end`, counters), optional sort |
| Common prompts | maximize/minimize count/cost with one-pass decisions, interval scheduling, jump reachability, gas station |

## Related Playbook

- Full interview question set for this pattern:
  [Pattern 09 Top 10 Questions Playbook](./questions/09-greedy-top-10-questions.md)

## Diagram + Intuition

### Pattern Diagram

```text
repeat:
  1) choose the locally safest/best action by rule
  2) commit (do not backtrack)
  3) update minimal state

correctness hinge:
  local choice must be provably safe
  (exchange argument / stay-ahead / cut property)
```

### Read-the-Question Trigger Cues

- Objective is min/max and decisions are incremental.
- A simple rule seems to work if choices are processed in a specific order.
- Problem hints at "earliest finishing", "farthest reach", "minimum removals", "always take best now".
- DP/backtracking looks possible but likely heavier than needed.

### Intuition Anchor

- "Commit only when I can explain why changing this local choice cannot improve the final answer."

### 3-Second Pattern Check

- Can I state a one-line proof idea (exchange/stay-ahead)?
- Does each step reduce future uncertainty without requiring reversal?
- Is there a deterministic ordering (often sorted) that makes local choices safe?

## Decision Table: What to Store

| Prompt shape | Structure | Key -> value | Typical query |
|---|---|---|---|
| reachability/coverage | running boundary | `state -> farthest reachable` | can current index be reached? |
| interval selection/removal | sorted intervals + last kept end | `last_end` | does current interval conflict? |
| resource reset/candidate start | running sum + total sum | `tank`, `total`, `candidate` | if tank < 0, reset start |
| local gain optimization | sorted values and counters | `chosen_count`, `current_cost` | can we include this item safely? |
| partition by last occurrence | map + running boundary | `char -> last index`, `end` | reached boundary to cut segment? |
| activity scheduling | sorted by finish time | `current_end` | can next activity start now? |

## Universal Invariant

Before coding, say this sentence out loud:

- "After processing position `i`, my chosen decisions are at least as good as any alternative that respects the same processed prefix under the greedy rule."

If this invariant is unclear, the implementation will usually fail on edge cases.

## Step-by-Step Method (Easy Version)

Use this exact flow while coding:

1. Write the default return first (`False`, `0`, `[]`, or `-1`).
2. Define greedy rule in one sentence (what you choose at each step).
3. State proof sketch quickly (exchange or stay-ahead).
4. If order matters, sort by the correct key.
5. Iterate once, applying rule and updating minimal state.
6. Handle reset/tie-break conditions explicitly.
7. Return final constructed value or feasibility result.

Fill-in template:

```python
def solve(items):
    items = preprocess_or_sort_if_needed(items)
    state = init_state()

    for x in items:
        if should_take_or_reset(x, state):
            apply_greedy_action(x, state)
        else:
            apply_alternative_update(x, state)

    return build_answer(state)
```

## Query/Update Order Rules

### A) Check feasibility, then commit (most common)

Use for reachability and conflict checks.

```python
for i, x in enumerate(nums):
    if violates_invariant(i, state):
        return fail_answer
    update_state_with_choice(i, x)
```

### B) Sort first, then greedy-select during scan

Use for interval scheduling/removal and cost minimization by order.

```python
items.sort(key=greedy_key)
for x in items:
    if can_take(x, state):
        take(x, state)
    else:
        skip_or_replace(x, state)
```

### C) Two-pass validation + construction

Use when one pass validates feasibility and second pass builds answer.

```python
if not globally_feasible(items):
    return impossible

state = init()
for x in items:
    greedily_construct_answer(x, state)
```

## Detailed Example (Jump Game)

**Input:** `nums = [2, 3, 1, 1, 4]`

1. Start `reach = 0`.
2. At `i=0`, reachable, update `reach = max(0, 0+2) = 2`.
3. At `i=1`, reachable, update `reach = max(2, 1+3) = 4`.
4. Since `reach >= last_index`, you can reach the end.
5. Return `True`.

Why it works: maintaining farthest reachable index is a stay-ahead invariant; if any index becomes unreachable, no later step can fix it.

## Reusable Python Templates

### 1) Membership (Can Reach End)

```python
def can_jump(nums):
    reach = 0
    for i, step in enumerate(nums):
        if i > reach:
            return False
        reach = max(reach, i + step)
    return True
```

Example:

```python
can_jump([2, 3, 1, 1, 4])  # True
can_jump([3, 2, 1, 0, 4])  # False
```

### 2) Frequency/Boundary Count (Partition Labels)

```python
def partition_labels(s):
    last = {ch: i for i, ch in enumerate(s)}
    out = []
    start = end = 0

    for i, ch in enumerate(s):
        end = max(end, last[ch])
        if i == end:
            out.append(end - start + 1)
            start = i + 1

    return out
```

Example:

```python
partition_labels("ababcbacadefegdehijhklij")  # [9, 7, 8]
partition_labels("eccbbbbdec")  # [10]
```

### 3) Value -> Index Candidate (Gas Station Start)

```python
def can_complete_circuit(gas, cost):
    total = 0
    tank = 0
    start = 0

    for i in range(len(gas)):
        diff = gas[i] - cost[i]
        total += diff
        tank += diff
        if tank < 0:
            start = i + 1
            tank = 0

    return start if total >= 0 else -1
```

Example:

```python
can_complete_circuit([1,2,3,4,5], [3,4,5,1,2])  # 3
can_complete_circuit([2,3,4], [3,4,3])  # -1
```

### 4) Sort + Greedy Selection (Non-overlapping Intervals)

```python
def erase_overlap_intervals(intervals):
    if not intervals:
        return 0

    intervals.sort(key=lambda x: x[1])  # earliest end first
    kept = 0
    last_end = float("-inf")

    for s, e in intervals:
        if s >= last_end:
            kept += 1
            last_end = e

    return len(intervals) - kept
```

Example:

```python
erase_overlap_intervals([[1,2],[2,3],[3,4],[1,3]])  # 1
erase_overlap_intervals([[1,2],[1,2],[1,2]])  # 2
```

## Complexity

Let:

- `n` = number of input elements/items.
- `Csort` = sorting cost (usually `O(n log n)` when sorting is used).

Per-operation cost:

- Greedy state update/check during scan: `O(1)` each.

End-to-end cost (most interview problems):

| Variant | Time (average) | Space |
|---|---|---|
| one-pass reachability/candidate reset | `O(n)` | `O(1)` |
| partition by precomputed last index | `O(n)` | `O(u)` |
| interval scheduling/removal with sort | `O(n log n)` | `O(1)` extra |
| sort + greedy construction | `O(n log n)` | `O(1)` to `O(n)` |
| greedy + heap variants | `O(n log n)` | `O(n)` |

Interview note:

- State total complexity with sort included.
- Emphasize that correctness comes from proof, not only runtime.

## Edge-Case Checklist (Pre-Submit)

Use this as a final pass before you finish coding.

### Contract Checks

- Return type matches prompt exactly: boolean, count, start index, list, or cost.
- No-solution behavior is explicit and correct (`False`, `0`, `-1`, or `[]`).
- If multiple valid answers exist, prompt tie-break requirements are respected.
- For index outputs, confirm 0-based vs 1-based expectations.

### Data-Rule Checks

- Greedy rule is explicitly stated and justified.
- If sorting is required, key and tie-break are correct.
- Reset logic (when invariant breaks) is intentional and complete.
- Running totals/boundaries are updated in correct order.
- Local choice does not violate future feasibility by proof argument.

### Input Boundary Checks

- Empty input and single-element input handled safely.
- All-equal/all-zero/extreme values handled.
- Negative values are handled when allowed by prompt.
- Large `n` does not accidentally trigger quadratic fallback logic.
- Already-optimal and worst-case inputs both behave correctly.

### Pattern-Specific Checks

- Reachability problems fail immediately when current index exceeds farthest reach.
- Interval greedy uses correct boundary relation (`>=` vs `>`).
- Gas station variant checks total feasibility before trusting candidate start.
- Partition-label style uses last occurrence map, not first.

### Quick Sanity Tests (Run Mentally)

| Scenario | Example | What should happen |
|---|---|---|
| trivial reachable | `nums=[0]` | jump result is `True` |
| blocked jump | `[3,2,1,0,4]` | jump result is `False` |
| feasible circuit | gas/cost example with answer `3` | returns correct start |
| impossible circuit | total gas < total cost | returns `-1` |
| overlap-heavy intervals | `[[1,2],[1,2],[1,2]]` | removals count correct |

## Common Pitfalls

- Applying greedy rule without proof and missing counterexamples.
- Equating "largest immediate value" with "safest structural choice."
- Forgetting required sort or choosing wrong sort key.
- Missing tie-break logic that preserves optimality.
- Failing to reset state when local feasibility breaks.

## When Not Ideal

- Local-choice property is absent (greedy can fail; DP/backtracking needed).
- Objective depends on long-range interactions not captured by small state.
- Prompt requires counting all optimal solutions (not just one optimum).
- Constraints are small enough that exact DP is preferred for certainty.

## Variations

- Interval scheduling / non-overlap removal.
- Jump Game I and II.
- Gas Station start index.
- Minimum arrows to burst balloons.
- Partition labels / chunk partitioning.

## Interview Tips

- Use this 20-second opener:
  "I’ll apply greedy because a local choice can be shown safe by exchange/stay-ahead argument."
- Say the proof sketch before coding:
  why replacing an alternative with your local choice does not worsen outcome.
- Declare sort key if used:
  "Sort by end/start because that makes safe decisions local."
- Narrate invariant while coding:
  farthest reach, last end, current tank, or current segment end.
- Mention fallback:
  "If greedy proof fails, I would switch to DP/backtracking."

## Interviewer Questions While Coding (Important)

| Interviewer asks | How to answer quickly |
|---|---|
| Why greedy is correct here? | Local choice is safe by exchange/stay-ahead argument; it never harms an optimal completion. |
| Why this sort key? | This key makes the provably safe decision visible at each step. |
| Can a counterexample break your rule? | I checked common counterexamples; they still satisfy invariant under this rule. |
| Why not DP? | DP works but is heavier; greedy achieves same optimum with lower complexity given structure. |
| What is your invariant? | State variable (reach/end/tank/etc.) always summarizes best feasible state for processed prefix. |
| Complexity? | Usually linear scan, or `O(n log n)` when sorting dominates. |
| What if ties occur? | Use explicit tie-break preserving proof assumptions. |
| What if no solution exists? | Return prompt-defined sentinel (`-1`/`False`/`0`). |
| Most common bug? | Using a plausible local rule without proof and missing edge counterexample. |

## Practice Ladder (2 Deep Interview Walkthroughs)

### 1) Jump Game

Problem:

- Given `nums`, where `nums[i]` is max jump length from index `i`, determine if you can reach last index.

What interviewer is testing:

- Can you keep a stay-ahead invariant?
- Can you detect failure as soon as index becomes unreachable?
- Can you avoid unnecessary DP/backtracking?

#### What to Say in First 30 Seconds

Use this script:

"Brute force tries all jump paths and can explode combinatorially.  
Greedy invariant: maintain farthest reachable index while scanning left to right.  
If current index is beyond farthest reach, answer is false immediately.  
Otherwise update reach with `max(reach, i + nums[i])`.  
This is linear time and constant space."

#### Solution A: Backtracking DFS

Idea:

- Recursively try all reachable next jumps.

```python
def can_jump_backtracking(nums):
    n = len(nums)

    def dfs(i):
        if i >= n - 1:
            return True
        furthest = min(n - 1, i + nums[i])
        for nxt in range(i + 1, furthest + 1):
            if dfs(nxt):
                return True
        return False

    return dfs(0)
```

Complexity:

- Exponential in worst case.

#### Solution B: DP Reachability

Idea:

- Mark indices reachable from previous reachable positions.

```python
def can_jump_dp(nums):
    n = len(nums)
    reachable = [False] * n
    reachable[0] = True

    for i in range(n):
        if not reachable[i]:
            continue
        for j in range(i + 1, min(n, i + nums[i] + 1)):
            reachable[j] = True

    return reachable[-1]
```

Complexity:

- Time up to `O(n^2)`, Space `O(n)`.

Interviewer tradeoff answer:

- "DP is safer than backtracking but still too slow; greedy reach captures exactly what matters."

#### Solution C: Greedy Farthest Reach (Optimal)

Idea:

- Keep one number: farthest index reachable so far.

```python
def can_jump_optimal(nums):
    reach = 0
    for i, step in enumerate(nums):
        if i > reach:
            return False
        reach = max(reach, i + step)
        if reach >= len(nums) - 1:
            return True
    return True
```

Complexity:

- Time `O(n)`, Space `O(1)`.

What to say while solving with interviewer:

1. "Invariant: all indices `<= reach` are reachable."
2. "If `i > reach`, we are stuck forever."
3. "Update reach greedily with best jump seen so far."
4. "I’ll test `[2,3,1,1,4]` and `[3,2,1,0,4]`."

Common interviewer follow-up and answer:

| Interviewer asks | Good answer |
|---|---|
| Why not pick biggest jump value each step? | Value alone is insufficient; we care about maximum future boundary `i + nums[i]`. |
| Why early failure is safe? | If current index is unreachable, all later indices are unreachable from processed prefix. |
| Could DP ever beat this here? | Not on asymptotic complexity; greedy is optimal for this decision variant. |

### 2) Gas Station

Problem:

- Given `gas` and `cost`, return starting station index to complete circuit once, or `-1` if impossible.

What interviewer is testing:

- Can you separate global feasibility from local candidate reset?
- Can you justify why reset to `i+1` is safe?
- Can you implement one-pass greedy correctly?

#### What to Say in First 30 Seconds

Use this script:

"First, if total gas is less than total cost, no solution exists.  
If feasible globally, greedy one-pass works: maintain running tank and candidate start.  
When tank drops below zero at station `i`, none of starts in current segment can work, so reset start to `i+1` and tank to zero.  
At end, candidate start is valid."

#### Solution A: Try Every Start

Idea:

- Simulate full circuit from each station.

```python
def gas_station_bruteforce(gas, cost):
    n = len(gas)
    for start in range(n):
        tank = 0
        ok = True
        for step in range(n):
            i = (start + step) % n
            tank += gas[i] - cost[i]
            if tank < 0:
                ok = False
                break
        if ok:
            return start
    return -1
```

Complexity:

- Time `O(n^2)`, Space `O(1)`.

#### Solution B: Prefix-Min Rotation View

Idea:

- Build cumulative diff and choose index after minimum prefix if total non-negative.

```python
def gas_station_prefix(gas, cost):
    total = 0
    curr = 0
    min_prefix = float("inf")
    min_idx = -1

    for i in range(len(gas)):
        diff = gas[i] - cost[i]
        total += diff
        curr += diff
        if curr < min_prefix:
            min_prefix = curr
            min_idx = i

    if total < 0:
        return -1
    return (min_idx + 1) % len(gas)
```

Complexity:

- Time `O(n)`, Space `O(1)`.

Interviewer tradeoff answer:

- "This is elegant but less intuitive in interviews than the reset-based greedy pass."

#### Solution C: One-Pass Greedy Reset (Canonical)

Idea:

- Track total diff, current tank, and candidate start.

```python
def gas_station_optimal(gas, cost):
    total = 0
    tank = 0
    start = 0

    for i in range(len(gas)):
        diff = gas[i] - cost[i]
        total += diff
        tank += diff

        if tank < 0:
            start = i + 1
            tank = 0

    return start if total >= 0 else -1
```

Complexity:

- Time `O(n)`, Space `O(1)`.

What to say while solving with interviewer:

1. "Global feasibility is `sum(gas) >= sum(cost)`."
2. "Negative tank at `i` invalidates all starts up to `i`."
3. "So reset start to `i+1` and continue."
4. "I’ll test feasible and infeasible totals."

Common interviewer follow-up and answer:

| Interviewer asks | Good answer |
|---|---|
| Why does reset skip multiple starts safely? | Any earlier start would have even lower tank at failure point, so cannot succeed. |
| Why keep total separately from tank? | `tank` is local segment feasibility; `total` determines global existence. |
| Is answer unique? | For this classic problem, if feasible, returned start is valid and solution is unique per prompt statement. |
