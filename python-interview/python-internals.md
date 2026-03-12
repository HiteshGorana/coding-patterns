# Python Internals

## What "Python Internals" Means

Python internals means understanding what Python is doing underneath your code.

It answers questions like:

- What is a Python object internally?
- What does a variable really store?
- How does Python execute code?
- Why do mutable-object bugs happen?
- Why are dictionaries fast?
- Why do threads behave differently for CPU-bound and I/O-bound work in CPython?

In interviews, "Python internals" usually does not mean memorizing CPython C source code. It means explaining Python's runtime model clearly and accurately.

---

## Why It Matters

Knowing Python internals helps you:

- debug tricky bugs involving mutation and references
- reason about performance and memory
- answer "why does Python behave like this?" questions
- choose between threads, processes, and async correctly
- explain language behavior instead of memorizing it

---

## The Big Picture

At a high level, Python execution looks like this:

```text
Python source code
        ->
Parser
        ->
AST (Abstract Syntax Tree)
        ->
Bytecode
        ->
Python Virtual Machine
        ->
Objects, function calls, output, side effects
```

Mental model:

- your code is written in Python source
- CPython compiles it to bytecode
- the Python Virtual Machine executes that bytecode
- objects are created and manipulated during execution

Python is not "just interpreted" in the simplistic sense. In CPython, source is compiled to bytecode before it is executed.

---

## 1. The Basics

### 1.1 Everything Is an Object

In Python, almost everything is an object:

- `int`
- `str`
- `list`
- `dict`
- function
- class
- module

Each object has:

- identity
- type
- value

Example:

```python
x = 42
print(id(x))
print(type(x))
print(x)
```

Think of an object like a record in memory:

```text
Object
|- identity
|- type
|- value
```

---

### 1.2 Variables Are Names, Not Boxes

This is one of the most important Python ideas.

When you do:

```python
a = [1, 2, 3]
```

`a` is not a container holding the raw list. `a` is a name bound to a list object.

Diagram:

```text
a ---> [1, 2, 3]
```

Now:

```python
b = a
```

Diagram:

```text
a ----\
       -> [1, 2, 3]
b ----/
```

If you mutate through `b`:

```python
b.append(4)
print(a)  # [1, 2, 3, 4]
```

Cause-effect:

- `a` and `b` point to the same object
- the list changes in place
- both names see the same mutation

Analogy:

- variables are sticky notes
- objects are the actual items on the desk
- two sticky notes can point to the same item

---

### 1.3 Types Define Behavior

The type of an object determines:

- what data it holds
- what operations it supports
- how it behaves

Example:

```python
"abc".upper()
[1, 2, 3].append(4)
```

Strings and lists support different methods because their types define different capabilities.

---

## 2. Core Components

### 2.1 Python Execution Model

When Python runs code, the rough process is:

1. tokenize source code
2. parse source into syntax structure
3. build an AST
4. compile AST into bytecode
5. execute bytecode using the Python Virtual Machine

Example:

```python
x = 10
y = 20
print(x + y)
```

At runtime, Python is doing work like:

- create integer objects
- bind names `x` and `y`
- look up `print`
- compute `x + y`
- pass result to `print`

---

### 2.2 Stack Frames

Every function call creates a stack frame.

A frame contains:

- local variables
- current execution state
- references to globals
- references to built-ins

Example:

```python
def add(a, b):
    c = a + b
    return c
```

Calling `add(2, 3)` creates a frame with:

```text
Frame: add
|- a = 2
|- b = 3
|- c = 5
```

Why this matters:

- recursion creates many frames
- locals live inside frames
- stack growth explains recursion depth limits

---

### 2.3 Namespaces and Scope

Python resolves names using LEGB:

- Local
- Enclosing
- Global
- Built-in

Example:

```python
x = "global"

def outer():
    x = "enclosing"

    def inner():
        x = "local"
        return x

    return inner()
```

The returned value is `"local"` because local scope wins.

Analogy:

- first check current room
- then outer room
- then house
- then public library

---

### 2.4 Memory Management

CPython mainly uses:

- reference counting
- cyclic garbage collection

#### Reference counting

If an object has no references left, it can be deallocated.

Example:

```python
a = [1, 2]
b = a
del a
del b
```

After the last reference disappears, the object can be freed.

#### Cyclic garbage collection

Reference counting alone fails for cycles.

