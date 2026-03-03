# Bit Manipulation: A Deep Dive

---

## 1. What Is It? (Definition & Core Components)

**Bit manipulation** is the act of directly operating on the individual binary digits (bits) of integers using bitwise operators — working at the lowest level of data representation that software can access. Instead of treating a number as an abstract mathematical quantity, bit manipulation treats it as a **sequence of 0s and 1s** and operates on those digits directly, one bit at a time or all bits simultaneously.

```
NORMAL ARITHMETIC VIEW:        BIT MANIPULATION VIEW:

  42 + 7 = 49                    42 = 0 0 1 0 1 0 1 0
  "add these numbers"             7 = 0 0 0 0 0 1 1 1
                                  &   ───────────────
                                      0 0 0 0 0 0 1 0  = 2
                                  "AND every pair of bits"

  Same integer, two worldviews.
  Arithmetic: treats number as a whole.
  Bitwise:    treats number as 32 or 64 individual switches.
```

**Core components:**

- **Bit** — a single binary digit, either 0 or 1; the smallest unit of information
- **Byte** — 8 bits grouped together; can represent 256 values (0–255)
- **Integer representation** — modern systems use 32-bit or 64-bit integers stored in two's complement
- **Bitwise operators** — the six fundamental operations: AND (`&`), OR (`|`), XOR (`^`), NOT (`~`), left shift (`<<`), right shift (`>>`)
- **Bit position** — the index of a bit, counted from 0 at the rightmost (least significant) position
- **LSB** — Least Significant Bit; the rightmost bit; represents 2⁰ = 1; determines odd/even
- **MSB** — Most Significant Bit; the leftmost bit; represents 2^(n-1); in two's complement, the sign bit
- **Two's complement** — the standard representation of signed integers in all modern hardware
- **Mask** — a bit pattern used with AND/OR/XOR to isolate, set, or flip specific bits

---

## 2. Binary Number Representation

Before manipulating bits, you must see numbers as their binary representation.

### Positive Integers

```
DECIMAL TO BINARY CONVERSION:

  Decimal 42:
    42 ÷ 2 = 21 remainder 0   ← LSB
    21 ÷ 2 = 10 remainder 1
    10 ÷ 2 =  5 remainder 0
     5 ÷ 2 =  2 remainder 1
     2 ÷ 2 =  1 remainder 0
     1 ÷ 2 =  0 remainder 1   ← MSB
    Read remainders bottom-up: 101010

  42 in binary = 00101010 (8-bit)

POSITIONAL VALUE VERIFICATION:
  Position:  7    6    5    4    3    2    1    0
  Bit:       0    0    1    0    1    0    1    0
  Value:   128   64   32   16    8    4    2    1
  Contribution: 0 + 0 + 32 + 0 + 8 + 0 + 2 + 0 = 42 ✅

QUICK POWERS OF 2 (must memorize):
  2⁰  = 1        2⁴  = 16       2⁸  = 256
  2¹  = 2        2⁵  = 32       2¹⁰ = 1,024
  2²  = 4        2⁶  = 64       2¹⁶ = 65,536
  2³  = 8        2⁷  = 128      2³² = 4,294,967,296
```

### Two's Complement — How Signed Integers Work

```
TWO'S COMPLEMENT for n-bit integers:

  Positive numbers:  stored normally, MSB = 0
  Negative numbers:  MSB = 1; value = -(2^n) + sum of remaining bits

8-BIT EXAMPLES:
   127 = 0111 1111   (max positive)
     1 = 0000 0001
     0 = 0000 0000
    -1 = 1111 1111   ← NOT -1 in binary, but 255 unsigned
    -2 = 1111 1110
  -128 = 1000 0000   (min negative)

TO NEGATE a number in two's complement:
  Step 1: Flip all bits (bitwise NOT)
  Step 2: Add 1

  Negate 5:
    5  = 0000 0101
  flip = 1111 1010
   + 1 = 1111 1011 = -5 ✅

  Verify: -5 = -128 + 64 + 32 + 16 + 8 + 2 + 1
             = -128 + 123 = -5 ✅

WHY TWO'S COMPLEMENT?
  Addition works the same for positive and negative numbers.
  No special "negative addition" circuitry needed.
  5 + (-5) = 0000 0101 + 1111 1011 = 1 0000 0000 → overflow discarded → 0000 0000 = 0 ✅
```

---

## 3. The Six Bitwise Operators

### AND ( & ) — Both Must Be 1

```
RULE: Output bit is 1 only if BOTH input bits are 1.

  0 & 0 = 0        1 & 0 = 0
  0 & 1 = 0        1 & 1 = 1    ← only this case

TRUTH TABLE:
  A  B  A&B
  0  0   0
  0  1   0
  1  0   0
  1  1   1

EXAMPLE:  42 & 15
  42 = 0010 1010
  15 = 0000 1111
  &    ─────────
       0000 1010 = 10

ANALOGY: AND is a FILTER or MASK.
  The 1s in the mask SAY "keep these bits."
  The 0s in the mask SAY "zero out these bits."
  15 = 0000 1111 keeps only the lower 4 bits of 42.

APPLICATIONS:
  Check if bit k is set: n & (1 << k) != 0
  Extract lower k bits:  n & ((1 << k) - 1)
  Check if even:         n & 1 == 0  (LSB = 0 means even)
  Clear specific bits:   n & ~mask
```

### OR ( | ) — At Least One Must Be 1

