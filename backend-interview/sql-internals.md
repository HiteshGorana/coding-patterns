# SQL Internals

## What "SQL Internals" Means

SQL internals means understanding how a relational database executes SQL under the hood.

At the surface level, you write queries like:

```sql
SELECT * FROM users WHERE id = 42;
UPDATE orders SET status = 'paid' WHERE id = 10;
SELECT * FROM products WHERE price > 1000 ORDER BY created_at DESC LIMIT 20;
```

At the internals level, the important questions are:

- How is SQL parsed and planned?
- How does the database find rows efficiently?
- What do indexes actually store?
- How do joins work internally?
- Why do some queries scan the whole table and others use an index?
- How do transactions, locks, logs, and caching fit into execution?

So "SQL internals" is the runtime model of how relational databases process queries and store data.

---

## Big Picture

Typical flow:

```text
SQL query
  ->
Parser
  ->
Query tree
  ->
Optimizer / planner
  ->
Execution plan
  ->
Storage engine + indexes + buffer cache
  ->
Rows returned or modified
```

---

## Core Components

### Tables and Rows

Relational databases store data in tables, but physically they usually organize that data in pages on disk.

Think of a table as:

- logical view: rows and columns
- physical reality: pages, tuples, metadata, indexes

---

### Pages

Databases usually read and write fixed-size blocks called pages.

Why pages matter:

- disk and memory I/O happen page by page
- index lookups and scans are really page access patterns

Analogy:

- a table is a book
- a page is a physical page in that book
- an index is the back-of-book index that tells you where to jump

---

### Indexes

An index is an auxiliary structure that helps the database find rows faster.

Most common type:

- B-tree index

Typical idea:

- keys are stored in sorted order
- tree traversal narrows down where matching rows live

Without an index, many queries must scan every row.

---

### Buffer Cache

The database keeps hot pages in memory.

Why:

- reading from memory is much cheaper than disk
- repeated queries benefit heavily from cached pages

---

### Transaction Manager

Transactions group operations into atomic units.

Core guarantees usually discussed as ACID:

- atomicity
- consistency
- isolation
- durability

Internally, transaction handling affects:

- row visibility
- locking
- versioning
- recovery

---

### Write-Ahead Logging

Most relational databases use a write-ahead log.

Basic rule:

- log the change before the actual data page is treated as safely written

Why:

- crash recovery
- durability
- replication

---

## How SQL Queries Work

### 1. Parsing

The database parses SQL text into an internal structure.

Example:

```sql
SELECT name FROM users WHERE id = 42;
```

The parser identifies:

- query type: `SELECT`
- table: `users`
- projection: `name`
- filter condition: `id = 42`

---

### 2. Planning / Optimization

The optimizer chooses how to run the query.

Possible choices:

- full table scan
- index scan
- index-only scan
- nested loop join
- hash join
- merge join

The optimizer uses statistics to estimate cost.

Cause-effect:

- good statistics -> better plan choice
- stale statistics -> worse plans

---

### 3. Execution

The execution engine follows the chosen plan.

For an index lookup:

1. traverse index pages
2. find matching row pointers
3. fetch actual row pages if needed
4. apply remaining filters
5. return result

---

## Why Questions

### Why Are Indexes Fast?

Because they reduce search space.

Instead of scanning every row, the database navigates a tree or another index structure to jump near the answer.

---

### Why Can an Index Still Be Slow?

Because:

- the query may return too many rows
- the index may not match the filter/order pattern
- the planner may still prefer a scan
- extra row fetches may dominate cost

Indexes are not magic. They are selective access paths.

---

### Why Do Joins Get Expensive?

Because the database must combine rows from multiple inputs, and join strategy depends on:

- row counts
- join keys
- indexes
- memory availability
- sorting needs

---

## What If Questions

### What If There Is No Index?

The database often falls back to a sequential scan.

That can be fine for:

- small tables
- low selectivity queries

but expensive for large selective lookups.

---

### What If an Index Exists but the Query Still Scans?

Possible reasons:

- too many rows would match
- the planner estimates a scan is cheaper
- functions or casts prevent useful index use
- statistics are misleading

---

### What If Many Transactions Update the Same Rows?

Then contention appears through:

- locks
- version cleanup pressure
- deadlocks
- reduced concurrency

---

## Practical Applications

- designing indexes for production queries
- understanding slow query plans
- debugging deadlocks and isolation issues
- choosing between normalization and denormalization
- building APIs with predictable database access patterns

---

## Compare With Related Ideas

### SQL Internals vs ORM Internals

ORM internals explain how application code becomes queries.

SQL internals explain how the database executes those queries.

---

### SQL Internals vs NoSQL Internals

SQL systems usually emphasize:

- relational structure
- joins
- transactions
- schema

NoSQL systems often trade some of that for:

- flexible documents
- different scaling models
- different query patterns

---

## Retention Tips

Memorize this pipeline:

```text
query
 ->
parse
 ->
plan
 ->
index/scan
 ->
fetch pages
 ->
return rows
```

And keep these anchor ideas:

- tables are logical; pages are physical
- indexes narrow search space
- the planner picks a strategy
- transactions change visibility and concurrency
- logs make recovery possible
