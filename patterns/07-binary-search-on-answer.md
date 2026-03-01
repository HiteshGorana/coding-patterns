# Pattern 07: Binary Search on Answer

## At a Glance

| Item | Summary |
|---|---|
| Use when | You need minimum/maximum value satisfying a monotonic feasibility condition |
| Main tradeoff | Fast search over answer range, but correctness depends on a valid monotonic `can(x)` |
| Typical runtime | `O(C * log R)` where `C` is feasibility-check cost |
| Main structures | numeric bounds (`low/high`), midpoint guess, feasibility predicate |
| Common prompts | minimum feasible rate/capacity/time, maximum feasible threshold, optimize worst-case bound |

## Related Playbook

- Full interview question set for this pattern:
  [Pattern 07 Top 10 Questions Playbook](./questions/07-binary-search-on-answer-top-10-questions.md)

## Diagram + Intuition

### Pattern Diagram

```text
Search over value range, not index range:

low ------------------ mid ------------------ high
           guess = mid, run can(mid)

If finding minimum feasible:
  can(mid) == True  -> keep left half (high = mid)
  can(mid) == False -> keep right half (low = mid + 1)

If finding maximum feasible:
  can(mid) == True  -> keep right half (low = mid)
  can(mid) == False -> keep left half (high = mid - 1)
```

### Read-the-Question Trigger Cues

- Prompt asks for "minimum feasible" or "maximum feasible" numeric answer.
- You can quickly check whether a guessed answer works.
- Feasibility is monotonic (once true, remains true on one side).
- Direct optimization search is expensive but verification is manageable.

### Intuition Anchor

- "I may not construct the optimal answer directly, but I can verify a guess."

### 3-Second Pattern Check

- Is there a monotonic relation between answer and feasibility?
- Can I define `can(x)` in linear or near-linear time?
- Can I set safe bounds that contain the true answer?

## Decision Table: What to Store

| Prompt shape | Structure | Key -> value | Typical query |
|---|---|---|---|
| minimum feasible value | integer bounds + predicate | `x -> can(x)` | first true |
| maximum feasible value | integer bounds + predicate | `x -> can(x)` | last true |
| capacity/rate minimization | bounds from constraints | `x -> days/hours needed` | `needed <= limit` |
| partition/load minimization | bounds `max(nums)..sum(nums)` | `x -> pieces needed` | `pieces <= k` |
| distance maximization | sorted positions + predicate | `x -> can place count` | `count >= target` |
| real-valued threshold | float bounds + epsilon | `x -> can(x)` | converge within precision |

## Universal Invariant

Before coding, say this sentence out loud:

- "My current search interval always contains the optimal boundary answer, and each predicate decision discards only impossible values."

If this invariant is unclear, the implementation will usually fail on edge cases.

## Step-by-Step Method (Easy Version)

Use this exact flow while coding:

1. Write the default return first (or define impossible case behavior).
2. Define predicate `can(x)` with clear contract and complexity.
3. Derive safe bounds `[low, high]` that must contain the answer.
4. Decide boundary type: first true (min feasible) or last true (max feasible).
5. Binary search with monotonic-safe updates until converged.
6. Return boundary and optionally validate if prompt permits "no feasible solution."
7. State complexity as `check_cost * log(search_range)`.

Fill-in template:

```python
def optimize(low, high):
    while low < high:
        mid = low + (high - low) // 2
        if can(mid):
            high = mid        # min feasible
        else:
            low = mid + 1
    return low
```

## Query/Update Order Rules

### A) First true boundary (minimum feasible)

Use when feasible values are on the right side of threshold.

```python
while low < high:
    mid = low + (high - low) // 2
    if can(mid):
        high = mid
    else:
        low = mid + 1
```

### B) Last true boundary (maximum feasible)

Use when feasible values are on the left side or when maximizing feasible value.

```python
while low < high:
    mid = low + (high - low + 1) // 2  # upper mid
    if can(mid):
        low = mid
    else:
        high = mid - 1
```

### C) Two-pass (discover bounds, then binary search)

Use when upper bound is unknown initially.

```python
low, high = 0, 1
while not can(high):
    high *= 2
    low = high // 2

# then run standard boundary binary search on [low, high]
```

## Detailed Example (Koko Eating Bananas)

**Input:** `piles = [3, 6, 7, 11], h = 8`

