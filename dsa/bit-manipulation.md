# Bit Manipulation (Interview-Ready Guide)

Using `[TOPIC] = Bit Manipulation`.

## 0) Scope (Checklist)
- [x] XOR basics & XOR tricks
- [x] Bit masks, set/clear/toggle
- [x] Power of two checks
- [x] Counting bits (Brian Kernighan)
- [x] Subsets via bitmask
- [x] Bitwise AND/OR properties in ranges
- [x] Two's complement basics

## 1) Foundations
Bit manipulation works directly on binary representation.

Core terms:
- Bit position, mask, shift
- AND `&`, OR `|`, XOR `^`, NOT `~`
- Signed representation (two's complement)

Mental model:
- Treat integer bits like compact boolean arrays.

## 2) How it works
Cause-effect:
1. Build mask `1 << k`.
2. Test: `x & mask`
3. Set: `x | mask`
4. Clear: `x & ~mask`
5. Toggle: `x ^ mask`

Tiny trace (count set bits in `13` = `1101`):
- `n=1101`, `n&(n-1)=1100` count=1
- `1100 -> 1000` count=2
- `1000 -> 0000` count=3
- Answer 3

## 3) Patterns (Interview Templates)
1. Single number with XOR cancelation
2. Mask state compression
3. Subset enumeration over `mask` from `0..(1<<n)-1`
4. Bit-count optimization

Invariants:
- `a ^ a = 0`, `a ^ 0 = a`
- `n & (n-1)` drops lowest set bit
- Power of two has single set bit

Signals:
- "Exactly one/two unique among duplicates"
- "Need compact state for small n"
- "Operations on subsets"

## 4) Examples (Easy -> Medium -> Hard)
1. Easy: Single Number
- Approach: XOR all elements, duplicates cancel.

2. Medium: Counting Bits
- Approach: DP relation `bits[i] = bits[i>>1] + (i&1)` or Kernighan loop.

3. Medium: Subsets
- Approach: iterate masks and include element if bit set.

4. Hard: Single Number III
- Approach: XOR all, split by rightmost set bit.

5. Hard: Maximum XOR of Two Numbers
- Approach: bitwise trie or prefix-set greedy by bit.

## 5) Why & What-if
Edge cases:
- Negative numbers and sign extension
- Large shifts beyond bit-width

Pitfalls:
- Confusing logical vs arithmetic right shift by language
- Overflow with signed ints
- Operator precedence mistakes

Why it works:
- Bit identities provide algebraic guarantees on each position.

Variations:
- Use unsigned types for predictable shifts.
- 64-bit masks when `n > 31`.

## 6) Complexity and Tradeoffs
- Bit ops are `O(1)` each
- Kernighan count: `O(number of set bits)`
- Subset enumeration: `O(2^n * n)` (or `O(2^n)` with bit tricks)

Tradeoffs:
- Very fast and memory efficient but less readable if overused.

## 7) Real-world uses
- Permission flags
- Networking/protocol parsing
- Compression and encoding
- Cryptographic primitives

## 8) Comparisons
- Bitmask set vs hash set:
  - Bitmask faster/smaller for small bounded universe.
  - Hash set for large sparse/unbounded keys.
- XOR tricks vs map counting:
  - XOR elegant for specific duplicate patterns only.

## 9) Retention
Cheat sheet:
- Test/set/clear/toggle with one-bit mask.
- `x & (x-1) == 0` and `x>0` => power of two.
- Enumerate subsets with masks.

Recall hooks:
- "XOR cancels twins."
- "And with one-less removes lowest one."

Practice (10):
1. Easy: Number of 1 Bits
2. Easy: Power of Two
3. Easy: Single Number
4. Medium: Counting Bits
5. Medium: Subsets
6. Medium: Bitwise AND of Numbers Range
7. Medium: Sum of Two Integers (without +)
8. Hard: Single Number III
9. Hard: Maximum XOR of Two Numbers in an Array
10. Hard: Minimum One Bit Operations to Make Integers Zero