```
RULE: Output bit is 1 if EITHER (or both) input bits are 1.

  0 | 0 = 0
  0 | 1 = 1        1 | 0 = 1
  1 | 1 = 1

EXAMPLE:  42 | 15
  42 = 0010 1010
  15 = 0000 1111
  |    ─────────
       0010 1111 = 47

ANALOGY: OR is a SETTER or COMBINER.
  Forces specific bits to 1.
  Combines two bitmasks into one.

APPLICATIONS:
  Set bit k:         n | (1 << k)
  Combine flags:     READ | WRITE | EXECUTE
  Set lower k bits:  n | ((1 << k) - 1)
```

### XOR ( ^ ) — Exactly One Must Be 1

```
RULE: Output bit is 1 if input bits are DIFFERENT (eXclusive OR).

  0 ^ 0 = 0    (same → 0)
  1 ^ 1 = 0    (same → 0)
  0 ^ 1 = 1    (different → 1)
  1 ^ 0 = 1    (different → 1)

EXAMPLE:  42 ^ 15
  42 = 0010 1010
  15 = 0000 1111
  ^    ─────────
       0010 0101 = 37

MAGICAL PROPERTIES OF XOR:
  1. a ^ a = 0          (anything XOR itself = 0)
  2. a ^ 0 = a          (anything XOR 0 = itself)
  3. Commutative: a ^ b = b ^ a
  4. Associative: (a^b)^c = a^(b^c)
  5. Self-inverse: (a^b)^b = a  ← XOR is its own inverse!

Property 5 is the key:
  Encrypt: message ^ key = ciphertext
  Decrypt: ciphertext ^ key = (message ^ key) ^ key = message ✅

ANALOGY: XOR is a TOGGLER or DIFFERENCER.
  Shows where two numbers DIFFER.
  Toggles specific bits between 0 and 1.

APPLICATIONS:
  Toggle bit k:          n ^ (1 << k)
  Swap without temp:     a ^= b; b ^= a; a ^= b
  Find single unique:    XOR all elements, duplicates cancel to 0
  Detect difference:     a ^ b shows which bits differ
```

### NOT ( ~ ) — Flip Every Bit

```
RULE: Flip all bits. 0 becomes 1, 1 becomes 0.

  ~0000 0101 = 1111 1010

In two's complement: ~n = -(n+1)
  ~5  = -6
  ~42 = -43
  ~0  = -1   ← all 1s in two's complement = -1
  ~(-1) = 0  ← all 0s

EXAMPLE:
  ~42:
  42  = 0010 1010
  ~42 = 1101 0101 = -43 (in two's complement) ✅

APPLICATIONS:
  Create inverted mask:  ~mask
  Clear bit k:           n & ~(1 << k)
  Negate + adjust:       ~n = -(n+1), so n = ~(-n-1)
```

### Left Shift ( << ) — Multiply by Powers of 2

```
RULE: Shift all bits LEFT by k positions.
      Fill right side with 0s.
      Leftmost bits that "fall off" are discarded.

EFFECT: n << k = n × 2^k  (for values that don't overflow)

  5 << 1 = 10    (5 × 2¹)
  5 << 2 = 20    (5 × 2²)
  5 << 3 = 40    (5 × 2³)

EXAMPLE: 5 << 3
  5   = 0000 0101
  <<3 = 0010 1000 = 40 ✅

VISUAL:
  0 0 0 0 0 1 0 1      (5)
  ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓  shift left 3
  0 0 1 0 1 0 0 0      (40)
  └───────────────┘
       fills with 0s on right, drops bits off left

CREATING MASKS:
  1 << k creates a mask with only bit k set:
  1 << 0 = 0000 0001  (mask for bit 0)
  1 << 3 = 0000 1000  (mask for bit 3)
  1 << 7 = 1000 0000  (mask for bit 7)

OVERFLOW CAUTION:
  In 32-bit int: 1 << 31 sets the sign bit → negative number!
  Use 1L << k or 1n << k for larger shifts.
```

### Right Shift ( >> ) — Divide by Powers of 2

```
RULE: Shift all bits RIGHT by k positions.
      Rightmost bits "fall off" (discarded).
      Left fill depends on sign:

LOGICAL RIGHT SHIFT (>>> in Java, >> for unsigned in C):
  Always fills with 0s.
  Treats number as unsigned.

ARITHMETIC RIGHT SHIFT (>> in most languages):
  Fills with the SIGN BIT (0 for positive, 1 for negative).
  Preserves the sign of the number.
  Equivalent to floor division by 2^k.

EXAMPLE: Arithmetic right shift
  40 >> 3:
  40  = 0010 1000
  >>3 = 0000 0101 = 5   (fills with 0, positive number) ✅
  40 / 8 = 5 ✅

  -40 >> 3 (arithmetic):
  -40 = 1101 1000
  >>3 = 1111 1011 = -5   (fills with 1, negative number)
  ⌊-40 / 8⌋ = -5 ✅

  -40 >>> 3 (logical, Java):
  -40 = 1101 1000 (with 32-bit sign extension = 1111...1101 1000)
  >>>3 = 0001 1111...1111 1011 = 536870907 (large positive number) ⚠️

APPLICATIONS:
  Divide by 2^k:    n >> k
  Extract bit k:    (n >> k) & 1
  Get sign bit:     n >> 31  (0 for positive, -1 for negative in arithmetic)
```

---

## 4. The Physical Analogy: A Row of Light Switches

Imagine an integer as a panel of 8 light switches (bits), each either ON (1) or OFF (0):