1. Bounds: `low = 1`, `high = 11`.
2. Guess `mid = 6`: hours needed = `1+1+2+2 = 6` (feasible), move left (`high = 6`).
3. Guess `mid = 3`: hours = `1+2+3+4 = 10` (not feasible), move right (`low = 4`).
4. Guess `mid = 5`: hours = `1+2+2+3 = 8` (feasible), move left (`high = 5`).
5. Guess `mid = 4`: hours = `1+2+2+3 = 8` (feasible), move left (`high = 4`).
6. Converged at `4`, minimum feasible speed is `4`.

Why it works: feasibility transitions from false to true once, so first-true boundary is the optimal answer.

## Reusable Python Templates

### 1) Membership (Feasibility Predicate Skeleton)

```python
def can_finish_with_limit(nums, limit):
    # Example contract: return True if current guess `limit` is feasible.
    used = 1
    curr = 0

    for x in nums:
        if x > limit:
            return False
        if curr + x <= limit:
            curr += x
        else:
            used += 1
            curr = x

    return True
```

Example:

```python
can_finish_with_limit([7, 2, 5, 10, 8], 18)  # True
can_finish_with_limit([7, 2, 5, 10, 8], 14)  # False
```

### 2) Minimum Feasible Integer

```python
def min_feasible(low, high, can):
    while low < high:
        mid = low + (high - low) // 2
        if can(mid):
            high = mid
        else:
            low = mid + 1
    return low
```

Example:

```python
arr = [3, 6, 7, 11]
h = 8
min_feasible(1, max(arr), lambda k: sum((x + k - 1) // k for x in arr) <= h)  # 4
```

### 3) Maximum Feasible Integer

```python
def max_feasible(low, high, can):
    while low < high:
        mid = low + (high - low + 1) // 2
        if can(mid):
            low = mid
        else:
            high = mid - 1
    return low
```

Example:

```python
max_feasible(0, 10, lambda x: x * x <= 30)  # 5
max_feasible(0, 10, lambda x: x <= 7)       # 7
```

### 4) Real-Valued Binary Search (Precision)

```python
def min_feasible_float(low, high, can, eps=1e-6):
    while high - low > eps:
        mid = (low + high) / 2.0
        if can(mid):
            high = mid
        else:
            low = mid
    return high
```

Example:

```python
min_feasible_float(0.0, 10.0, lambda x: x * x >= 2.0, 1e-7)  # approx sqrt(2)
```

## Complexity

Let:

- `R` = size of answer range (`high - low + 1` for integers).
- `C` = time complexity of one feasibility check `can(x)`.

Per-operation cost:

- Midpoint and boundary update: `O(1)`.
- Feasibility check: `O(C)`.

End-to-end cost (most interview problems):

| Variant | Time (average) | Space |
|---|---|---|
| minimum feasible integer | `O(C * log R)` | `O(1)` + check state |
| maximum feasible integer | `O(C * log R)` | `O(1)` + check state |
| unknown bound + doubling + search | `O(C * (log A + log R))` | `O(1)` |
| real-valued search with precision `eps` | `O(C * log((high-low)/eps))` | `O(1)` |
| two boundary searches | `O(C * log R)` each | `O(1)` |

Interview note:

- Dominant cost is almost always `can(mid)`.
- Tight initial bounds reduce iterations but do not change asymptotic complexity.

## Edge-Case Checklist (Pre-Submit)

Use this as a final pass before you finish coding.

### Contract Checks

- Return type matches prompt exactly (integer/float/capacity/rate).
- If no feasible answer is possible, behavior is explicitly defined.
- For floating answers, precision requirement (`eps`) matches prompt.
- Boundary answer is correct variant (first true vs last true).

### Data-Rule Checks

- Predicate `can(x)` is monotonic and side direction is proven.
- Bounds `[low, high]` actually contain a valid answer.
- Midpoint formula matches variant (`lower mid` vs `upper mid`).
- Update rules strictly shrink interval and guarantee progress.
- Integer division/ceiling logic inside `can` is correct.

### Input Boundary Checks

- Smallest input sizes are handled safely.
- Single-value answer ranges converge correctly.
- Very large bounds avoid overflow-prone formulas.
- Extreme constraint values (tight limits or huge limits) are handled.
- All-equal or highly skewed inputs still satisfy feasibility logic.

### Pattern-Specific Checks

- Min-feasible variant uses `high = mid` on success.
- Max-feasible variant uses upper mid and `low = mid` on success.
- `can(mid)` has no hidden side effects across iterations.
- For partition/load problems, check greedily with correct reset behavior.

### Quick Sanity Tests (Run Mentally)

| Scenario | Example | What should happen |
|---|---|---|
| answer at lower bound | `low` already feasible | returns `low` |
| answer at upper bound | only `high` feasible | returns `high` |
| tight one-step range | `low + 1 == high` | converges in one iteration |
| impossible mid logic bug | non-monotonic `can` | detect and fix predicate |
| large values | big bounds and sums | still converges without overflow |

