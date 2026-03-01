# Pattern 23: Trie (Prefix Tree)

## Diagram + Intuition

### Pattern Diagram
```text
root
 └─ a ─ p ─ p* ─ l ─ e*
```

### Read-the-Question Trigger Cues
- Prefix search, dictionary, autocomplete, many shared prefixes.

### Intuition Anchor
- "Store characters as paths, not full repeated strings."

### 3-Second Pattern Check
- Do prefix checks happen frequently?

## What This Pattern Solves
Efficient prefix operations on strings such as insert, search, startsWith, and dictionary matching.

## Recognition Signals
- Many words with shared prefixes.
- Need fast prefix checks/autocomplete.
- Need repeated dictionary matching across text/grid.

## Core Intuition
Store characters along edges from root:
- each node represents a prefix
- terminal flag marks complete words

Prefix operations become proportional to query length, not number of words.

## Step-by-Step Method
1. Define trie node with:
   - children map/array
   - `is_word` boolean
2. Insert by creating missing child nodes char by char.
3. Search by traversing chars; success requires terminal flag.
4. Prefix query requires path existence only.

## Detailed Example
Insert: `"apple"`, `"app"`
1. Shared path `a -> p -> p`.
2. Mark node after second `p` as word (`"app"`).
3. Continue `l -> e` and mark terminal for `"apple"`.

## Complexity
- Insert/search/prefix: `O(L)` where `L` is word length
- Space: proportional to total stored characters/prefix nodes

## Python Template
```python
class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_word = False


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        node = self.root
        for ch in word:
            if ch not in node.children:
                node.children[ch] = TrieNode()
            node = node.children[ch]
        node.is_word = True

    def search(self, word):
        node = self.root
        for ch in word:
            if ch not in node.children:
                return False
            node = node.children[ch]
        return node.is_word
```

## Common Pitfalls
- Forgetting separate terminal marker for complete words.
- Excessive memory from dense child structures where sparse map is better.
- Not deleting/unmarking correctly for mutable dictionary variants.
- Failing to backtrack visited cells correctly in grid + trie search.

## Variations
- Word Dictionary with wildcard search (`.`)
- Word Search II (trie + DFS)
- Replace Words
- Autocomplete systems (with frequency metadata)

## Interview Tips
- Contrast with hash set: trie wins on prefix operations.
- Mention memory/speed tradeoff (array children faster, map smaller).
- For Word Search II, prune leaf branches after found words for speed.

## Practice Problems
- Implement Trie (Prefix Tree)
- Design Add and Search Words Data Structure
- Word Search II
- Replace Words