```
LIGHT SWITCH PANEL for 42 = 00101010:

  Switch: [7][6][5][4][3][2][1][0]
  State:  [○][○][●][○][●][○][●][○]   ● = ON(1), ○ = OFF(0)
  Value:  [0][0][1][0][1][0][1][0]

AND: Two panels. Output ON only where BOTH are ON.
  "Need both switches on to light the room"

OR:  Two panels. Output ON where EITHER is ON.
  "Either switch can light the room"

XOR: Two panels. Output ON where EXACTLY ONE is ON.
  "Exactly one switch lights the room; both on = off"

NOT: Flip every switch on the panel.
  "Emergency invert — flip every switch"

<<3: Slide all switches 3 positions LEFT.
  New right switches are all OFF.
  "The whole pattern shifts left"

>>3: Slide all switches 3 positions RIGHT.
  New left switches match the original leftmost switch.
  "The whole pattern shifts right"
```

This mental model makes bitwise operations concrete: you're not doing arithmetic, you're **physically toggling switches in a panel**, independently for each position.

---

## 5. Core Bit Manipulation Techniques

### The Essential Toolkit

```
Given integer n and bit position k (0-indexed from right):

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
CHECK if bit k is set:
  n & (1 << k) != 0

  n=42=00101010, k=3: 42 & (1<<3) = 42 & 8 = 00101010 & 00001000
                                            = 00001000 = 8 ≠ 0 → SET ✅
  n=42, k=2:          42 & (1<<2) = 42 & 4 = 00101010 & 00000100
                                            = 00000000 = 0 → NOT SET ✅

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
SET bit k (force to 1):
  n | (1 << k)

  n=42=00101010, k=2: 42 | (1<<2) = 42 | 4 = 00101010 | 00000100
                                           = 00101110 = 46 ✅

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
CLEAR bit k (force to 0):
  n & ~(1 << k)

  n=42=00101010, k=3: ~(1<<3) = ~8 = 11110111
                      42 & ~8 = 00101010 & 11110111
                              = 00100010 = 34 ✅

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
TOGGLE bit k (flip 0↔1):
  n ^ (1 << k)

  n=42=00101010, k=2: 42 ^ (1<<2) = 42 ^ 4 = 00101010 ^ 00000100
                                           = 00101110 = 46 (was 0, now 1)
  n=42, k=1:          42 ^ (1<<1) = 42 ^ 2 = 00101010 ^ 00000010
                                           = 00101000 = 40 (was 1, now 0) ✅

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
GET value of bit k (0 or 1):
  (n >> k) & 1

  n=42, k=3: (42>>3) & 1 = 5 & 1 = 0000 0101 & 0000 0001 = 1 ✅
  n=42, k=2: (42>>2) & 1 = 10 & 1 = 0000 1010 & 0000 0001 = 0 ✅

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
CLEAR lowest set bit (turn off rightmost 1):
  n & (n - 1)

  n=12=1100: 12 & 11 = 1100 & 1011 = 1000 = 8 ✅
  WHY? n-1 flips the lowest set bit AND all bits below it.
  n    = ...1 0 0 0 0   (lowest set bit and trailing zeros)
  n-1  = ...0 1 1 1 1   (borrow propagates through trailing zeros)
  n&(n-1) = ...0 0 0 0 0  ← lowest set bit cleared ✅

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
ISOLATE lowest set bit (keep only rightmost 1):
  n & (-n)   or equivalently  n & (~n + 1)

  n=12=1100: -12 in two's complement = 0100
             12 & (-12) = 1100 & 0100 = 0100 = 4 ✅
             (bit position 2, value 4 = 2²)
  WHY? -n = ~n + 1. The +1 propagates through trailing zeros,
       flipping only the lowest set bit back to 1.
       ANDing with n keeps only that one bit.
```

---

## 6. The n & (n-1) Trick — A Deep Look

This single expression is one of the most powerful and frequently tested bit manipulation tricks.

```
n & (n-1) CLEARS THE LOWEST SET BIT.

WHY IT WORKS (binary arithmetic insight):

  Consider any number n with some lowest set bit at position k:
  n   = xxxx 1 000...0    (some bits above, 1 at position k, zeros below)
  n-1 = xxxx 0 111...1    (borrow from position k, flips k and everything below)

  n & (n-1):
        xxxx 1 000...0
      & xxxx 0 111...1
      = xxxx 0 000...0    ← bit k cleared, bits above unchanged ✅

APPLICATIONS:

1. COUNT SET BITS (Brian Kernighan's algorithm):
   def count_bits(n):
       count = 0
       while n:
           n &= (n - 1)   ← each iteration removes ONE set bit
           count += 1
       return count

   n=13=1101:
     1101 & 1100 = 1100 (count=1, removed bit 0)
     1100 & 1011 = 1000 (count=2, removed bit 2)
     1000 & 0111 = 0000 (count=3, removed bit 3)
   Result: 3 ✅ (13 has three 1-bits: 1+4+8=13)

   Time: O(number of set bits) — much faster than O(32) for sparse numbers

2. CHECK IF POWER OF 2:
   n > 0 and (n & (n-1)) == 0

   Powers of 2 have EXACTLY ONE set bit.
   Removing that one bit leaves 0.

   n=8=1000:  8 & 7 = 1000 & 0111 = 0000 = 0 → IS power of 2 ✅
   n=12=1100: 12 & 11 = 1100 & 1011 = 1000 ≠ 0 → NOT power of 2 ✅
   n=1:       1 & 0 = 0 → IS power of 2 ✅

3. FIND HIGHEST POWER OF 2 LESS THAN n:
   Repeatedly clear lowest set bit until one bit remains.
   Or use: bit_length approach with shifts.
```