## Common Pitfalls

- Predicate is not truly monotonic, breaking binary-search correctness.
- Bounds do not include the true answer.
- Using min-feasible update rules for max-feasible problem (or vice versa).
- Wrong midpoint rounding causing infinite loops in max-feasible form.
- Arithmetic mistakes in `can(mid)` (especially ceiling division and resets).

## When Not Ideal

- No monotonic feasible/infeasible split exists.
- Feasibility check itself is too expensive to run `log R` times.
- Exact combinatorial optimum is required and cannot be checked via monotonic predicate.
- Search domain is tiny; direct enumeration may be simpler and sufficient.

## Variations

- Minimize maximum load/capacity/time.
- Maximize minimum distance/threshold.
- Real-number binary search with epsilon precision.
- Binary search + greedy feasibility.
- Binary search + DP feasibility (when greedy is insufficient).

## Interview Tips

- Use this 20-second opener:
  "I will binary-search the answer value because feasibility is monotonic; I can verify each guess with `can(mid)`."
- Define monotonicity explicitly before coding:
  "If `x` is feasible, all larger/smaller values are feasible in this direction."
- Write `can(x)` first and test it independently on small values.
- Declare boundary type:
  first true (minimum feasible) or last true (maximum feasible).
- Mention dominant complexity:
  check cost times logarithmic number of guesses.

## Interviewer Questions While Coding (Important)

| Interviewer asks | How to answer quickly |
|---|---|
| Why binary search on answer? | Feasibility is monotonic over numeric answer space, so each check discards half the range. |
| What is your predicate? | `can(x)` returns whether guess `x` satisfies problem constraints. |
| How do you prove monotonicity? | Show feasible set shape: once true (or false), it stays that way in one direction. |
| How did you choose bounds? | Use tight provable limits from constraints (`max(nums)`, `sum(nums)`, etc.). |
| Why this midpoint formula? | Prevent overflow and ensure convergence (`upper mid` for max-feasible). |
| Complexity? | `O(C * log R)` where `C` is one feasibility check cost. |
| What if no feasible answer exists? | Add validation step or impossible-case return as required by prompt. |
| Most common bug? | Incorrect predicate monotonicity or wrong update direction. |
| How to handle floats? | Binary search until interval width is below epsilon. |

## Practice Ladder (2 Deep Interview Walkthroughs)

### 1) Koko Eating Bananas

Problem:

- Given `piles` and `h` hours, find minimum integer eating speed `k` so all bananas are eaten within `h`.

What interviewer is testing:

- Can you identify min-feasible boundary?
- Can you write correct ceiling arithmetic in `can(k)`?
- Can you choose correct bounds and updates?

#### What to Say in First 30 Seconds

Use this script:

"I cannot directly compute best speed, but I can check if a speed works.  
Feasibility is monotonic: if speed `k` works, any larger speed also works.  
So I binary-search `k` in `[1, max(piles)]` and use `can(k)` that sums required hours with ceiling division.  
This gives `O(n log maxPile)` time."

#### Solution A: Brute Force Scan of Speeds

Idea:

- Try each speed from `1` to `max(piles)` and return first feasible one.

```python
def min_speed_bruteforce(piles, h):
    max_pile = max(piles)
    for k in range(1, max_pile + 1):
        hours = 0
        for x in piles:
            hours += (x + k - 1) // k
        if hours <= h:
            return k
    return max_pile
```

Complexity:

- Time `O(n * max(piles))`, Space `O(1)`.

#### Solution B: Tight-Bound Enumeration

Idea:

- Start from tighter lower bound `ceil(sum(piles)/h)` instead of `1`.

```python
def min_speed_tighter_scan(piles, h):
    total = sum(piles)
    low = max(1, (total + h - 1) // h)
    high = max(piles)

    for k in range(low, high + 1):
        hours = 0
        for x in piles:
            hours += (x + k - 1) // k
        if hours <= h:
            return k
    return high
```

Complexity:

- Time `O(n * (high - low + 1))`, Space `O(1)`.

Interviewer tradeoff answer:

- "Tighter bounds help in practice, but worst-case range is still large; binary search gives guaranteed logarithmic guesses."

#### Solution C: Binary Search on Answer (Optimal)

Idea:

- Search first feasible speed with monotonic predicate.

```python
def min_eating_speed(piles, h):
    def can(k):
        hours = 0
        for x in piles:
            hours += (x + k - 1) // k
        return hours <= h

    low, high = 1, max(piles)
    while low < high:
        mid = low + (high - low) // 2
        if can(mid):
            high = mid
        else:
            low = mid + 1
    return low
```

