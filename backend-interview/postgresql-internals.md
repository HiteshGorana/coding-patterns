# PostgreSQL Internals

## What Makes PostgreSQL Internally Distinct

PostgreSQL is a relational database with a strong focus on standards, extensibility, MVCC, and rich query execution.

Its internal mental model is especially important for understanding:

- heap tables
- secondary indexes
- MVCC tuple visibility
- vacuum
- WAL
- query planning

---

## Big Picture

For a typical lookup:

```sql
SELECT * FROM users WHERE id = 42;
```

PostgreSQL roughly does:

```text
parse query
  ->
plan query
  ->
choose index scan or seq scan
  ->
read index pages if useful
  ->
get tuple pointers
  ->
check heap tuples for visibility
  ->
return row
```

---

## Core Storage Model

### Heap Table

PostgreSQL stores table rows in a heap structure.

Important idea:

- the table itself is not physically ordered by primary key
- indexes are separate structures

This differs from systems like InnoDB where the primary key is clustered.

---

### Indexes

Indexes in PostgreSQL usually store:

- indexed key
- pointer to tuple location in heap

That means an index lookup often needs:

1. index traversal
2. heap fetch

This extra heap lookup is one reason "index scan" and "index-only scan" are different.

---

### MVCC

PostgreSQL uses Multi-Version Concurrency Control.

Instead of overwriting rows in place for everyone, PostgreSQL creates row versions.

Each tuple carries metadata such as transaction visibility info.

Cause-effect:

- readers and writers interfere less
- old row versions can accumulate
- cleanup is needed

---

### Vacuum

Because MVCC creates dead row versions, PostgreSQL needs vacuuming.

Vacuum:

- reclaims space logically
- updates visibility information
- helps prevent table bloat

Without proper vacuum:

- table bloat grows
- index bloat grows
- performance degrades

---

## How a Lookup Works

### Index Scan Path

Suppose:

```sql
SELECT * FROM users WHERE email = 'a@example.com';
```

If there is an index on `email`, PostgreSQL may:

1. traverse the B-tree index
2. find tuple locations
3. fetch tuples from heap pages
4. check whether each tuple is visible to the current transaction snapshot
5. return visible rows

Why visibility check matters:

- because MVCC means not every physical tuple is visible to every transaction

---

### Index-Only Scan

An index-only scan can happen if PostgreSQL can answer the query from the index without fetching heap rows.

But there is a catch:

- PostgreSQL still needs enough visibility information to avoid heap checks

This is where the visibility map matters.

Cause-effect:

- healthy vacuuming can make index-only scans more effective

---

## Why Questions

### Why Is PostgreSQL Heap-Based Instead of Clustered by Primary Key?

Because PostgreSQL separates table storage from index structures.

This supports flexibility, but means secondary index lookups typically lead to heap access.

---

### Why Does Vacuum Matter So Much?

Because MVCC keeps old tuple versions around until cleanup is safe.

Without vacuum:

- dead tuples remain
- table and index size grow
- more pages are scanned

---

### Why Can a Simple Lookup Still Touch the Heap?

Because PostgreSQL indexes usually point to heap tuples, not full rows.

So even if the index finds a match quickly, PostgreSQL may still need the heap page.

---

## What If Questions

### What If There Is No Useful Index?

PostgreSQL may choose a sequential scan.

This is often correct for:

- small tables
- low-selectivity predicates

---

### What If Statistics Are Wrong?

The planner may choose a poor plan.

That is why `ANALYZE` and healthy statistics matter.

---

### What If Updates Happen Frequently on Large Tables?

Then dead tuples accumulate faster, and vacuum pressure becomes more important.

---

## Practical Applications

- reading `EXPLAIN` plans
- diagnosing bloat
- understanding why index-only scans do or do not happen
- designing schemas and indexes for PostgreSQL-specific behavior

---

## Compare With Other Databases

### PostgreSQL vs InnoDB

PostgreSQL:

- heap table + separate indexes
- MVCC with tuple versions in heap
- vacuum is a central operational concern

InnoDB:

- clustered primary key storage
- secondary indexes point to primary key

### PostgreSQL vs MongoDB

PostgreSQL is relational and join-friendly.

MongoDB is document-oriented and often avoids joins through embedding.

---

## Retention Tips

Remember PostgreSQL with this sentence:

- "PostgreSQL stores rows in heap pages, indexes point into the heap, MVCC creates row versions, and vacuum keeps the system healthy."