---

## 7. XOR — The Most Versatile Operator

XOR deserves special attention because its unique properties unlock a family of elegant algorithms.

### XOR Properties in Practice

```
PROPERTY 1: a ^ a = 0  (self-cancellation)
  Any number XORed with itself = 0.
  Used to detect duplicates — duplicates cancel out.

PROPERTY 2: a ^ 0 = a  (identity)
  XOR with 0 leaves number unchanged.
  0 is the identity element for XOR.

PROPERTY 3: XOR is commutative and associative
  Order doesn't matter: a^b^c = c^b^a = b^a^c

COMBINED: a ^ b ^ a = b
  The two a's cancel, leaving b.
  This is the foundation of the "find the unique element" trick.
```

### Find the Single Non-Duplicate

```
PROBLEM: Array has every element appearing twice except one. Find it.

NAIVE: Sort + scan O(n log n), or hash map O(n) space.
BITWISE: XOR all elements. Pairs cancel to 0. Unique remains.

arr = [4, 1, 2, 1, 2]

4 ^ 1 ^ 2 ^ 1 ^ 2
= 4 ^ (1^1) ^ (2^2)   ← pairs cancel
= 4 ^ 0 ^ 0
= 4 ✅

def single_number(nums):
    result = 0
    for n in nums:
        result ^= n      ← XOR everything together
    return result

Time: O(n)   Space: O(1)   ← elegant!

EXTENSION: Two unique numbers among duplicates
  XOR all → result = a ^ b (where a,b are the two uniques)
  Find any set bit in result (that bit differs between a and b)
  Partition array by that bit → each partition has one unique
  XOR each partition separately → find both uniques
```

### XOR Swap

```
SWAP a and b WITHOUT temporary variable:

  a = 5  (0101)
  b = 3  (0011)

  a ^= b:  a = 0101 ^ 0011 = 0110  (a now holds a^b)
  b ^= a:  b = 0011 ^ 0110 = 0101  (b = b^(a^b) = a) ✅
  a ^= b:  a = 0110 ^ 0101 = 0011  (a = (a^b)^a = b) ✅

  a = 3, b = 5 ✅

WHY IT WORKS:
  Step 1: a = a^b           (a stores the XOR of both)
  Step 2: b = b^a = b^(a^b) = a^(b^b) = a^0 = a   (b gets original a)
  Step 3: a = a^b = (a^b)^a = b^(a^a) = b^0 = b   (a gets original b)

CAVEAT: If a and b are the SAME VARIABLE (same memory location):
  a ^= a → a = 0 (self-XOR clears to 0)
  b ^= a → b = b (XOR with 0)
  a ^= b → a = b (XOR with original b, not the intended swap)
  RESULT: Both become 0 ❌
  Always check a != b (or use different indices) before XOR swap.
```

---

## 8. Bit Counting Techniques

### Naive Count (O(32))

```python
def count_bits_naive(n):
    count = 0
    while n:
        count += n & 1    # check LSB
        n >>= 1           # shift right
    return count
```

### Brian Kernighan (O(set bits))

```python
def count_bits_kernighan(n):
    count = 0
    while n:
        n &= n - 1        # remove lowest set bit
        count += 1
    return count
```

### Lookup Table (O(1) with preprocessing)

```python
# Precompute bit counts for all 8-bit values (0-255)
lookup = [bin(i).count('1') for i in range(256)]

def count_bits_lookup(n):
    return (lookup[n & 0xFF] +          # bits 0-7
            lookup[(n >> 8) & 0xFF] +   # bits 8-15
            lookup[(n >> 16) & 0xFF] +  # bits 16-23
            lookup[(n >> 24) & 0xFF])   # bits 24-31
# O(1) with O(256) = O(1) extra space ✅
```

### Population Count (Hardware)

```
Modern CPUs have a dedicated POPCNT instruction.
In Python:  bin(n).count('1')
In Java:    Integer.bitCount(n)
In C++:     __builtin_popcount(n)

POPCNT executes in ONE CPU cycle — O(1) for any 32/64-bit number.
The most efficient possible, implemented in silicon.
```

### Count Bits for All Numbers 0 to n (DP)

```python
def count_bits_dp(n):
    dp = [0] * (n + 1)
    for i in range(1, n + 1):
        dp[i] = dp[i >> 1] + (i & 1)
        # dp[i] = dp[i//2] + (1 if i is odd else 0)
        # i >> 1 removes LSB; its count is dp[i>>1]
        # LSB itself contributes i & 1

    # Trace:
    # dp[0] = 0
    # dp[1] = dp[0] + 1 = 1    (1 = 1)
    # dp[2] = dp[1] + 0 = 1    (10 = 1)
    # dp[3] = dp[1] + 1 = 2    (11 = 2)
    # dp[4] = dp[2] + 0 = 1    (100 = 1)
    # dp[5] = dp[2] + 1 = 2    (101 = 2)
    # dp[6] = dp[3] + 0 = 2    (110 = 2)
    # dp[7] = dp[3] + 1 = 3    (111 = 3)

    return dp
# O(n) time, O(n) space ✅
```

---

## 9. Bitmask DP — Representing Subsets

One of the most powerful applications of bit manipulation is using an integer to represent a **subset of elements**, enabling DP over all 2ⁿ subsets.

