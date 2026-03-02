# Hash Map / Set Lookup: A Deep Dive

---

## 1. What Is It? (Definition & Core Components)

A **hash map** (also called a hash table or dictionary) is a data structure that stores **key-value pairs** and provides average O(1) insertion, deletion, and lookup by transforming keys into array indices through a mathematical function called a **hash function**. A **hash set** is the same structure storing only keys with no associated values — answering "does this element exist?" in O(1).

```
HASH MAP:                         HASH SET:

  "alice" → 95                      {"cat", "dog", "bird"}
  "bob"   → 87                      Answers: "is X in the set?"
  "carol" → 92                      in O(1)
  Answers: "what is alice's score?"
  in O(1)
```

**Core components:**

- **Key** — the identifier used to store and retrieve data (string, integer, object)
- **Value** — the data associated with a key (hash map only; absent in hash set)
- **Hash function** — the deterministic mathematical function that converts a key into an integer index
- **Bucket array** — the underlying fixed-size array where entries are stored; indexed by hash output
- **Hash code** — the raw integer output of the hash function before being mapped to array size
- **Index** — `hash(key) % array_size`; the actual slot in the bucket array
- **Collision** — when two different keys produce the same index; must be resolved
- **Collision resolution** — the strategy for handling collisions (chaining or open addressing)
- **Load factor** — the ratio of stored entries to array capacity; triggers resizing when too high
- **Resizing / rehashing** — growing the bucket array and reinserting all entries when load factor is exceeded

The central promise: **turn any key into a direct array index, making lookup as fast as `arr[i]`** — O(1) — regardless of how many elements are stored.

---

## 2. The Physical Analogy: A Post Office with Numbered Mailboxes

Imagine a post office with 100 numbered mailboxes:

```
POST OFFICE:

  Mailboxes: [0][1][2][3]...[99]

  HASH FUNCTION = "rule for assigning mailboxes"
    Rule: take the addressee's name, convert to a number,
          take that number mod 100 → that's their mailbox.

  "Alice"  → name-to-number → 65 → mailbox 65
  "Bob"    → name-to-number → 12 → mailbox 12
  "Carol"  → name-to-number → 65 → mailbox 65 ← COLLISION!

  To retrieve Alice's mail:
    Apply hash function to "Alice" → 65
    Check mailbox 65 → Alice's mail ✅
    One step, regardless of how many people use this post office.
```

This analogy captures the core ideas:
- The **hash function** is the assignment rule — deterministic, fast, same input always gives same mailbox
- **Direct access** — you go straight to the right mailbox, no searching
- **Collisions** — when two people are assigned the same mailbox, you need a strategy
- **The tradeoff** — more mailboxes (larger array) = fewer collisions, but more wasted space

---

## 3. The Hash Function — The Engine of Everything

The hash function is the most critical component. Its quality determines correctness (same key always returns same result), performance (distribution of keys across buckets), and collision rate.

### What Makes a Good Hash Function?

```
PROPERTIES OF A GOOD HASH FUNCTION:

1. DETERMINISTIC: hash(key) always returns same value for same key.
   "alice" → 65 today, 65 tomorrow, 65 forever.

2. UNIFORM DISTRIBUTION: outputs spread evenly across [0, array_size).
   Poor distribution → many collisions → O(n) degradation.
   Good distribution → few collisions → O(1) performance.

3. FAST TO COMPUTE: O(key_length) at most, ideally O(1).
   The whole point is fast access — hash function can't be slow.

4. AVALANCHE EFFECT: small input changes → drastically different output.
   "alice" → 65
   "alic"  → 23   (not 64 — big change from small change)
   Prevents clustering of similar keys.
```

### Hash Function for Strings

