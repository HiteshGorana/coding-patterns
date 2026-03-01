# Hashing / Hash Maps / Sets (Interview-Ready Guide)

Using `[TOPIC] = Hashing & Hash Maps/Sets`.

## 0) Scope (Checklist)
- [x] Frequency counting
- [x] Two-sum / k-sum hashing
- [x] Group anagrams
- [x] Prefix sum + hash map (subarray sum equals k)
- [x] Custom hashing considerations (collisions conceptually)

## 1) Foundations
Hashing maps keys to buckets for near-constant-time lookup.

Core terms:
- Hash function, bucket, collision, load factor, rehash
- Map (`key -> value`) and set (`key` only)
- Average vs worst-case complexity

Mental model:
- Store facts about what you have seen so far.
- Trade memory for speed by avoiding repeated scans.

## 2) How it works
Cause-effect:
1. Transform object into key (number/string/tuple/signature).
2. Query map/set in average `O(1)`.
3. Update state as you scan.
4. Resolve collisions via chaining/open addressing (runtime dependent).

Tiny trace (`subarray sum = k`, `nums=[1,2,1]`, `k=3`):
- Prefix `0` count map `{0:1}`
- Read `1`: pref=1, need=-2 not found, map[1]+=1
- Read `2`: pref=3, need=0 found once -> answer +=1
- Read `1`: pref=4, need=1 found once -> answer +=1
- Result: 2 subarrays

## 3) Patterns (Interview Templates)
1. Membership set template
2. Frequency map template
3. Complement map (`target-x`)
4. Canonical key grouping (sorted string or count tuple)
5. Prefix sum count map

Invariants:
- Map state must represent processed prefix only.
- Check-before-update or update-before-check depends on problem semantics.
- Canonical key must be deterministic.

Signals:
- "Duplicate/count/first unique"
- "Pair sum in linear time"
- "Group by structural equivalence"

## 4) Examples (Easy -> Medium -> Hard)
1. Easy: Contains Duplicate
- Approach: insert into set, if already present return true.

2. Medium: Group Anagrams
- Approach: key by sorted string or 26-char frequency vector.
- Trace: `"eat","tea","tan"` -> keys `"aet","aet","ant"` -> two groups.

3. Medium: Two Sum
- Approach: complement lookup during one pass.

4. Hard: Subarray Sum Equals K
- Approach: prefix sum + map frequency.
- Trace shown in section 2.

5. Hard: Longest Consecutive Sequence
- Approach: set, start only at numbers with no predecessor (`x-1` missing).

## 5) Why & What-if
Edge cases:
- Empty input
- Repeated large keys
- Negative numbers in prefix sum

Pitfalls:
- Using mutable objects as unstable keys
- Wrong update order in prefix sum problems
- Assuming worst-case `O(1)` (it is average)

Why it works:
- Constant-time expected lookup compresses repeated search.

Variations:
- Custom objects need consistent `hash` + equality.
- Memory-heavy cases may need sorting alternative (`O(n log n)`).

## 6) Complexity and Tradeoffs
- Typical map/set ops: average `O(1)`, worst `O(n)`
- Grouping/anagram counting: usually `O(n * k)` where `k` is string length
- Prefix-sum map methods: `O(n)` time, `O(n)` space

Tradeoffs:
- Hashing fast on average but uses extra memory.
- Sorting approach can be slower but deterministic and memory-friendlier in some settings.

## 7) Real-world uses
- Caches and key-value stores
- Session/user lookup
- Log deduplication
- Counting analytics and aggregation pipelines

## 8) Comparisons
- Hash map vs balanced BST map:
  - Hash map: average `O(1)`, unordered
  - BST map: `O(log n)`, ordered iteration
- Set vs bitset:
  - Bitset is smaller/faster when key range is small and known.

## 9) Retention
Cheat sheet:
- Seen-before check -> set
- Count frequencies -> map
- Prefix relation -> prefix hash map
- Pair lookup -> complement map

Recall hooks:
- "Remember the past to avoid rescanning."
- "Canonical key means same group."

Practice (10):
1. Easy: Contains Duplicate
2. Easy: Valid Anagram
3. Easy: Intersection of Two Arrays
4. Medium: Two Sum
5. Medium: Group Anagrams
6. Medium: Top K Frequent Elements
7. Medium: Isomorphic Strings
8. Hard: Subarray Sum Equals K
9. Hard: Longest Consecutive Sequence
10. Hard: Minimum Window Substring (frequency map)