```
IDEA: For a set of n elements {0, 1, 2, ..., n-1},
      represent any subset as an n-bit integer where
      bit k = 1 means "element k is in the subset."

EXAMPLE: Set {A, B, C, D} (n=4)

  mask = 0000: {}          (empty set)
  mask = 0001: {A}         (only bit 0)
  mask = 0011: {A, B}      (bits 0 and 1)
  mask = 0101: {A, C}      (bits 0 and 2)
  mask = 1111: {A,B,C,D}   (full set)
  Total masks: 2⁴ = 16    (all subsets)

SUBSET OPERATIONS AS BIT OPERATIONS:

  Add element k to subset:   mask | (1 << k)
  Remove element k:          mask & ~(1 << k)
  Check if k in subset:      mask & (1 << k)
  Union of two subsets:      mask1 | mask2
  Intersection:              mask1 & mask2
  Complement:                ((1 << n) - 1) ^ mask  ← flip all n bits
  Number of elements:        popcount(mask)
  Is subset of other:        (mask1 & mask2) == mask1

ITERATE ALL SUBSETS of a set:
  for mask in range(1 << n):    # 0 to 2^n - 1
      process(mask)

ITERATE SUBMASKS of a given mask:
  sub = mask
  while sub > 0:
      process(sub)
      sub = (sub - 1) & mask    # remove highest bit of sub that's in mask
      # This clever trick iterates ALL submasks of mask efficiently
```

### Traveling Salesman Problem with Bitmask DP

```
CLASSIC BITMASK DP: TSP for n cities.

State: dp[mask][i] = minimum cost to visit all cities in mask,
                     ending at city i.

mask represents which cities have been visited.

Transition:
  For each city j not in mask:
    dp[mask | (1<<j)][j] = min(dp[mask | (1<<j)][j],
                               dp[mask][i] + dist[i][j])

Base case: dp[1<<0][0] = 0  (start at city 0, only city 0 visited)

Answer: min over all i of (dp[(1<<n)-1][i] + dist[i][0])
        (visited all cities, return to start)

Without bitmask DP: O(n!) time (try all permutations)
With bitmask DP:    O(2^n × n²) time
For n=20: 20! ≈ 2.4×10¹⁸ vs 2²⁰ × 400 ≈ 4×10⁸ — 10 billion× faster ✅
```

---

## 10. Arithmetic with Bit Tricks

### Fast Multiply and Divide by Powers of 2

```
n * 2^k  =  n << k      (much faster than multiplication)
n / 2^k  =  n >> k      (for non-negative n)
n % 2^k  =  n & (2^k - 1)

EXAMPLES:
  n * 8  = n << 3     (8 = 2³, shift left 3)
  n / 16 = n >> 4     (16 = 2⁴, shift right 4)
  n % 8  = n & 7      (7 = 0b111, keep lower 3 bits)
  n % 16 = n & 15     (15 = 0b1111, keep lower 4 bits)

SPEED: Bit shifts execute in 1 CPU clock cycle.
       Multiplication: 3-5 cycles.
       Division: 20-80 cycles (hardware dependent).
       For powers of 2: shifts are 20-80× faster than division.
```

### Check Odd/Even Without Modulo

```
n is even: (n & 1) == 0    ← LSB = 0 means even
n is odd:  (n & 1) == 1    ← LSB = 1 means odd

n=42=00101010: 42 & 1 = 0 → EVEN ✅
n=7 =00000111: 7  & 1 = 1 → ODD  ✅

WHY: Even numbers have LSB=0 (divisible by 2).
     Odd numbers have LSB=1 (remainder 1 when divided by 2).
     This is directly encoded in the binary representation.
```

### Absolute Value Without Branch

```
BRANCHLESS ABSOLUTE VALUE:
  mask = n >> 31        # arithmetic right shift: 0 if positive, -1 if negative
  abs_n = (n + mask) ^ mask

  FOR POSITIVE n (mask = 0):
    (n + 0) ^ 0 = n ^ 0 = n  ✅

  FOR NEGATIVE n (mask = -1 = 1111...1111):
    (n + (-1)) ^ (-1) = (n-1) ^ (-1)
    n-1 flips the trailing bits, XOR with all-1s flips everything = -n ✅

  Example: n = -5 = 1111 1011
    mask = -5 >> 31 = -1 = 1111 1111
    n + mask = -5 + (-1) = -6 = 1111 1010
    (-6) ^ (-1) = 1111 1010 ^ 1111 1111 = 0000 0101 = 5 ✅

WHY BRANCHLESS?
  Modern CPUs use branch prediction.
  Mispredicted branches cost 10-20 cycles.
  For operations that alternate unpredictably between + and -:
  branchless version avoids misprediction penalty entirely.
```

---

## 11. The "Why" Questions

### Why use bit manipulation instead of arithmetic?

```
THREE MAIN REASONS:

1. SPEED: Bitwise operations execute in a SINGLE CPU CLOCK CYCLE.
   Comparison:
     Addition:       1 cycle
     Multiplication: 3-5 cycles
     Division:       20-80 cycles
     Bitwise AND:    1 cycle
     Bit shift:      1 cycle

   n % 8 vs n & 7:
     % uses division: ~20 cycles
     & uses AND:       1 cycle
     20× faster ✅

2. SPACE: Pack multiple booleans into one integer.
   32 boolean flags = 32 bytes normally.
   32 boolean flags = 1 integer = 4 bytes with bitmask.
   8× space savings. All 32 flags checked in ONE AND operation.

3. ELEGANCE: Some problems have natural bitwise solutions.
   "Find the unique element" XOR solution is O(n) time O(1) space.
   Hash map solution is O(n) time O(n) space.
   The bitwise solution is both faster AND uses less memory.
```

