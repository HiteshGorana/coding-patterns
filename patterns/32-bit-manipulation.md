# Pattern 32: Bit Manipulation

## Diagram + Intuition

### Pattern Diagram
```text
mask operations:
set: x | (1<<b)
check: x & (1<<b)
toggle: x ^ (1<<b)
```

### Read-the-Question Trigger Cues
- XOR uniqueness, subset masks, bit count/power-of-two checks.

### Intuition Anchor
- "Use bits as compact boolean array."

### 3-Second Pattern Check
- Can binary properties replace heavier data structures?

## What This Pattern Solves
Uses binary-level operations for efficient state handling, parity tricks, and constant-space solutions.

## Recognition Signals
- XOR uniqueness problems.
- Need subset/state compression.
- Need fast checks on powers of two, bit counts, masks.

## Core Intuition
Bits enable compact representation and algebraic properties:
- `x ^ x = 0`
- `x ^ 0 = x`
- `x & (x - 1)` clears lowest set bit
- shifts multiply/divide by powers of two

## Step-by-Step Method
1. Identify target bit property (single number, mask membership, toggling).
2. Choose operation: `&`, `|`, `^`, `~`, `<<`, `>>`.
3. Maintain mask/invariant carefully.
4. Validate with small binary examples.

## Detailed Example (Single Number)
Array where every number appears twice except one:
1. XOR all elements.
2. Pairs cancel out.
3. Result is unique element.

## Complexity
- Often `O(n)` time, `O(1)` space
- Bitmask DP can be `O(n * 2^n)` depending state size

## Python Template
```python
def single_number(nums):
    ans = 0
    for x in nums:
        ans ^= x
    return ans
```

## Common Pitfalls
- Signed right-shift behavior differences across languages.
- Forgetting to mask when simulating fixed-width integers.
- Operator precedence mistakes (`&` vs `==` grouping).
- Overusing bit tricks where clearer logic is acceptable.

## Variations
- Counting Bits
- Single Number II/III
- Subsets via bitmask
- Maximum XOR of Two Numbers in an Array

## Interview Tips
- Explain binary property in plain words before code.
- Show one tiny binary trace to prove operation.
- Mention readability tradeoff; avoid opaque tricks without explanation.

## Practice Problems
- Single Number
- Counting Bits
- Subsets
- Single Number III