```
NAIVE (bad): Sum of character values
  hash("ab") = 97 + 98 = 195
  hash("ba") = 98 + 97 = 195   ← SAME! Doesn't distinguish order.
  hash("abc") = 97+98+99 = 294
  hash("bac") = 98+97+99 = 294 ← anagrams always collide!

POLYNOMIAL ROLLING HASH (good):
  hash(s) = s[0]×p^(n-1) + s[1]×p^(n-2) + ... + s[n-1]×p^0  mod M
  where p = prime (e.g., 31 or 37), M = large prime

  hash("abc") = 97×31² + 98×31 + 99
              = 97×961 + 98×31 + 99
              = 93217 + 3038 + 99
              = 96354 mod M

  hash("bac") = 98×961 + 97×31 + 99
              = 94178 + 3007 + 99
              = 97284 mod M   ← DIFFERENT ✅

WHY POLYNOMIAL?
  Each character's position is encoded by the power of p.
  "a" at position 0 contributes p^0 = 1 × 'a'.
  "a" at position 1 contributes p^1 = 31 × 'a'.
  Same characters in different positions give different values.
```

### Hash Function for Integers

```
SIMPLE: hash(k) = k % array_size
  Effective for uniformly distributed keys.
  Problem: if array_size = 100 and keys are multiples of 10,
           only 10 buckets used → extreme clustering.

MULTIPLICATION METHOD:
  hash(k) = floor(array_size × (k × A mod 1))
  where A ≈ 0.618... (golden ratio conjugate)
  Better distribution for sequential keys.

PYTHON IMPLEMENTATION:
  hash(int) uses the integer itself (mod table size internally)
  hash(str) uses SipHash (cryptographic quality, changes per process)
  hash(tuple) combines element hashes via formula
```

---

## 4. Collision Resolution — The Two Strategies

No hash function eliminates collisions entirely. Every hash table needs a collision resolution strategy.

### Strategy 1: Separate Chaining

```
Each bucket holds a LINKED LIST of all entries that hashed to that index.

ARRAY:
  [0]: → null
  [1]: → ("alice",95) → null
  [2]: → ("bob",87) → ("carol",92) → null   ← collision at index 2
  [3]: → null
  [4]: → ("dave",78) → null
  ...

INSERT "carol" (hashes to 2):
  Slot 2 already has "bob".
  APPEND "carol" to linked list at slot 2. ✅

LOOKUP "carol":
  Hash "carol" → 2
  Traverse list at slot 2: check "bob" (no), check "carol" (yes) ✅

WORST CASE: All keys hash to same slot → O(n) lookup (degenerate linked list)
AVERAGE CASE: O(1 + load_factor) lookup

ADVANTAGES:
  Simple to implement
  Handles high load factors gracefully
  No clustering between buckets

DISADVANTAGES:
  Extra memory for list pointers
  Poor cache performance (linked lists scatter in memory)
  Memory allocation per insertion (slow in practice)
```

```
VISUAL WITH HASH TABLE SIZE 5, storing {(0,A),(5,B),(3,C),(8,D),(10,E)}:

  keys 0,5,10 all hash to 0 (% 5)
  key 3 hashes to 3
  key 8 hashes to 3

  Bucket 0: [0→A] → [5→B] → [10→E]
  Bucket 1: empty
  Bucket 2: empty
  Bucket 3: [3→C] → [8→D]
  Bucket 4: empty

  Lookup key=5: hash(5)=0, traverse list → skip 0 → find 5 → return B ✅
```

### Strategy 2: Open Addressing

```
ALL entries stored IN the array itself. On collision, probe for next empty slot.

LINEAR PROBING: try index, index+1, index+2, ...

INSERT "carol" (hashes to 2, slot 2 is taken):
  Try slot 2: occupied by "bob" → move on
  Try slot 3: empty → INSERT HERE ✅

Array: [_, "alice", "bob", "carol", _, ...]
index:  0     1        2       3

LOOKUP "carol":
  Hash "carol" → 2
  Slot 2: "bob" ≠ "carol" → probe slot 3
  Slot 3: "carol" ✅

DELETION PROBLEM:
  If you DELETE "bob" (slot 2), later lookup of "carol":
    Hash "carol" → 2
    Slot 2: EMPTY → assume not found → WRONG ❌

  FIX: Use TOMBSTONE markers instead of truly emptying deleted slots.
  Tombstone: "this slot was deleted but keep probing through it"
```

