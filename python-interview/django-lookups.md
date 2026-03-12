# Django Lookups

## What "Django Lookup" Means

In Django, a lookup is the ORM mechanism used to describe conditions in a query.

You most commonly see lookups in:

- `filter()`
- `exclude()`
- `get()`

Example:

```python
User.objects.filter(username__icontains="aman")
```

Here, `icontains` is the lookup.

At a high level, Django lookups are the Python ORM version of SQL `WHERE` conditions.

---

## Why It Matters

Django lookups matter because they let you:

- query the database without writing raw SQL
- filter across related tables
- express comparisons clearly and safely
- compose conditions incrementally
- keep query logic inside the ORM

If you understand lookups deeply, you can reason about:

- what SQL Django is likely generating
- why some filters are fast and others are expensive
- how joins happen across relationships
- where subtle bugs come from with `NULL`, relations, and JSON paths

---

## The Core Formula

The most important mental model is:

```text
field_path__transform__lookup = value
```

Examples:

```python
Book.objects.filter(title__icontains="django")
Order.objects.filter(total__gte=500)
Entry.objects.filter(pub_date__year=2025)
Entry.objects.filter(blog__name__iexact="tech")
```

Breakdown:

- `field_path`: where to read data from
- `transform`: reshape the left-hand side before comparing
- `lookup`: the final comparison operator
- `value`: the right-hand-side comparison value

If the final lookup is omitted, Django assumes `exact`.

Example:

```python
User.objects.filter(id=10)
User.objects.filter(id__exact=10)
```

These are equivalent.

---

## 1. The Basics

### 1.1 Field Path

The field path tells Django which field to target.

Simple example:

```python
Book.objects.filter(title="Clean Code")
```

Here the field path is just `title`.

Across relations:

```python
Entry.objects.filter(blog__name="Tech")
```

Here the field path is `blog__name`.

That means:

- start from `Entry`
- follow the `blog` relation
- then read the `name` field on `Blog`

Analogy:

- the field path is like walking through rooms in a building until you reach the drawer you want

```text
Entry -> blog -> name
```

---

### 1.2 Lookup

A lookup is the final comparison operation.

Common examples:

- `exact`
- `iexact`
- `contains`
- `icontains`
- `gt`
- `gte`
- `lt`
- `lte`
- `in`
- `isnull`
- `startswith`
- `endswith`

Examples:

```python
Product.objects.filter(price__gt=1000)
User.objects.filter(email__iendswith="@company.com")
Post.objects.filter(deleted_at__isnull=True)
```

Think of the lookup as the final question being asked:

- equal?
- greater than?
- contains?
- starts with?
- null?

---

### 1.3 Transform

A transform modifies the field before the final lookup runs.

Example:

```python
Entry.objects.filter(pub_date__year=2025)
```

Here:

- `pub_date` is the field
- `year` is a transform
- `exact` is implied

Another example:

```python
Entry.objects.filter(pub_date__year__gte=2024)
```

This means:

```text
take pub_date
-> extract year
-> compare using >= 2024
```

Transforms are important because they explain why chained lookup syntax works.

---

## 2. Core Components

### 2.1 QuerySet

Lookups are used on QuerySets.

Example:

```python
qs = Book.objects.filter(title__icontains="python")
```

`qs` is still a QuerySet, not the final result list.

Important point:

- QuerySets are lazy
- the lookup is parsed and stored first
- SQL is generated later when the QuerySet is evaluated

---

### 2.2 Lookup Expression

A lookup expression is usually passed as a keyword argument:

```python
field__lookup=value
```

Examples:

```python
User.objects.filter(age__gte=18)
Invoice.objects.filter(status__in=["paid", "sent"])
```

Under the hood, Django resolves:

- the left-hand side field or expression
- the lookup class
- the right-hand side value

---

### 2.3 Relation Traversal

Django uses double underscore syntax to traverse relationships.

Example:

```python
Entry.objects.filter(blog__owner__email__icontains="admin")
```

Diagram:

```text
Entry
  -> Blog
      -> Owner
          -> Email
              -> icontains "admin"
```

Django turns this into the required SQL joins automatically.

Cause-effect:

- more relationship hops usually mean more joins
- more joins can increase query cost

---

### 2.4 Built-in Lookup Types

Common categories:

#### Equality

- `exact`
- `iexact`

#### String matching

- `contains`
- `icontains`
- `startswith`
- `istartswith`
- `endswith`
- `iendswith`

#### Range/comparison

- `gt`
- `gte`
- `lt`
- `lte`
- `range`

#### Membership

- `in`

#### Null checks

- `isnull`

#### Date/time related

- `date`
- `year`
- `month`
- `day`

#### Regular expressions

- `regex`
- `iregex`

---

## 3. How Django Lookups Work

### 3.1 Basic Process

Take this example:

```python
Entry.objects.filter(blog__name__icontains="django")
```

Django roughly does the following:

1. Split the keyword into parts:
   - `blog`
   - `name`
   - `icontains`
2. Resolve `blog` as a relation.
3. Resolve `name` as the target field on the related model.
4. Resolve `icontains` as the final lookup.
5. Prepare the right-hand-side value `"django"`.
6. Build joins and SQL conditions.
7. Keep the QuerySet lazy until evaluation.

Conceptual diagram:

```text
blog__name__icontains="django"
        ->
follow relation path
        ->
select target column
        ->
apply lookup logic
        ->
generate SQL WHERE clause
```

---

### 3.2 Cause and Effect

#### Why does `field=value` work?

Because Django inserts `exact` automatically.

```python
User.objects.filter(username="aman")
```

is the same as:

```python
User.objects.filter(username__exact="aman")
```

#### Why does `blog__name="Tech"` create a join?

Because the field path crosses a relationship, so Django must join the related table.

#### Why does `pub_date__year=2025` work?

Because `year` is a transform and `exact` is implied afterward.

#### Why does `icontains` behave differently from `contains`?

Because `icontains` is case-insensitive and uses different database comparison behavior.

---

### 3.3 A Useful Analogy

Think of a lookup like asking a librarian for books.

```text
library section -> shelf -> comparison rule -> target value
```

Example:

```python
Book.objects.filter(author__name__icontains="martin")
```

This is like saying:

- go to the related author record
- take the author's name
- compare it case-insensitively
- keep rows where it contains "martin"

---

## 4. Simple Examples

### Equality

```python
User.objects.filter(username__exact="aman")
User.objects.filter(username="aman")
```

### Case-insensitive string match

```python
User.objects.filter(username__icontains="aman")
```

### Numeric comparison

```python
Order.objects.filter(total__gte=1000)
```

### Membership

```python
Book.objects.filter(id__in=[1, 2, 3, 4])
```

### Null checks

```python
User.objects.filter(last_login__isnull=True)
```

### Date transform

```python
Entry.objects.filter(pub_date__year=2026)
```

### Across relationships

```python
Entry.objects.filter(blog__owner__email__iendswith="@company.com")
```

---

## 5. Why Questions

### Why use Django lookups instead of raw SQL?

Because lookups give you:

- ORM abstraction
- portability across supported databases
- safer parameter handling
- relationship-aware queries
- composition with QuerySets, `Q`, `F`, `annotate()`, and `Subquery`

Raw SQL is still useful, but lookups are usually the right default.

---

### Why is the `__` syntax so powerful?

Because it lets Django encode:

- field selection
- relationship traversal
- transforms
- comparisons

all in one compact format.

---

### Why are lookups important for performance reasoning?

Because different lookups imply different SQL behavior.

Examples:

- `exact` on indexed fields is often fast
- `icontains` can be expensive
- relationship traversal may add joins
- transforms may prevent efficient index use depending on the database

So lookup choice changes performance characteristics.

