# Pattern 33: Math / Number Theory

## Diagram + Intuition

### Pattern Diagram
```text
problem -> formula/invariant
use gcd/mod/fastpow/combinatorics
```

### Read-the-Question Trigger Cues
- Divisibility, modular cycles, huge exponents, prime logic.

### Intuition Anchor
- "Exploit algebraic structure instead of simulation."

### 3-Second Pattern Check
- Is there a known math identity that collapses complexity?

## What This Pattern Solves
Uses arithmetic structure for efficient solutions beyond brute-force simulation.

## Recognition Signals
- Repeated modular patterns, cyclic behavior, divisibility.
- Need power/exponentiation, gcd/lcm, prime checks.
- Overflow/precision concerns in direct multiplication.

## Core Intuition
Mathematical identities reduce complexity:
- Euclid for GCD
- fast exponentiation for powers
- modulo arithmetic for wrap-around and large numbers
- combinatorics for counting arrangements

## Step-by-Step Method
1. Convert problem statement into formula/invariant.
2. Choose robust numeric method (iterative fast power, gcd loop, sieve).
3. Handle edge cases (`0`, negatives, overflow).
4. Validate on small values and boundary constraints.

## Detailed Example (Fast Power `x^n`)
1. If `n` is even: `x^n = (x^(n/2))^2`.
2. If odd: `x^n = x * x^(n-1)`.
3. Use iterative exponentiation by squaring for `O(log n)`.

## Complexity
- GCD: `O(log min(a, b))`
- Fast power: `O(log n)`
- Sieve of Eratosthenes: `O(n log log n)`

## Python Template (Fast Power)
```python
def fast_pow(x, n):
    if n < 0:
        x, n = 1 / x, -n
    ans = 1.0
    while n:
        if n & 1:
            ans *= x
        x *= x
        n >>= 1
    return ans
```

## Common Pitfalls
- Not handling negative exponents.
- Overflow in languages with fixed integer width.
- Incorrect modulo operation with negative numbers (language-specific behavior).
- Floating-point precision assumptions.

## Variations
- GCD of array / fractions
- Modular exponentiation for large power under mod
- Prime counting/checking
- Combinatorics with factorials and modular inverses

## Interview Tips
- State formulas first; then code.
- Mention time benefit over naive loops.
- Clarify integer vs floating-point expectations in output.

## Practice Problems
- Pow(x, n)
- Rotate Array (mod indexing)
- Greatest Common Divisor of Strings
- Count Primes