```
PROBING STRATEGIES:

LINEAR PROBING:
  probe[i] = (hash(key) + i) % size
  Simple, but CLUSTERS (primary clustering):
    Filled slots bunch together, making future insertions probe longer.

  [_][_][A][B][C][D][_][_]   ← cluster of 4, next insert in this area probes 4 slots
         ↑ hash lands here, must probe to D+1

QUADRATIC PROBING:
  probe[i] = (hash(key) + i²) % size
  Reduces primary clustering, but can cause secondary clustering.
  Not guaranteed to find empty slot unless size is prime and load < 0.5.

DOUBLE HASHING:
  probe[i] = (hash1(key) + i × hash2(key)) % size
  Different keys have different probe sequences → minimal clustering.
  Best collision avoidance but requires computing two hash functions.
```

---

## 5. Load Factor and Resizing

```
LOAD FACTOR α = (number of entries) / (array size)

  10 entries in array of size 20: α = 0.5
  19 entries in array of size 20: α = 0.95  ← very high, many collisions

EFFECT OF LOAD FACTOR ON PERFORMANCE:

Chaining:    Expected lookups ≈ 1 + α/2  (for successful search)
Open addr.:  Expected probes ≈ 1/(1-α)   (approaches ∞ as α→1)

  α=0.5:  chaining≈1.25  open≈2.0  probes — fast
  α=0.7:  chaining≈1.35  open≈3.3  probes — still ok
  α=0.9:  chaining≈1.45  open≈10   probes — getting slow
  α=0.99: chaining≈1.50  open≈100  probes — terrible

TYPICAL THRESHOLDS:
  Java HashMap: resize when α > 0.75
  Python dict:  resize when α > 0.67 (2/3)
  C++ unordered_map: depends on implementation, default max_load=1.0

RESIZING PROCESS (rehashing):
  1. Allocate new array of size ≈ 2× current
  2. For every key-value pair in old array:
     a. Recompute hash with new array size: hash(key) % new_size
     b. Insert into new array
  3. Replace old array with new array

  COST: O(n) for one resize operation.
  AMORTIZED: O(1) per insertion because resizes double the capacity,
             so n insertions trigger O(log n) resizes, each O(n/2^k):
             total resize cost = O(n/2 + n/4 + n/8 + ...) = O(n)
             amortized per insertion: O(n)/n = O(1) ✅
```

```
RESIZE EXAMPLE:
  array_size=4, entries: {(a,1),(b,2),(c,3),(d,4)} → α=1.0 → resize!

  OLD (size 4):           NEW (size 8):
  [0]: (a,1)              [0]: (a,1)   ← hash(a)%8 might differ from hash(a)%4!
  [1]: (b,2)              [1]: (b,2)
  [2]: (c,3)              [3]: (c,3)
  [3]: (d,4)              [4]: (d,4)
                          [2],[5],[6],[7]: empty

  CRITICAL: Must RECOMPUTE all indices. Old indices are invalid.
  hash(key) % 4 ≠ hash(key) % 8 in general.
```

---

## 6. Core Operations — Full Mechanics

### INSERT(key, value)

```
def insert(key, value):
    index = hash(key) % array_size

    if CHAINING:
        traverse list at array[index]
        if key found: UPDATE value (handle duplicate key)
        else: APPEND (key, value) to list

    if OPEN ADDRESSING:
        probe sequence starting at index
        find first empty or tombstone slot
        INSERT (key, value) there

    entries_count++
    if load_factor > threshold: RESIZE

Time: O(1) average, O(n) worst case (all collisions)
```

### LOOKUP(key)

```
def lookup(key):
    index = hash(key) % array_size

    if CHAINING:
        traverse list at array[index]
        return value where entry.key == key
        return None if not found

    if OPEN ADDRESSING:
        probe sequence starting at index
        if slot matches key: return value
        if slot is empty (not tombstone): return None (key not present)
        if slot is tombstone: continue probing
        return None if full probe sequence finds nothing

Time: O(1) average, O(n) worst case
```

