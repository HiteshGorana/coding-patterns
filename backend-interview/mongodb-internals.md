# MongoDB Internals

## What Makes MongoDB Internally Distinct

MongoDB is a document database.

Instead of storing rows in normalized tables, it stores BSON documents inside collections.

That changes lookup behavior, indexing patterns, schema design, and join strategy.

---

## Big Picture

For a query like:

```javascript
db.users.find({ email: "a@example.com" })
```

MongoDB roughly does:

```text
parse query
  ->
query planner chooses index scan or collection scan
  ->
traverse index if useful
  ->
fetch matching documents
  ->
return BSON documents
```

---

## Core Storage Model

### Collections and Documents

MongoDB stores:

- collection = group of documents
- document = structured BSON object

Example:

```json
{
  "_id": 42,
  "name": "Aman",
  "email": "aman@example.com",
  "address": {
    "city": "Delhi"
  }
}
```

This document-oriented model is why MongoDB handles nested data naturally.

---

### BSON

MongoDB stores data as BSON, a binary form related to JSON.

Why BSON matters:

- richer typed storage than plain JSON
- efficient transport/storage representation

---

### Default `_id` Index

MongoDB automatically creates an index on `_id`.

This makes `_id` lookups efficient by default.

Example:

```javascript
db.users.find({ _id: 42 })
```

---

### Additional Indexes

MongoDB also uses indexes, typically B-tree based.

Common indexed fields:

- email
- createdAt
- status
- nested document fields

MongoDB can index nested paths like:

```javascript
{ "address.city": 1 }
```

---

## How a Lookup Works

### Indexed Lookup

Example:

```javascript
db.users.find({ email: "a@example.com" })
```

If `email` is indexed:

1. traverse the index
2. identify matching document locations
3. fetch documents
4. return results

---

### Collection Scan

If there is no useful index, MongoDB may scan the whole collection.

That means:

- inspect many or all documents
- apply filter document by document

This can become expensive fast on large collections.

---

### Embedded Data Lookup

MongoDB handles nested lookups naturally.

Example:

```javascript
db.users.find({ "address.city": "Delhi" })
```

This is a major difference from relational systems, where similar data is often normalized across tables.

---

## Why Questions

### Why Is MongoDB Good for Nested Data?

Because documents can store related data together.

This reduces the need for joins in many use cases.

---

### Why Can Document Size Matter?

Because MongoDB often reads/writes documents as larger units.

Very large documents can make updates and retrieval more expensive.

---

### Why Are Indexes Still Important in MongoDB?

Because without an index, the database may have to scan the collection.

Document model flexibility does not remove the need for access-path optimization.

---

## What If Questions

### What If I Model Everything as One Huge Document?

Reads may become simple, but:

- document growth can hurt performance
- updates become heavier
- duplication may increase

Embedding is powerful, but not unlimited.

---

### What If I Normalize Too Much in MongoDB?

Then you may reintroduce join-like complexity and lose some of MongoDB's document-model advantages.

---

### What If There Is No Useful Index?

Expect collection scans, higher latency, and reduced scalability.

---

## Practical Applications

- modeling event data
- user profiles with nested settings
- content documents
- catalogs with flexible attributes
- APIs where documents map naturally to returned JSON

---

## Compare With Other Databases

### MongoDB vs PostgreSQL

MongoDB:

- document model
- nested structure is natural
- fewer joins in many common patterns

PostgreSQL:

- relational model
- normalized schemas
- stronger join-centric querying

### MongoDB vs InnoDB

MongoDB emphasizes document-oriented access and schema flexibility.

InnoDB emphasizes row storage, transactions, and relational structure.

---

## Retention Tips

Remember MongoDB with this sentence:

- "MongoDB stores BSON documents in collections, uses indexes to avoid collection scans, and shines when related data fits naturally inside one document."