### Why does ~n = -(n+1)?

```
MATHEMATICAL DERIVATION:

In 32-bit two's complement:
  n + ~n = ?

  n     = any pattern
  ~n    = all bits flipped
  n + ~n = 1111 1111 1111 1111 = -1  (all 1s = -1 in two's complement)

  Therefore: ~n = -1 - n = -(n+1)

EXAMPLES:
  ~0  = -(0+1)  = -1   ✅  (0000...0 → 1111...1 = -1)
  ~1  = -(1+1)  = -2   ✅  (0000...1 → 1111...0 = -2)
  ~5  = -(5+1)  = -6   ✅
  ~(-1) = -(-1+1) = 0  ✅  (1111...1 → 0000...0 = 0)
  ~(-5) = -(-5+1) = 4  ✅

THIS MEANS:
  -(n+1) = ~n   (negate and subtract 1 by just flipping bits)
  -(n)   = ~n + 1  (negate by flipping bits and adding 1)
  These are used in two's complement hardware for fast negation.
```

### Why does (n & -n) isolate the lowest set bit?

```
-n in two's complement = ~n + 1

For n = 12 = 0000 1100:
  ~n    = 1111 0011
  ~n+1  = 1111 0100   ← this is -n

  n &(-n) = 0000 1100
          & 1111 0100
          = 0000 0100 = 4  ← only bit 2 set ✅

WHY:
  ~n flips all bits. +1 to ~n propagates carry through trailing 0s
  of ~n (which were 1s in n), flipping them back to 0 and setting
  the position of the lowest set bit of n to 1.

  The pattern:
  n    = xxxx 1 000  (lowest set bit at position k, zeros below)
  ~n   = xxxx 0 111  (flip everything)
  ~n+1 = xxxx 1 000  (carry propagates through the 111 section, stops at 0)

  n & (~n+1) = xxxx 1 000 & xxxx 1 000 = 0000 1 000  (only shared pattern) ✅
```

---

## 12. "What If" Edge Cases

| What If...? | What Happens |
|---|---|
| XOR swap when a and b are same variable | Both become 0; must check they're different variables/indices |
| Left shift by 32 on a 32-bit int | Undefined behavior in C/C++; Python auto-extends; Java wraps modulo 32 |
| Right shift negative number with `>>` | Arithmetic shift fills with 1s (sign preserved); use `>>>` for logical shift |
| n & (n-1) when n = 0 | n-1 = -1 = all 1s; 0 & -1 = 0; returns 0 correctly (0 has no set bits) |
| Counting bits of negative number | Depends on language; Python integers are arbitrary precision; C/Java count all 32/64 bits |
| (1 << 31) in signed 32-bit int | Sets sign bit → -2147483648 (overflow); use `1L << 31` for long |
| XOR of empty set of numbers | Result is 0 (identity element); correctly handles empty input |
| Bitmask for more than 64 elements | Exceeds hardware integer size; need BigInteger or bitset data structure |
| n % k where k is not a power of 2 | Cannot use AND trick; must use regular modulo |
| ~0 | All bits set = -1 in two's complement; common mask for "all bits enabled" |

### The 32 vs 64 Bit Problem

```
PYTHON: Integers have ARBITRARY PRECISION — no overflow, ever.
  1 << 100 = 1267650600228229401496703205376   (works fine)
  ~5 = -6   (correct two's complement behavior)
  Be careful: Python's >> is always arithmetic (no logical >>>)

JAVA:
  int:  32 bits, arithmetic >>; use >>> for logical
  long: 64 bits, use L suffix: 1L << 40 (not 1 << 40)
  Integer.MAX_VALUE = 2^31 - 1 = 2147483647
  Integer.MIN_VALUE = -2^31   = -2147483648

C/C++:
  Undefined behavior for shifting by >= bit width
  Unsigned right shift is always logical
  Signed right shift is implementation-defined (usually arithmetic)

SAFE PRACTICE:
  Always verify integer width for the language you're using.
  Use explicit type casts for large shifts.
  In interviews: clarify "32-bit int" assumption.
```

---

## 13. Classic Problems

### Reverse Bits

```
PROBLEM: Reverse the bit order of a 32-bit unsigned integer.
  Input:  43261596 = 00000010100101000001111010011100
  Output:           00111001011110000010100101000000 = 964176192

def reverse_bits(n):
    result = 0
    for _ in range(32):
        result = (result << 1) | (n & 1)   # take LSB of n, append to result
        n >>= 1                             # shift n right
    return result

TRACE (simplified to 8 bits, n=00101010=42):
  Step 1: result=0<<1 | 0 = 0, n=00010101
  Step 2: result=0<<1 | 1 = 1, n=00001010
  Step 3: result=1<<1 | 0 = 2=10, n=00000101
  Step 4: result=2<<1 | 1 = 5=101, n=00000010
  ...continues...
  Final: 01010100 = 84   (reversed bits of 42) ✅
```

### Missing Number

