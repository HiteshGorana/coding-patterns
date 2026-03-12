# MySQL Internals

## Scope

When people discuss MySQL internals in interviews, they almost always mean **MySQL with the InnoDB storage engine**.

That is the useful default mental model.

---

## Big Picture

For a lookup like:

```sql
SELECT * FROM users WHERE id = 42;
```

InnoDB roughly does:

```text
parse query
  ->
optimizer chooses plan
  ->
traverse clustered index
  ->
find row in leaf page
  ->
return result
```

For a secondary index lookup, the path is different and more expensive.

---

## Core Storage Model

### Clustered Primary Key Index

InnoDB stores table data in the primary key B-tree itself.

That means:

- leaf pages of the primary key contain the full row

This is one of the most important MySQL internals facts.

Cause-effect:

- primary key lookups are efficient
- row order on disk is tied to primary key clustering

---

### Secondary Indexes

A secondary index in InnoDB stores:

- secondary key
- primary key value

It does **not** usually store the full row.

So a secondary index lookup often becomes:

1. search secondary index
2. get matching primary key
3. search clustered primary key index
4. fetch full row

This is sometimes called a double lookup.

---

### Buffer Pool

InnoDB keeps pages in memory in the buffer pool.

This is a huge performance factor.

If hot index and data pages stay in the buffer pool:

- reads become much faster

---

### Redo Log and Undo Log

InnoDB uses logging for durability and MVCC behavior.

Simplified roles:

- redo log helps recover committed changes
- undo data helps support rollback and version visibility

This supports transactions and crash recovery.

---

## How a Lookup Works

### Primary Key Lookup

Example:

```sql
SELECT * FROM users WHERE id = 42;
```

If `id` is the primary key:

1. traverse clustered B-tree
2. reach leaf page
3. row is already there
4. return result

This is why primary key lookups are very efficient in InnoDB.

---

### Secondary Index Lookup

Example:

```sql
SELECT * FROM users WHERE email = 'a@example.com';
```

If `email` is a secondary index:

1. traverse secondary index
2. get primary key of matching row
3. traverse clustered primary key index
4. fetch full row

Cause-effect:

- secondary index lookups are usually more expensive than clustered primary key lookups

---

### Covering Index

If the query only needs columns present in the index, InnoDB may avoid the extra row fetch.

Example idea:

```sql
SELECT email FROM users WHERE email = 'a@example.com';
```

If the index already covers the needed data, lookup becomes cheaper.

---

## Why Questions

### Why Is Primary Key Design So Important in InnoDB?

Because the table is physically organized around the clustered primary key.

This affects:

- storage layout
- page locality
- secondary index size
- insert/update behavior

---

### Why Do Secondary Indexes Cost More?

Because they generally require two navigation steps:

- secondary index lookup
- clustered primary key lookup

---

### Why Does a Large Primary Key Hurt Secondary Indexes?

Because secondary indexes store the primary key value with each entry.

Larger primary keys make secondary indexes larger.

---

## What If Questions

### What If There Is No Primary Key?

InnoDB still needs clustered organization and may create a hidden internal row identifier.

That is why explicit primary keys are usually better.

---

### What If the Query Returns Many Rows?

The optimizer may prefer a scan rather than lots of random index lookups.

---

### What If the Index Covers the Query?

Then InnoDB can avoid extra row fetches and the query gets cheaper.

---

## Practical Applications

- choosing good primary keys
- understanding why covering indexes help
- reading `EXPLAIN`
- diagnosing why secondary-index-heavy workloads slow down

---

## Compare With Other Databases

### MySQL/InnoDB vs PostgreSQL

InnoDB:

- clustered primary key
- secondary indexes store PK values

PostgreSQL:

- heap table
- indexes point to heap tuples

### MySQL/InnoDB vs MongoDB

InnoDB is row-oriented and relational.

MongoDB is document-oriented and often optimized around whole-document access patterns.

---

## Retention Tips

Remember InnoDB with this sentence:

- "InnoDB stores rows in the clustered primary key, and secondary indexes usually require a second lookup through that primary key."