---

## 6. What If Questions

### What if I omit the lookup?

Django uses `exact`.

```python
Book.objects.filter(title="Django")
```

means:

```python
Book.objects.filter(title__exact="Django")
```

---

### What if I compare a field to `None`?

Django usually translates that into SQL `IS NULL`.

Example:

```python
User.objects.filter(last_login=None)
```

Often, the clearer form is:

```python
User.objects.filter(last_login__isnull=True)
```

---

### What if I use `exclude()`?

`exclude()` negates conditions, but behavior can become subtle across multi-valued relations.

Example:

```python
Blog.objects.exclude(entry__headline__contains="Draft")
```

This is not always identical to the mental model "remove blogs where one specific related row matches in exactly this way." Multi-row joins can make negation less intuitive.

Practical takeaway:

- be especially careful with `exclude()` on reverse relations and many-to-many relationships

---

### What if I search with `%` or `_` in a string lookup?

For `contains`, `icontains`, `startswith`, and similar lookups, Django escapes those characters so they are treated safely in SQL `LIKE` patterns.

That prevents accidental wildcard behavior.

---

### What if I mistype a JSON key path?

With `JSONField`, typos can be tricky because unknown path pieces may be interpreted as JSON keys instead of causing an obvious error.

Example idea:

```python
Dog.objects.filter(data__owner__name="Bob")
```

If part of that path is misspelled, Django may still treat it as a JSON key lookup.

Practical takeaway:

- test JSON lookups carefully
- do not assume typos will always fail loudly

---

### What if I need a lookup Django does not provide?

You can create a custom lookup or custom transform and register it on a field type.

Conceptually:

- a custom lookup defines a new comparison
- a custom transform defines a new left-hand-side transformation

This is useful for domain-specific query behavior.

---

## 7. Practical Applications

### Search Features

```python
User.objects.filter(name__icontains=query)
```

Use case:

- user search bar
- admin search
- dashboard filters

---

### Date Filtering

```python
Invoice.objects.filter(created_at__year=2026)
Invoice.objects.filter(created_at__date=today)
```

Use case:

- reports
- analytics pages
- monthly summaries

---

### E-commerce Filtering

```python
Product.objects.filter(price__gte=min_price, price__lte=max_price)
Product.objects.filter(category__slug__in=slugs)
```

Use case:

- price range filters
- category filters
- faceted product browsing

---

### Relationship-Based Business Rules

```python
Order.objects.filter(customer__email__iendswith="@enterprise.com")
```

Use case:

- customer segmentation
- multi-table reporting
- staff/admin data slicing

---

### Soft Delete Patterns

```python
Post.objects.filter(deleted_at__isnull=True)
```

Use case:

- active row filtering
- admin views
- API visibility rules

---

### JSON Metadata Filtering

```python
Event.objects.filter(metadata__source="api")
```

Use case:

- event ingestion systems
- semi-structured data
- analytics payload filtering

---

## 8. Comparison with Related Ideas

### Lookup vs Transform

Transform changes the field before comparison.

Lookup performs the final comparison.

Example:

```python
Entry.objects.filter(pub_date__year__gte=2025)
```

Here:

- `year` is a transform
- `gte` is a lookup

---

### Lookup vs `Q` Objects

A lookup describes one condition.

`Q` objects combine conditions.

Example:

```python
from django.db.models import Q

User.objects.filter(
    Q(username__icontains="aman") | Q(email__icontains="aman")
)
```

So:

- lookup = one predicate
- `Q` = boolean composition of predicates

---

### Lookup vs `F()` Expressions

Lookup compares.

`F()` references another field or expression.

Example:

```python
from django.db.models import F

Product.objects.filter(stock__lt=F("reorder_level"))
```

Here:

- `lt` is the lookup
- `F("reorder_level")` is the right-hand-side field expression

---

### Lookup vs `annotate()`

Lookup filters rows.

