# Math & Number Theory (Interview-Ready Guide)

Using `[TOPIC] = Math & Number Theory`.

## 0) Scope (Checklist)
- [x] GCD/LCM, Euclid
- [x] Modular arithmetic basics
- [x] Fast exponentiation
- [x] Primes, sieve basics
- [x] Combinatorics basics (`nCr`)
- [x] Overflow/precision pitfalls

## 1) Foundations
Math patterns reduce brute-force loops through numeric properties.

Core terms:
- Divisor, multiple, prime, composite
- Congruence (`a % m`)
- Modular inverse (when applicable)
- Overflow and precision limits

Mental model:
- Replace repeated work with formulas and algebraic invariants.

## 2) How it works
Cause-effect:
1. Use Euclid to reduce GCD quickly: `gcd(a,b)=gcd(b,a%b)`.
2. Use exponentiation by squaring to reduce power multiplications.
3. Use sieve to mark composites once for many prime queries.

Tiny trace (`pow(3,5)`):
- `5` odd -> result*=3, `n=4`
- square base `3->9`, `n=2`
- square base `9->81`, `n=1`
- odd -> result*=81 => `243`

## 3) Patterns (Interview Templates)
1. GCD normalization and fraction reduction
2. Modular counting and cyclic patterns
3. Fast pow / modular pow
4. Sieve preprocess + query
5. Combinatorics with factorial/precompute mod

Invariants:
- `a = q*b + r` in Euclid
- `(x+y)%m`, `(x*y)%m` distributive rules
- Fast pow keeps same mathematical value while halving exponent

Signals:
- "Huge exponent"
- "Repeated prime checks"
- "Periodic/cycle in remainders"

## 4) Examples (Easy -> Medium -> Hard)
1. Easy: GCD of Array
- Approach: fold with Euclid.

2. Medium: Count Primes
- Approach: sieve of Eratosthenes.

3. Medium: Pow(x, n)
- Approach: fast exponentiation.

4. Hard: Subarray sums divisible by K
- Approach: prefix remainder frequency counting.

5. Hard: nCr mod p (large n)
- Approach: precompute factorials/inverses (prime mod case).

## 5) Why & What-if
Edge cases:
- Zero and negative inputs
- Mod by 1
- Large multiplication overflow

Pitfalls:
- Integer overflow before modulo
- Floating point precision for exact integer tasks
- Assuming modular inverse exists for non-coprime values

Why it works:
- Number-theoretic identities provide exact reductions.

Variations:
- Use `long long`/`BigInt` for large ranges.
- For non-prime modulus, inverse handling changes.

## 6) Complexity and Tradeoffs
- Euclid GCD: `O(log min(a,b))`
- Fast pow: `O(log n)`
- Sieve up to `N`: `O(N log log N)` time, `O(N)` space

Tradeoffs:
- Precomputation accelerates many queries but costs memory/time upfront.

## 7) Real-world uses
- Cryptography and key exchange
- Hashing and modular arithmetic in algorithms
- Time/period scheduling with LCM
- Probabilistic counting and combinatorics

## 8) Comparisons
- Trial division vs sieve:
  - Trial for few checks, sieve for many.
- Naive exponentiation vs fast pow:
  - `O(n)` vs `O(log n)`.

## 9) Retention
Cheat sheet:
- GCD by Euclid
- LCM via `a/gcd(a,b)*b`
- Modular arithmetic properties
- Sieve for many primes

Recall hooks:
- "Modulo early, modulo often."
- "Halve exponent, square base."

Practice (10):
1. Easy: Plus One
2. Easy: Palindrome Number
3. Medium: Pow(x, n)
4. Medium: Count Primes
5. Medium: Happy Number
6. Medium: Fraction to Recurring Decimal
7. Medium: Subarray Sums Divisible by K
8. Hard: Super Pow
9. Hard: Nth Magical Number
10. Hard: Count Different Subsequences GCDs