```
PROBLEM: Find the missing number in array [0, 1, ..., n] with one number missing.

XOR APPROACH:
  XOR all indices 0..n with all elements.
  Present numbers cancel themselves out.
  Missing number has no pair → remains.

def missing_number(nums):
    n = len(nums)
    xor = 0
    for i in range(n + 1):
        xor ^= i                 # XOR all expected numbers 0..n
    for num in nums:
        xor ^= num               # XOR all actual numbers
    return xor                   # only missing number remains

nums = [3, 0, 1]:  n=3, expected {0,1,2,3}

  xor = 0^1^2^3 = 0
  xor = xor ^ 3 ^ 0 ^ 1 = 0^1^2^3^3^0^1 = 2 ✅

ARITHMETIC APPROACH (also O(1) space):
  expected_sum = n*(n+1)/2
  return expected_sum - sum(nums)
  XOR approach handles large n without overflow risk.
```

### Power of Two, Four, and Other Special Values

```
POWER OF 2:
  n > 0 and (n & (n-1)) == 0
  Exactly one bit set.

POWER OF 4:
  Power of 2 AND that single bit is at an even position (0, 2, 4, ...):
  n > 0 and (n & (n-1)) == 0 and (n & 0xAAAAAAAA) == 0
  0xAAAAAAAA = 1010...1010 (bits at ODD positions)
  If AND with this mask = 0, the set bit is at an EVEN position ✅

  n=4=100:  4 & 3=0 ✅, 4 & 0xAAAAAAAA=0 ✅ → power of 4 ✅
  n=8=1000: 8 & 7=0 ✅, 8 & 0xAAAAAAAA=8 ✗ → NOT power of 4 ✅ (8=2³)

POWER OF 3, 5, etc.:  No bitwise trick — use modulo arithmetic.
  Powers of 2 are special because binary naturally represents them.
```

### Two Non-Duplicate Numbers

```
PROBLEM: Array with every element twice except TWO unique numbers. Find both.

STEP 1: XOR everything → result = a ^ b (a,b are the two uniques)
  They differ in at least one bit (otherwise they'd be equal).

STEP 2: Find any bit that differs (use lowest set bit of a^b):
  diff_bit = (a^b) & -(a^b)    ← isolate lowest set bit

STEP 3: Partition array: group1 has this bit set, group2 doesn't.
  XOR within each group → one unique number per group.

def find_two_unique(nums):
    xor = 0
    for n in nums: xor ^= n           # xor = a ^ b

    diff_bit = xor & (-xor)            # lowest bit where a and b differ

    a = b = 0
    for n in nums:
        if n & diff_bit:               # partition
            a ^= n
        else:
            b ^= n
    return [a, b]

nums = [1, 2, 1, 3, 2, 5]
  XOR all: 1^2^1^3^2^5 = 3^5 = 011^101 = 110 = 6
  diff_bit = 6 & (-6) = 6 & (1111...1010) = 0000...0010 = 2 (bit 1)
  Group bit1 set:   {2, 3, 2} → XOR = 3
  Group bit1 clear: {1, 1, 5} → XOR = 5
  Answer: [3, 5] ✅
```

---

## 14. Real-World Applications

| Domain | Bit Technique | How It's Used |
|---|---|---|
| **Network programming** | Bitmasks for IP | Subnet masks: `ip & subnet_mask` extracts network address |
| **Operating systems** | Permission flags | `rwxr-xr-x` = 101 101 101 in binary; chmod uses octal |
| **Graphics** | Color channels | RGBA = 4 bytes packed: `(r<<24)\|(g<<16)\|(b<<8)\|a` |
| **Compression** | Huffman encoding | Bit-level packing of variable-length codes |
| **Cryptography** | XOR cipher, AES | XOR for mixing; shifts for diffusion; AND/OR for S-boxes |
| **Databases** | Bloom filters | Bitmask of hash values for probabilistic set membership |
| **Embedded systems** | Hardware registers | Set/clear specific control bits in hardware registers |
| **Chess engines** | Bitboards | 64-bit integer represents piece positions; moves via shifts |
| **Set operations** | BitSet/BitArray | O(1) union/intersection for sets of bounded integers |
| **Error detection** | CRC, parity | XOR-based checksum for detecting transmission errors |

### Unix File Permissions — Bitmasks in Daily Use

```
UNIX PERMISSION BITS (9 bits):
  rwx rwx rwx
  ↑   ↑   ↑
  owner group others

  r (read)    = bit 2 = 4
  w (write)   = bit 1 = 2
  x (execute) = bit 0 = 1

PERMISSION: rwxr-xr-x = 755

  Owner:  rwx = 1+2+4 = 7
  Group:  r-x = 1+0+4 = 5
  Others: r-x = 1+0+4 = 5

  Combined: 0o755 = 111 101 101 in binary

CHECK if owner has write permission:
  mode = 0o755 = 0b111101101
  owner_write_mask = 0b010000000 = 0o200
  mode & owner_write_mask = 0b010000000 ≠ 0 → has write ✅

ADD execute for others:
  mode | 0o001 = 0o755 | 0o001 = 0o755 (already set)

REMOVE write from group:
  mode & ~0o020 = 0o755 & ~0o020

Every time you type chmod 755 in a terminal,
you're working with a 9-bit bitmask. ✅
```

### Chess Bitboards — Bit Manipulation for Game AI