### DELETE(key)

```
def delete(key):
    if CHAINING:
        traverse list at array[index]
        remove the node with matching key

    if OPEN ADDRESSING:
        find the slot via probing
        replace entry with TOMBSTONE (not empty!)
        entries_count--

    WHY TOMBSTONE AND NOT EMPTY?
    Suppose we inserted A and B, both hashing to slot 3.
    A goes to slot 3. B probes to slot 4.
    If we DELETE A and truly empty slot 3:
      Lookup B: hash→3, slot 3 is EMPTY → "B not found" ❌
    If we use TOMBSTONE at slot 3:
      Lookup B: hash→3, slot 3 is tombstone → keep probing → slot 4 → B ✅

Time: O(1) average
```

---

## 7. Hash Collisions in Detail — The Numbers

```
BIRTHDAY PARADOX APPLICATION:
  How many insertions before the first collision in a table of size n?

  Expected first collision ≈ √(π × n / 2)

  n = 365 days: first collision ≈ √(π×365/2) ≈ 23.9 people (birthday problem!)
  n = 1000 slots: first collision ≈ √(π×500) ≈ 39.6 insertions
  n = 1,000,000 slots: first collision ≈ √(π×500,000) ≈ 1253 insertions

LESSON: Collisions happen much sooner than intuition suggests.
  A table of 1 million slots experiences its first collision
  after only ~1253 insertions (0.1% full).
  This is why a good hash function and collision resolution are BOTH necessary.
```

---

## 8. Python, Java, and Internals

### Python's dict

```python
# Python dict: hash table with open addressing + compact layout

d = {}                  # empty dict, initial size 8
d["alice"] = 95         # hash("alice") → some index
d["bob"] = 87

# Internal state (simplified):
# hash table size starts at 8, grows by 4× until 50k, then 2×
# Lookup:  hash(key) → index → compare key → return value
# Keys must be HASHABLE (immutable: int, str, tuple, frozenset)
# Lists, dicts are NOT hashable (mutable → hash would change)

# Why does Python's dict maintain INSERTION ORDER (Python 3.7+)?
# Compact dictionary design: separate indices array + entries array
# Entries added in order; indices array points to entry positions
# Iteration follows entries array order → insertion order preserved
```

### Java's HashMap

```java
// Java HashMap: chaining with linked lists (turns to trees at length 8)

HashMap<String, Integer> map = new HashMap<>();
map.put("alice", 95);     // hash("alice") → index → insert
map.get("alice");         // hash("alice") → index → lookup

// Default load factor: 0.75
// Default initial capacity: 16
// When size > 0.75 × capacity: resize to 2× capacity

// Java 8+: when a chain length exceeds 8, converts to RED-BLACK TREE
// Chain: O(n) worst case per bucket
// Tree:  O(log n) worst case per bucket
// This prevents O(n) hash flooding attacks
```

---

## 9. The "Why" Questions

### Why is lookup O(1) instead of O(log n) or O(n)?

```
ARRAY LOOKUP arr[i]:  O(1)
  Because: memory address = base_address + i × element_size
  Direct computation → direct memory access → one operation.

HASH MAP LOOKUP hash_map[key]:  O(1) AVERAGE
  Step 1: compute hash(key) → O(key_length) ≈ O(1) for fixed-length keys
  Step 2: compute index = hash % size → O(1)
  Step 3: access array[index] → O(1) (same as array access)
  Step 4: compare key → O(1) if no collision, O(chain_length) if collision

  AVERAGE CASE: chain_length ≈ load_factor ≈ constant
                → O(1) average

  WORST CASE: all keys in one bucket → O(n)
              happens with pathological input or terrible hash function

  CONTRAST:
    Binary search tree: O(log n) because each comparison halves the space
    Hash map: O(1) because hash function DIRECTLY computes the location
              No searching needed — go straight to the answer.
```

### Why doesn't the hash function need to be unique (injective)?