`annotate()` computes extra values.

Example:

```python
Blog.objects.annotate(num_entries=Count("entry")).filter(num_entries__gt=10)
```

So:

- `annotate()` creates data
- lookup filters on that data

---

### Lookup vs Raw SQL

Lookups are:

- safer
- composable
- ORM-native
- relationship-aware

Raw SQL is:

- lower-level
- more flexible
- sometimes necessary

Default rule:

- use lookups first
- use raw SQL only when the ORM stops being the right tool

---

## 9. Common Edge Cases and Gotchas

### Case Sensitivity Depends on Lookup and Database

`contains` and `icontains` are not the same.

You should know whether your comparison is case-sensitive and whether the database has collation-specific behavior.

---

### Lookups Across Reverse and Many-to-Many Relations Can Duplicate Rows

Example:

```python
Blog.objects.filter(entry__headline__icontains="django")
```

A blog with multiple matching entries may appear multiple times unless you use:

```python
.distinct()
```

Cause:

- SQL joins can produce repeated parent rows

---

### Negation Can Be Subtle

`exclude()` is not always as intuitive as "just negate the filter" when joins are involved.

This is especially true for:

- reverse foreign keys
- many-to-many relations

---

### Transform-Based Filtering Can Affect Index Usage

Example:

```python
Entry.objects.filter(pub_date__year=2026)
```

Depending on the database and index structure, applying transforms in the query may reduce index efficiency.

Practical lesson:

- think about the SQL shape, not just the Python syntax

---

## 10. Diagrams and Mental Models

### The Main Formula

```text
field_path__transform__lookup = value
```

Example:

```text
blog__name__icontains = "django"
```

means:

```text
Entry
  -> follow blog relation
  -> read blog.name
  -> apply icontains
  -> compare with "django"
```

---

### Join Mental Model

```text
Entry table
   JOIN Blog table
   WHERE Blog.name matches condition
```

---

### Transform Mental Model

```text
pub_date__year__gte=2025

pub_date
  -> extract year
  -> compare using >= 2025
```

---

## 11. Retention Tips

### Learn the Formula First

Memorize:

```text
field path -> transforms -> final lookup -> value
```

If that becomes automatic, everything else gets easier.

---

### Memorize Five Anchor Examples

Keep these in your head:

```python
name__icontains="aman"
price__gte=1000
created_at__year=2026
author__email__iendswith="@company.com"
deleted_at__isnull=True
```

These cover:

- string search
- numeric comparison
- transforms
- relationship traversal
- null checks

---

### Use a One-Line Memory Hook

Use this sentence:

- "Find the field, optionally reshape it, then apply the final comparison."

---

### Think in SQL Terms

Whenever you write a lookup, ask:

- what column is this targeting?
- does this add a join?
- does this use `LIKE`?
- does this compare to `NULL`?
- is this likely index-friendly?

That habit makes lookup behavior much easier to retain.

---

## 12. Interview Answer Template

If someone asks, "What is a Django lookup?", a strong short answer is:

- "A Django lookup is the ORM mechanism used to express SQL-style filtering conditions in Python. It typically looks like `field__lookup=value`, and may include relation traversal and transforms, like `blog__name__icontains='django'` or `pub_date__year__gte=2025`. Django parses that chain, follows relationships, applies transforms, and generates the SQL `WHERE` clause lazily through the QuerySet."

---

## 13. Quick Revision Notes

- Django lookups power `filter()`, `exclude()`, and `get()`.
- Basic form is `field__lookup=value`.
- Full form is `field_path__transform__lookup=value`.
- If lookup is omitted, Django uses `exact`.
- Double underscore also traverses relations.
- Transforms reshape the field before comparison.
- Lookups define the final comparison.
- Complex paths can add joins and cost.
- `exclude()` on multi-valued relations needs care.
- JSON path lookups can hide typos.
- Use `Q` for boolean composition and `F()` for field references.