Example:

```python
class Node:
    def __init__(self):
        self.other = None

a = Node()
b = Node()
a.other = b
b.other = a
```

If outside references disappear, the objects still reference each other.

That is why Python also has a cyclic garbage collector.

Cause-effect:

- no cycles: reference counting is often enough
- cycles: extra GC logic is needed

---

## 3. How It Works

### 3.1 What Happens During Assignment

Example:

```python
x = [1, 2, 3]
```

Internally:

1. create list object
2. bind name `x` to that object

Now:

```python
y = x
```

Internally:

1. no new list is created
2. `y` is bound to the same object as `x`

This explains aliasing bugs.

---

### 3.2 What Happens During Function Calls

Example:

```python
def f(items):
    items.append(10)
```

If you do:

```python
a = []
f(a)
print(a)  # [10]
```

Why did `a` change?

Because Python passes object references. The function received a reference to the same list object and mutated it.

Now compare:

```python
def g(items):
    items = [1, 2, 3]

a = []
g(a)
print(a)  # []
```

Why no change?

Because `items = [1, 2, 3]` rebinds the local name to a new object. It does not modify the original list.

---

### 3.3 Mutable vs Immutable Objects

Immutable built-ins:

- `int`
- `float`
- `bool`
- `str`
- `tuple`
- `frozenset`

Mutable built-ins:

- `list`
- `dict`
- `set`

Example:

```python
x = 10
old_id = id(x)
x += 1
new_id = id(x)
```

Usually `old_id != new_id` because integers are immutable, so a new object is created.

Example with mutation:

```python
lst = [1, 2]
old_id = id(lst)
lst.append(3)
new_id = id(lst)
```

Usually `old_id == new_id` because the same list object was mutated.

Simple rule:

- immutable objects are replaced
- mutable objects can change in place

---

### 3.4 `is` vs `==`

`==` checks value equality.

`is` checks identity.

Example:

```python
a = [1, 2]
b = [1, 2]

print(a == b)  # True
print(a is b)  # False
```

Best practice:

```python
if x is None:
    ...
```

Use `is` for `None`, not `==`.

---

### 3.5 Shallow Copy vs Deep Copy

Shallow copy:

- outer container is copied
- nested objects are still shared

Deep copy:

- nested objects are copied recursively

Example:

```python
import copy

a = [[1, 2], [3, 4]]
b = copy.copy(a)
c = copy.deepcopy(a)

a[0].append(99)
```

Now:

- `b` sees the inner mutation
- `c` does not

Cause-effect:

- shallow copy duplicates structure
- deep copy duplicates contents recursively

---

## 4. Important Internal Concepts

### 4.1 Dictionaries and Hashing

Python dictionaries are hash tables.

Lookup process:

1. compute hash of key
2. use hash to locate position
3. resolve collisions if needed
4. compare key if necessary
5. return value

Example:

```python
d = {"name": "Aman"}
print(d["name"])
```

Why dicts are fast:

- average lookup is `O(1)`

Why lists cannot be dict keys:

- list is mutable
- mutable objects cannot safely be hash keys

Valid keys:

- `int`
- `str`
- tuples of hashable elements

---

### 4.2 `__dict__` and `__slots__`

Most normal Python instances store attributes in `__dict__`.

Example:

```python
class User:
    pass

u = User()
u.name = "Aman"
print(u.__dict__)
```

`__slots__` declares fixed attributes and often reduces memory usage.

Example:

```python
class User:
    __slots__ = ("name", "age")
```

Tradeoff:

- less flexible
- often more memory efficient

Use case:

- many small objects

---

### 4.3 Iterables, Iterators, and Generators

Iterable:

- can be looped over

Iterator:

- produces values one at a time

Generator:

- special iterator produced by `yield`

Example:

```python
def gen():
    yield 1
    yield 2
```

Why generators matter:

- lazy evaluation
- lower memory usage
- useful for large streams

Analogy:

- list = all boxes delivered now
- generator = one box delivered when needed

---

### 4.4 Closures and Late Binding

A closure can remember names from an outer scope.

Example:

```python
funcs = []
for i in range(3):
    funcs.append(lambda: i)

print([f() for f in funcs])  # [2, 2, 2]
```

Why?

- closures capture the variable, not a frozen past value
- all lambdas look up the same final `i`

Fix:

```python
funcs = []
for i in range(3):
    funcs.append(lambda i=i: i)
```

---

### 4.5 Mutable Default Argument Trap

Example:

```python
def add_item(x, items=[]):
    items.append(x)
    return items
```

Why dangerous?

- default arguments are evaluated once when function is defined
- the same list is reused on later calls

Correct pattern:

```python
def add_item(x, items=None):
    if items is None:
        items = []
    items.append(x)
    return items
```

This is a direct consequence of Python's function-definition behavior.

---

### 4.6 Decorators

A decorator takes a function and returns a wrapped function.

Example:

```python
def log_calls(fn):
    def wrapper(*args, **kwargs):
        print("calling", fn.__name__)
        return fn(*args, **kwargs)
    return wrapper

@log_calls
def greet(name):
    return f"Hello {name}"
```

Why decorators work:

- functions are objects
- functions can be passed around
- closures preserve outer references

---

### 4.7 Imports and Module Loading

When Python imports a module:

1. check `sys.modules`
2. if already loaded, reuse it
3. otherwise load and execute it
4. cache the module object

Practical consequence:

- top-level module code usually runs once per process import lifecycle

---

### 4.8 Bytecode and `.pyc`

CPython can store bytecode in `__pycache__`.

Purpose:

- speed up imports

Important:

- `.pyc` is bytecode
- not machine code
- still executed by the Python Virtual Machine

---

### 4.9 The GIL

The Global Interpreter Lock in CPython allows only one thread to execute Python bytecode at a time.

This matters for concurrency:

- threads are often useful for I/O-bound work
- threads are not ideal for CPU-bound Python bytecode
- multiprocessing gives separate processes and can achieve parallel CPU execution

Quick summary:

- I/O-bound -> threads can help
- CPU-bound -> multiprocessing is often better
- async -> useful for high-concurrency I/O, not CPU parallelism

---

## 5. Relationships, Processes, and Cause-Effect

### 5.1 Why Mutation Bugs Happen

If two names point to the same mutable object, mutation through one name affects the other.

Example:

```python
a = {"x": []}
b = a
b["x"].append(1)
print(a)  # {'x': [1]}
```

Cause:

- shared reference
- in-place mutation

---

### 5.2 Why Python Dict Lookup Is Fast

Cause:

- hash computation gives direct access path
- avoids scanning all keys linearly

Effect:

- average `O(1)` lookup

Tradeoff:

- extra memory overhead
- keys must be hashable

---

### 5.3 Why Threads Behave Differently from Processes

Cause:

- GIL restricts simultaneous Python bytecode execution in one CPython process

Effect:

- threading is strong for I/O waiting
- multiprocessing is stronger for CPU-heavy pure Python work

---

### 5.4 Why Generators Save Memory

Cause:

- they yield one value at a time instead of building the full result eagerly

Effect:

- lower memory usage
- better for pipelines and streams

---

## 6. Why Questions

### Why Is Python Slower Than C/C++ in Many Cases?

Because Python does more work at runtime:

- dynamic typing
- object allocation overhead
- bytecode interpretation
- generic operations
- memory-management overhead

Python trades raw performance for expressiveness and productivity.

---

### Why Is `list.append()` Amortized `O(1)`?

Because Python lists over-allocate capacity.

Most appends use existing spare space.

Occasional resize is expensive, but average append remains constant time.

---

### Why Can Tuple Be a Dict Key but List Cannot?

Because:

- tuple is immutable
- list is mutable

Hash-table correctness depends on key stability.

---

### Why Does `a += b` Sometimes Mutate and Sometimes Rebind?

Because the behavior depends on the object's type:

- list may mutate in place
- int/str/tuple usually produce a new object

So the same syntax can trigger different underlying behavior.

---

## 7. What If Questions

### What If Python Only Used Reference Counting?

Then cyclic garbage would leak.

Objects that only reference each other would never reach zero reference count.

---

### What If Mutable Objects Were Allowed as Dict Keys?

Then their hash meaning could change after insertion.

That would break lookup correctness.

---

### What If Imports Were Not Cached?

Then importing the same module repeatedly would rerun module top-level code over and over.

That would be slower and more error-prone.

---

### What If Closures Captured Values Instead of Variables?

Then late-binding surprises would disappear, but Python's closure behavior would be fundamentally different.

---

### What If There Were No GIL in CPython?