```
INJECTIVE (one-to-one) hash: different keys → always different indices
  Would eliminate all collisions.
  IMPOSSIBLE in general: infinitely many possible keys, finite array.
  (Can't map ∞ keys to n slots without collisions.)

  Even for finite key sets:
    If keys can be 64-bit integers (2^64 possible values)
    and array has 2^20 slots:
    By pigeonhole: some slot must hold 2^44 keys → can't be injective.

SO: Collisions are MATHEMATICALLY INEVITABLE.
    Good hash functions minimize collision PROBABILITY.
    Collision RESOLUTION handles the ones that occur.
    Together: amortized O(1) despite inevitable collisions.
```

### Why must keys be immutable (hashable)?

```
CONSEQUENCE OF MUTABILITY:

  Suppose you could use a list as a key:
    my_list = [1, 2, 3]
    hash_map[my_list] = "value"    ← stores at index hash([1,2,3]) = 42

  Now modify the list:
    my_list.append(4)              ← my_list is now [1,2,3,4]
    hash_map[my_list]              ← computes hash([1,2,3,4]) = 87
                                      looks at slot 87 → NOT FOUND ❌

  The entry is now UNREACHABLE — lost in the table at slot 42,
  but all lookups go to slot 87.

RULE: The hash of a key must NEVER CHANGE after insertion.
  Immutability guarantees this.
  Python: ints, strings, tuples = hashable ✅
          lists, dicts, sets = not hashable ❌

WORKAROUND: Use frozenset instead of set, tuple instead of list.
```

---

## 10. "What If" Edge Cases