Complexity:

- Time `O(n log max(piles))`, Space `O(1)`.

What to say while solving with interviewer:

1. "Predicate: speed `k` is feasible if total hours `<= h`."
2. "If feasible at `k`, any larger speed is also feasible."
3. "So we search first true boundary."
4. "I will test with `piles=[3,6,7,11], h=8`."

Common interviewer follow-up and answer:

| Interviewer asks | Good answer |
|---|---|
| Why ceiling division? | Partial pile still consumes a full hour, so we need `ceil(pile/k)`. |
| Why is low bound 1? | Speed is positive integer and 1 is always the minimum legal guess. |
| Could speed be above max pile? | Unnecessary; `max(pile)` already finishes each pile in at most one hour. |

### 2) Split Array Largest Sum

Problem:

- Split array `nums` into `k` non-empty contiguous subarrays to minimize the largest subarray sum.

What interviewer is testing:

- Can you transform optimization into feasibility?
- Can you compare DP vs binary-search-on-answer tradeoff?
- Can you implement greedy check for partition count correctly?

#### What to Say in First 30 Seconds

Use this script:

"Answer is the maximum subarray sum after split; I cannot directly optimize it greedily, but I can test a guess `x`.  
`can(x)` asks whether I can split into at most `k` parts such that each part sum is `<= x`.  
This predicate is monotonic, so I binary-search `x` over `[max(nums), sum(nums)]`.  
Greedy counting of partitions gives `O(n)` check, total `O(n log sum(nums))`."

#### Solution A: Brute Force Partition Enumeration

Idea:

- Try all possible cut placements recursively and minimize worst segment sum.

```python
def split_array_bruteforce(nums, k):
    n = len(nums)
    best = float("inf")

    def dfs(start, parts_left, current_max):
        nonlocal best
        if parts_left == 1:
            best = min(best, max(current_max, sum(nums[start:])))
            return

        s = 0
        # leave at least one element for each remaining part
        for end in range(start, n - parts_left + 1):
            s += nums[end]
            dfs(end + 1, parts_left - 1, max(current_max, s))

    dfs(0, k, 0)
    return best
```

Complexity:

- Exponential in worst case; impractical for large `n`.

#### Solution B: Dynamic Programming

Idea:

- `dp[i][p]` = minimal possible largest sum for first `i` elements in `p` parts.

```python
def split_array_dp(nums, k):
    n = len(nums)
    prefix = [0]
    for x in nums:
        prefix.append(prefix[-1] + x)

    INF = 10**18
    dp = [[INF] * (k + 1) for _ in range(n + 1)]
    dp[0][0] = 0

    for i in range(1, n + 1):
        for p in range(1, min(i, k) + 1):
            for j in range(p - 1, i):
                last = prefix[i] - prefix[j]
                dp[i][p] = min(dp[i][p], max(dp[j][p - 1], last))

    return dp[n][k]
```

Complexity:

- Time `O(n^2 * k)`, Space `O(n * k)`.

Interviewer tradeoff answer:

- "DP is exact and clearer mathematically, but too heavy at scale; binary search with greedy feasibility is much faster."

#### Solution C: Binary Search + Greedy Feasibility (Optimal)

Idea:

- Check if guess `limit` can keep partition count `<= k`.

```python
def split_array_optimal(nums, k):
    def can(limit):
        parts = 1
        running = 0
        for x in nums:
            if x > limit:
                return False
            if running + x <= limit:
                running += x
            else:
                parts += 1
                running = x
        return parts <= k

    low, high = max(nums), sum(nums)
    while low < high:
        mid = low + (high - low) // 2
        if can(mid):
            high = mid
        else:
            low = mid + 1
    return low
```

Complexity:

- Time `O(n log(sum(nums) - max(nums) + 1))`, Space `O(1)`.

What to say while solving with interviewer:

1. "Predicate asks whether partition count needed under `limit` is at most `k`."
2. "Greedy is valid because extending current partition is always best until limit is exceeded."
3. "Feasible limits form a monotonic suffix."
4. "I will test small `k=1`, `k=n`, and mixed values."

Common interviewer follow-up and answer:

| Interviewer asks | Good answer |
|---|---|
| Why bounds `max(nums)` to `sum(nums)`? | Largest part cannot be below max element or above total sum. |
| Why `parts <= k` and not exactly `k`? | If we can do fewer parts, we can split further without increasing max part sum. |
| Why greedy check works? | Delaying a forced split never reduces partitions needed under fixed limit. |