CPU-bound threads could run Python bytecode in true parallel, but implementation complexity around memory safety, object management, and extensions would increase significantly.

---

## 8. Practical Applications

### Debugging Real Bugs

Internals helps explain:

- why a nested list changed unexpectedly
- why default mutable arguments keep old state
- why a closure returns the same value repeatedly

---

### Writing Memory-Efficient Code

Use internals knowledge to choose:

- generators for streams
- tuples for immutable records
- `__slots__` for many small objects
- shallow vs deep copy carefully

---

### Backend Performance Decisions

Internals helps decide:

- `dict` or `list` lookup strategy
- threads vs multiprocessing
- eager list creation vs lazy iteration

---

### Interview Problem Solving

Many interview questions depend directly on internals:

- hashability
- mutability
- aliasing
- generator behavior
- decorator behavior
- closure capture
- GIL tradeoffs

---

## 9. Comparison with Related Ideas

### Python Internals vs Python Syntax

Syntax is how you write code.

Internals is why the code behaves the way it does.

Example:

- syntax: `x += 1`
- internals: for immutable objects, that usually creates a new object and rebinds the name

---

### Python Internals vs Data Structures and Algorithms

DSA explains abstract behavior.

Python internals explains Python-specific runtime behavior.

Example:

- hash table = DSA concept
- `dict` implementation behavior = Python internals topic

---

### Python Internals vs System Design

System design focuses on architecture and scalability.

Python internals focuses on language runtime behavior.

They connect in practice when choosing:

- multiprocessing vs threading
- memory-efficient data handling
- request concurrency models

---

### CPython Internals vs Python Language Specification

This distinction matters.

- Python language spec = what Python guarantees
- CPython internals = how standard Python commonly implements it

Examples of CPython-specific discussion:

- GIL
- reference counting details
- object memory representation

---

## 10. Diagrams and Mental Models

### Variable Binding

```text
x ---> [1, 2, 3]
y ---> same list
```

Mutation changes the shared object.

---

### Function Call Frame

```text
call add(2, 3)

Frame
|- a = 2
|- b = 3
|- c = 5
```

---

### Execution Pipeline

```text
Source Code
   ->
AST
   ->
Bytecode
   ->
Python Virtual Machine
   ->
Runtime behavior
```

---

### Generator Model

```text
List:
build everything now

Generator:
produce one item
pause
resume later
```

---

## 11. Long-Term Retention Tips

### Learn in Layers

Memorize in this order:

1. objects and references
2. mutability
3. stack frames and scope
4. hashing and dictionaries
5. GC and memory model
6. generators, closures, decorators
7. GIL and concurrency

---

### Use Contrast Pairs

Retain these pairs:

- `is` vs `==`
- mutable vs immutable
- shallow copy vs deep copy
- iterable vs iterator
- threads vs processes
- syntax vs runtime behavior

---

### Predict Tiny Code Snippets

Practice by predicting output before running:

- aliasing examples
- mutable defaults
- closure capture
- `id()` before and after mutation/rebinding
- shallow copy behavior

---

### Keep One Master Summary

```text
Python code
-> parsed and compiled
-> bytecode
-> VM executes
-> objects are created
-> names bind to objects
-> memory managed by ref counting + cyclic GC
-> behavior shaped by mutability, scope, hashing, and runtime rules
```

---

## 12. Interview Answer Template

When asked a Python internals question, answer in this order:

1. Define the concept clearly.
2. Explain what Python does internally at a high level.
3. Give one short example.
4. State the practical consequence or tradeoff.

Example:

- "Python dicts are hash tables. Python hashes the key, finds the right location, and resolves collisions internally, which gives average `O(1)` lookup. The tradeoff is extra memory overhead and the requirement that keys be hashable."

---

## 13. Quick Revision Notes

- Everything in Python is an object.
- Variables are names bound to objects.
- CPython compiles source to bytecode and runs it on a virtual machine.
- CPython uses reference counting plus cyclic garbage collection.
- Mutable objects change in place; immutable objects are replaced.
- `is` checks identity, `==` checks value.
- Dicts are hash tables and require hashable keys.
- Default mutable arguments are evaluated once.
- Closures use late binding.
- Generators are lazy iterators.
- `__slots__` can reduce per-instance memory.
- GIL affects CPU-bound threading behavior in CPython.