| What If...? | What Happens |
|---|---|
| Two keys have the same hash code | Collision — resolved by chaining or probing; correctness maintained |
| Hash function returns negative integer | Take `abs()` or use `hash & 0x7FFFFFFF` before `% size` to ensure positive index |
| Load factor reaches 1.0 (open addressing) | Table is full; insertion fails or infinite loop; must resize before this |
| Deleting from open-addressed table without tombstones | Future lookups incorrectly return "not found" for keys that probe through deleted slot |
| Very large key (e.g., 10MB string) | Hash function must process entire key: O(key_length); not O(1) for huge keys |
| Integer keys with poor hash (e.g., `k % size` with clustered inputs) | Bad distribution; many collisions; O(n) performance |
| Hash flooding attack (adversarial keys chosen to collide) | All keys in one bucket → O(n) lookup; mitigated by randomized hash seeds (Python's SipHash) |
| Custom object as key without custom hash | Uses object identity (memory address) as hash; two equal objects may have different hashes |
| Resize during iteration | Undefined behavior in most implementations; don't modify while iterating |
| Negative load factor threshold | Invalid; typically handled by constructor validation |

### Hash Flooding Attack

```
ATTACK: Adversary knows your hash function.
  They craft n inputs that ALL hash to index 0.
  Every lookup: O(n) traversal of the collision chain.
  Result: O(n) per request → denial of service.

DEFENSES:
  1. RANDOMIZED HASH SEEDS (Python's approach):
     hash_seed = random() at startup
     hash(key) = deterministic_hash(key, seed)
     Attacker can't predict which keys will collide (seed unknown).

  2. TREE-BASED CHAINS (Java 8+):
     When chain length > 8, convert to red-black tree.
     Worst case per-bucket: O(log n) instead of O(n).
     Attack still degrades performance but can't achieve O(n) per lookup.

  3. CUCKOO HASHING:
     Worst-case O(1) lookup.
     Uses two hash functions; adversary must break both simultaneously.
```

---

## 11. Hash Set vs Hash Map

```
HASH SET:                              HASH MAP:
  Stores: keys only                     Stores: key-value pairs
  Query: "is X present?"                Query: "what is the value for key X?"
  Operations: add, remove, contains     Operations: put, remove, get
  Space: O(n) for n elements            Space: O(n) for n pairs

  Implemented as:                       Standard implementation:
    hash map where value = placeholder    full key-value storage

WHEN TO USE HASH SET:
  Deduplication (remove duplicates)
  Membership testing ("have I seen this before?")
  Set operations (intersection, union, difference)

WHEN TO USE HASH MAP:
  Key-to-value mapping
  Counting occurrences (key = element, value = count)
  Caching / memoization (key = input, value = result)
  Grouping (key = group, value = list of members)

SET OPERATIONS USING HASH SETS:

  INTERSECTION (elements in both A and B):
    For each element in A: if element in B → add to result
    O(|A|) average

  UNION (elements in A or B):
    Add all of A to result, then add all of B
    O(|A| + |B|)

  DIFFERENCE (elements in A but not B):
    For each element in A: if element not in B → add to result
    O(|A|)
```

---

## 12. Classic Patterns Using Hash Map/Set

### Pattern 1: Two Sum

```
PROBLEM: Find two indices i, j where arr[i] + arr[j] = target.

NAIVE: O(n²) — check every pair.

HASH MAP: O(n)

For each element x at index i:
  complement = target - x
  IF complement in seen:
      return [seen[complement], i]   ← found the pair
  seen[x] = i                        ← store x's index for future pairs

TRACE: arr=[2,7,11,15], target=9

  x=2:  complement=7, 7 not in seen. seen={2:0}
  x=7:  complement=2, 2 IS in seen! return [0,1] ✅

WHY IT WORKS:
  For every element x, we check if its "partner" (target-x) was seen before.
  The hash map stores past elements with O(1) lookup.
  Single pass → O(n).
```

### Pattern 2: Frequency Counting

```
PROBLEM: Find the most frequent element, or count occurrences.

count = {}
for x in arr:
    count[x] = count.get(x, 0) + 1

APPLICATIONS:
  "First non-repeating character"  → count chars, find first with count=1
  "Top k frequent elements"        → count, then heap of size k
  "Anagram detection"              → compare frequency maps
  "Group anagrams"                 → sort word as key, group by key

ANAGRAM GROUPING:
  ["eat","tea","tan","ate","nat","bat"]

  "eat" → sorted="aet" → group["aet"].append("eat")
  "tea" → sorted="aet" → group["aet"].append("tea")
  "tan" → sorted="ant" → group["ant"].append("tan")
  "ate" → sorted="aet" → group["aet"].append("ate")
  "nat" → sorted="ant" → group["ant"].append("nat")
  "bat" → sorted="abt" → group["abt"].append("bat")

  Result: [["eat","tea","ate"],["tan","nat"],["bat"]] ✅
```

### Pattern 3: Sliding Window + Hash Map

```
PROBLEM: Longest substring without repeating characters.

Use hash map: {char → last_seen_index}
Maintain left pointer; move it past the last seen position of current char.

seen = {}
left = 0
max_len = 0

for right, char in enumerate(s):
    if char in seen and seen[char] >= left:
        left = seen[char] + 1      ← jump past the duplicate
    seen[char] = right
    max_len = max(max_len, right - left + 1)

TRACE: s="abcabcbb"

  r=0,c=a: seen={a:0},left=0,len=1
  r=1,c=b: seen={a:0,b:1},left=0,len=2
  r=2,c=c: seen={a:0,b:1,c:2},left=0,len=3
  r=3,c=a: a in seen, seen[a]=0>=left=0 → left=1
           seen={a:3,b:1,c:2},left=1,len=3
  r=4,c=b: b in seen, seen[b]=1>=left=1 → left=2
           seen={a:3,b:4,c:2},len=3
  r=5,c=c: c in seen, seen[c]=2>=left=2 → left=3, len=3
  r=6,c=b: b in seen, seen[b]=4>=left=3 → left=5, len=2
  r=7,c=b: left=7, len=1

Answer: 3 ✅ ("abc")
```

### Pattern 4: Memoization (Hash Map as Cache)

```
CLASSIC: Fibonacci with memoization

memo = {}

def fib(n):
    if n in memo: return memo[n]      ← O(1) lookup
    if n <= 1: return n
    memo[n] = fib(n-1) + fib(n-2)    ← compute once
    return memo[n]                    ← store for future

Hash map turns O(2ⁿ) into O(n) by caching subproblem results.
The key = subproblem input. The value = subproblem result.
This is the foundation of dynamic programming via memoization.
```

---

## 13. Real-World Applications

| Domain | Problem | Hash Map/Set's Role |
|---|---|---|
| **Databases** | Hash joins, indexed lookups | Hash map on join key for O(1) matching |
| **Compilers** | Symbol table (variable → type/location) | Hash map for O(1) identifier resolution |
| **Caches** | CPU L1/L2, web cache (Redis) | Hash map: URL/key → cached response |
| **Spell checkers** | Valid word lookup | Hash set of dictionary words |
| **Routers** | ARP table (IP → MAC address) | Hash map for O(1) address resolution |
| **Blockchain** | Transaction deduplication | Hash set of seen transaction IDs |
| **Game engines** | Entity component systems | Hash map: entity ID → component data |
| **Browsers** | DNS cache, visited links | Hash map: domain → IP, hash set: visited URLs |
| **Programming languages** | Object property lookup (JavaScript objects) | Hash map: property name → value |
| **Search engines** | Inverted index (word → document list) | Hash map for O(1) term lookup |

### JavaScript Objects as Hash Maps

```javascript
// JavaScript objects ARE hash maps under the hood
const obj = {};
obj["key"] = "value";    // hash map put
obj["key"];              // hash map get
"key" in obj;            // hash map contains

// V8 engine optimization:
//   Fast path: "hidden classes" for objects with stable structure
//   Slow path: hash table for dynamic objects
//   Objects used as hash maps deliberately → always hash table path

const map = new Map();   // explicit hash map (keys can be non-strings)
map.set(42, "integer key");
map.set({}, "object key");  // object reference as key
map.get(42);  // "integer key"
```

### Redis — Distributed Hash Map

```
Redis: in-memory key-value store = distributed hash map

  SET user:alice:score 95        ← hash map put
  GET user:alice:score           ← hash map get: O(1)
  EXISTS user:alice:score        ← hash map contains: O(1)

  Internally: sds strings + hash table
  Load factor threshold: 1.0 (triggers rehashing)
  Incremental rehashing: don't block while rehashing large tables
    → Use TWO hash tables simultaneously during resize
    → Gradually move entries from old to new table
    → Reads check both tables; writes go to new table
    → Eliminates O(n) resize pause → always responsive

Redis's incremental rehashing is a real-world solution to the
"O(n) resize is unacceptable in production" problem.
```

---

## 14. Comparison With Related Data Structures

```
              ┌──────────────────────────────────────────────────────────┐
              │              KEY LOOKUP DATA STRUCTURES                   │
              └──────────────────────────┬───────────────────────────────┘
                                         │
       ┌──────────────────┬──────────────┼──────────────┬────────────────┐
       ▼                  ▼             ▼              ▼                ▼
  HASH MAP            BALANCED        TRIE           ARRAY           SORTED
  (HASH TABLE)        BST                            (LINEAR)        ARRAY
  ──────────          ────────        ────           ───────         ──────
  O(1) avg            O(log n)        O(m)           O(n)            O(log n)
  O(n) worst          O(log n)        O(m)           O(1) if sorted  O(log n)
  No ordering         Ordered         Prefix ops     Index only      Full order
  Any hashable key    Comparable key  String keys    Int index only  Comparable
  O(n) space          O(n) space      O(n×m) space   O(n) space      O(n) space
  No range queries    Range queries   Prefix queries No range        Range queries
  No sorted iteration Sorted iter.   Sorted iter.   No              Sorted iter.
```

**Hash Map vs BST (Balanced):**
Hash map gives O(1) average lookup; BST gives O(log n) guaranteed. Hash map has no ordering; BST supports range queries, floor/ceiling, sorted iteration. Use hash map when you need maximum lookup speed and don't care about order. Use BST (TreeMap in Java) when you need ordering operations alongside lookup.

**Hash Map vs Trie:**
Both give O(m) worst-case for string keys (m = key length). Trie additionally supports prefix queries natively. Hash map can't answer "all keys starting with prefix X" without scanning all keys. For prefix-heavy string operations — trie. For general key-value lookup — hash map.

**Hash Set vs Sorted Array:**
Sorted array enables O(log n) binary search and preserves order; hash set gives O(1) average lookup. If you need to know "is X in the set?" without caring about order — hash set. If you need sorted iteration, range queries, or order-sensitive operations — sorted array/BST.

---

## 15. The Decision Framework

```
Do you need to look up values by key?
    │
    ├── Keys are strings with prefix queries?
    │       → Trie
    │
    ├── Need ordered iteration / range queries?
    │       → Balanced BST (TreeMap, SortedDict)
    │
    ├── Need O(1) average lookup, no ordering needed?
    │       → Hash Map ✅
    │
    └── Just membership testing (no values)?
            → Hash Set ✅

Special cases:
  ├── Many duplicate keys, need counts?       → Hash Map {key: count}
  ├── Cache with eviction policy?             → Hash Map + Doubly Linked List (LRU)
  ├── Need persistence / disk storage?        → B-Tree (databases)
  ├── Need worst-case O(1) (not average)?     → Cuckoo hashing
  └── Distributed key-value store?            → Consistent hashing
```

---

## 16. Tips for Long-Term Retention

**1. The post office mailbox image**
Every time you think "hash map," picture numbered mailboxes and a rule for assigning them. Hash function = assignment rule. Collision = two people, one mailbox. Chaining = stack mail in the mailbox. Probing = check the next mailbox. This single image encodes the entire structure.

**2. O(1) comes from array indexing, not magic**
Hash map lookup is O(1) for the same reason `arr[5]` is O(1): you compute a memory address arithmetically and go directly there. The hash function converts your key into the index. Once you see it as "turn key into array index," the O(1) feels inevitable rather than mysterious.

**3. The four properties of a good hash function**
Deterministic, uniform, fast, avalanche. If a hash function lacks any of these, the data structure degrades. Deterministic → correct lookups. Uniform → few collisions. Fast → O(1) per operation. Avalanche → no clustering of similar keys. Test any new hash function against all four.

**4. Mutable keys break everything**
This is the most common hash map mistake. Keys must be immutable because changing a key after insertion makes it unreachable — its new hash doesn't match its stored position. In Python: use strings, ints, tuples as keys — never lists or dicts. In Java: override both `equals()` and `hashCode()` consistently.

**5. Load factor is the performance dial**
The entire performance story is controlled by load factor. Low load factor → few collisions → fast but wasteful. High load factor → many collisions → space-efficient but slow. The resize threshold (0.75 in Java, 0.67 in Python) is a carefully calibrated balance. When something "feels slow" in a hash map — check the load factor.

**6. Complement pattern: `target - x` unlocks hash map solutions**
The two-sum pattern (`target - x` as the complement to look up) generalizes to dozens of problems: subarray sum = k, two numbers with given difference, pairs with given product. Whenever a problem asks "find two things that combine to some target," think: for each element, store it in a hash map and look up its complement. This single pattern handles an enormous class of problems.

**7. Hash map = instant lookup, hash set = instant membership**
These two use cases cover 90% of hash map/set applications in interviews and practice. When you see "find if X exists" → hash set. When you see "given X, return Y" → hash map. Start here and layer complexity on top.

---

A hash map is fundamentally a **bridge between the flexibility of arbitrary keys and the speed of array indexing**. Arrays are the fastest data structure for access — O(1) by index — but can only be indexed by integers. The real world has string names, compound identifiers, object references. The hash function is the bridge: it converts any key into an integer index, and suddenly any key gets array-speed access. The collision resolution handles the unavoidable imperfection of this mapping. The load factor and resizing maintain the bridge's integrity as data grows. Together, these pieces produce the data structure that underlies dictionaries, caches, database indexes, symbol tables, and most of the lookup-intensive code running in the world today.