```
A chess board has 64 squares.
A 64-bit integer perfectly represents which squares are occupied.

PIECE POSITIONS:
  white_pawns   = 0x000000000000FF00  (rank 2, bits 8-15)
  black_pawns   = 0x00FF000000000000  (rank 7, bits 48-55)
  white_rooks   = 0x0000000000000081  (corners a1 and h1)

MOVE GENERATION:
  white_pawn_moves = (white_pawns << 8) & ~all_pieces  ← shift up one rank
  white_pawn_attacks = ((white_pawns << 7) | (white_pawns << 9)) & black_pieces

  ONE BIT OPERATION generates ALL pawn moves simultaneously.
  Without bitboards: loop over 8 pawns, check each square → 8× slower.

ATTACKED SQUARES:
  knight_attacks = (knight << 17) | (knight << 15) | (knight << 10) | ...
  All 8 possible knight destinations in one expression.

PERFORMANCE:
  Stockfish, the world's strongest chess engine, uses bitboards extensively.
  Entire board state fits in 12 64-bit integers (6 piece types × 2 colors).
  Move generation: 100+ million positions per second on modern hardware.
  Bit manipulation makes this possible.
```

---

## 15. Comparison With Related Techniques

```
              ┌──────────────────────────────────────────────────────────┐
              │           DATA MANIPULATION TECHNIQUES                    │
              └──────────────────────────┬───────────────────────────────┘
                                         │
       ┌──────────────────┬──────────────┼──────────────┬────────────────┐
       ▼                  ▼             ▼              ▼                ▼
  BIT MANIP.          ARITHMETIC      BOOLEAN         SET OPS         HASH MAP
  ──────────          ──────────      ───────         ───────         ────────
  O(1) per op         O(1) per op     O(1) per op     O(1)–O(n)       O(1) avg
  Integer only        Any type        Boolean only    Any hashable    Any hashable
  Fixed precision     Overflow risk   No overflow     Unbounded size  Unbounded
  In-register         In-register     In-register     Heap-allocated  Heap-allocated
  No memory           No memory       No memory       O(n) memory     O(n) memory
  Tricky to read      Readable        Readable        Readable        Readable
  Hardware direct     Hardware direct CPU native      Software        Software
```

**Bit manipulation vs boolean arrays:**
A boolean array of n elements uses n bytes. A bitmask of n elements uses n/8 bytes. For n=64 elements: array=64 bytes, bitmask=8 bytes. All set operations (union, intersection, membership) that are O(n) on arrays become O(1) on bitmasks (single AND/OR instruction). The tradeoff: readability.

**Bit manipulation vs hash sets:**
Hash set: O(1) average membership, any type, unlimited size, O(n) memory. Bitmask: O(1) guaranteed membership, integers in bounded range only, limited to 64 elements (hardware int), O(1) memory. For the specific case of small integer sets — bitmask wins on both speed and memory.

---

## 16. Tips for Long-Term Retention

**1. The light switch panel image**
An integer is a row of 8 (or 32 or 64) light switches. AND = "need both on." OR = "either turns it on." XOR = "exactly one on." NOT = "flip everything." Shift = "slide the whole pattern." This physical image makes every operation intuitive and never requires memorizing abstract rules.

**2. The six operators and their one-word purpose**
AND = filter (keep bits matching mask). OR = set (force bits to 1). XOR = toggle (flip specific bits). NOT = invert (flip everything). Left shift = multiply by 2. Right shift = divide by 2. One word each, permanently locked to each operator.

**3. n & (n-1) clears the lowest bit — derive it**
Don't memorize this — derive it when needed. n has some lowest set bit at position k with zeros below. n-1 borrows from position k, flipping k to 0 and all below to 1. ANDing cancels them. After deriving it once, it feels obvious forever.

**4. XOR's three identities are the whole algorithm**
`a^a=0`, `a^0=a`, and self-inverse `(a^b)^b=a`. These three properties generate every XOR algorithm: find unique (pairs cancel), XOR swap, and the two-uniques problem. Internalize these three identities once and you can reconstruct any XOR algorithm from scratch.

**5. Bit manipulation = representing the impossible in O(1) space**
The conceptual leap: an integer is not just a number, it's a container for 32 or 64 boolean values that you can operate on ALL AT ONCE with a single instruction. "Does this subset contain elements i, j, k?" is one AND operation. "What's the union of these two subsets?" is one OR operation. This parallel nature is what makes bit manipulation so powerful.

**6. The bitmask DP pattern — subsets as integers**
When you see "find optimal solution over all subsets of n elements," reach for bitmask DP. Integer `mask` represents a subset. `mask | (1<<k)` adds element k. `mask & ~(1<<k)` removes it. Iterate all subsets with `for mask in range(1<<n)`. This pattern transforms O(n!) brute force into O(2^n × poly(n)) — feasible for n ≤ 20.

**7. Powers of 2 are the bridge**
`n << k = n × 2^k` and `n >> k = n // 2^k` and `n & (2^k - 1) = n % 2^k`. These three conversions bridge between arithmetic and bitwise operations. Whenever you see multiplication, division, or modulo by a power of 2 in performance-critical code — replace with the bitwise equivalent.

---

Bit manipulation is fundamentally about **seeing integers as data structures rather than just quantities**. A 64-bit integer is not just a number up to 2^64 — it is a set, a permission system, a board state, a collection of flags, a hash function intermediate, a compressed boolean array. The bitwise operators are not arithmetic shortcuts — they are set operations (AND = intersection, OR = union, XOR = symmetric difference) that execute in a single hardware instruction on all 64 elements simultaneously. This parallelism — 64 independent boolean operations in one CPU cycle — is the source of bit manipulation's power. Master the six operators, internalize the key tricks (n&(n-1), n&(-n), XOR properties), and you gain access to a level of the machine that makes otherwise O(n) operations O(1) and otherwise impossible memory constraints suddenly trivial.
