# JavaScript Internals

## What "JavaScript Internals" Means

JavaScript internals means understanding what the JavaScript engine is doing underneath your code.

At the surface level, you write things like:

- variables
- functions
- objects
- classes
- promises
- `async` / `await`
- events

At the internals level, the real questions are:

- How is JavaScript code executed?
- What are execution contexts?
- What is the call stack?
- How do scope and closures actually work?
- How are objects and prototype chains resolved?
- How does the event loop schedule work?
- What is the difference between heap and stack memory?
- How do promises, microtasks, and timers interact?
- How do engines optimize JavaScript at runtime?

So "JavaScript internals" is the runtime model of JavaScript.

---

## Why It Matters

Understanding JavaScript internals helps you:

- debug async bugs
- explain closures and scope clearly
- reason about performance
- avoid memory leaks
- understand `this`, prototypes, and inheritance
- write better frontend and backend JavaScript
- answer interview questions with cause-effect instead of memorized rules

If you only know syntax, JavaScript feels inconsistent.

If you understand internals, JavaScript starts to feel like a coherent runtime system.

---

## The Big Picture

A simple high-level model looks like this:

```text
JavaScript source code
        ->
Parser
        ->
AST
        ->
Bytecode / internal representation
        ->
Execution contexts + call stack
        ->
Heap objects + closures + prototype chains
        ->
Event loop + task queues for async work
```

In modern engines like V8, JavaScript is not just line-by-line interpreted in a simplistic way. Engines parse, compile, optimize, and execute code through multiple stages.

---

## 1. The Basics

### 1.1 JavaScript Is Single-Threaded at the Language Execution Level

The JavaScript engine executes one main piece of JavaScript code at a time on the call stack.

That means:

- one stack
- one currently executing frame
- one synchronous flow at a time

This does **not** mean JavaScript cannot do concurrency.

It means:

- synchronous JavaScript execution is single-threaded
- asynchronous behavior comes from the environment and event loop model

---

### 1.2 Memory Model: Stack vs Heap

A useful simplified model:

- stack stores execution frames
- heap stores objects, arrays, functions, closures, and other allocated data

Diagram:

```text
Call Stack:
- frame: main()
- frame: foo()
- frame: bar()

Heap:
- object {name: "Aman"}
- array [1, 2, 3]
- function object
- closure environment
```

Important note:

- the "stack vs heap" explanation is a simplified but very useful mental model
- engines are more complex than this, but this model is correct enough for interviews

---

### 1.3 Everything Important Runs Through Execution Contexts

JavaScript code executes inside execution contexts.

Main types:

- global execution context
- function execution context
- eval context

An execution context contains:

- scope information
- variable environment
- `this` binding
- reference to outer lexical environment

Think of an execution context as a "workspace" created whenever code starts executing.

---

## 2. Core Components

### 2.1 Execution Context

Every time code runs, JavaScript creates an execution context.

Example:

```javascript
function add(a, b) {
  const c = a + b;
  return c;
}

add(2, 3);
```

When `add(2, 3)` runs, a function execution context is created.

It stores:

- parameter bindings: `a`, `b`
- local bindings: `c`
- `this`
- link to outer scope

Diagram:

```text
Execution Context: add
- a = 2
- b = 3
- c = 5
- outer environment -> global
```

---

### 2.2 Call Stack

Execution contexts are pushed onto the call stack.

Example:

```javascript
function one() { two(); }
function two() { three(); }
function three() {}

one();
```

Stack progression:

```text
Global
Global -> one
Global -> one -> two
Global -> one -> two -> three
```

Then frames are popped in reverse order.

Cause-effect:

- deep recursion grows the stack
- too much recursion leads to stack overflow

---

### 2.3 Lexical Environment

A lexical environment is the structure that stores variable bindings and links to outer scopes.

JavaScript uses lexical scoping, which means scope is determined by where code is written, not where it is called.

Example:

```javascript
const x = 10;

function outer() {
  const y = 20;

  function inner() {
    const z = 30;
    console.log(x, y, z);
  }

  inner();
}
```

`inner()` can access:

- `z` from its own scope
- `y` from `outer`
- `x` from global scope

Diagram:

```text
inner -> outer -> global
```

This chain is the scope chain.

---

### 2.4 Scope Chain

When JavaScript looks up a variable:

1. it checks current scope
2. then outer lexical environment
3. then next outer one
4. eventually global

Example:

```javascript
const name = "global";

function test() {
  const name = "local";
  console.log(name);
}
```

Result:

- JavaScript finds `name` in local scope first
- it stops there

This lookup process explains shadowing.

---

### 2.5 Hoisting

Hoisting means declarations are processed before execution begins in a scope.

But not all declarations behave the same way.

#### `var`

Declared and initialized to `undefined` during setup.

```javascript
console.log(x); // undefined
var x = 5;
```

#### `let` and `const`

They are hoisted too, but remain in the temporal dead zone until initialized.

```javascript
console.log(x); // ReferenceError
let x = 5;
```

Cause-effect:

- `var` feels loosely available early
- `let` / `const` are safer because early access throws

---

### 2.6 Closures

A closure happens when a function remembers variables from its lexical environment even after the outer function has finished.

Example:

```javascript
function outer() {
  let count = 0;

  return function inner() {
    count++;
    return count;
  };
}

const fn = outer();
console.log(fn()); // 1
console.log(fn()); // 2
```

Why does `count` still exist?

Because the returned function closes over its lexical environment.

Analogy:

- a closure is like a backpack a function carries with remembered variables

---

### 2.7 `this` Binding

`this` in JavaScript is not based on where a function is written. It depends mostly on how the function is called.

Examples:

```javascript
const user = {
  name: "Aman",
  say() {
    console.log(this.name);
  }
};
```

Here `this` refers to `user` when called as `user.say()`.

But:

```javascript
const fn = user.say;
fn();
```

Now `this` is different.

Arrow functions are different:

- they do not create their own `this`
- they capture `this` lexically

This is a major internal rule that explains many bugs.

---

### 2.8 Objects and Property Lookup

JavaScript objects are collections of properties.

When you access:

```javascript
obj.name
```

the engine performs property lookup.

If the property is not on the object itself, JavaScript checks the prototype chain.

Diagram:

```text
obj
  ->
obj.__proto__
  ->
parent prototype
  ->
Object.prototype
  ->
null
```

This is one of the most important JavaScript internals.

Cause-effect:

- inherited methods work through prototype lookup
- property shadowing happens when an object defines a property that hides one from its prototype

---

### 2.9 Prototype Chain

JavaScript inheritance is prototype-based.

Example:

```javascript
const animal = {
  speak() {
    console.log("sound");
  }
};

const dog = Object.create(animal);
dog.bark = function () {
  console.log("woof");
};
```

`dog.speak()` works because `speak` is found on `animal` through the prototype chain.

Classes in JavaScript are syntax over this prototype system.

---

### 2.10 Garbage Collection

JavaScript engines automatically manage memory.

The simplified idea is:

- if an object is no longer reachable, it can be garbage collected

Reachability matters more than "reference count" in modern JS engines.

Common GC model used in explanation:

- mark-and-sweep

Basic idea:

1. start from roots like global objects and active stack references
2. mark everything reachable
3. remove what is unreachable

Cause-effect:

- closures can keep data alive
- event listeners can leak memory
- large detached objects can remain in memory if still referenced

---

## 3. How JavaScript Internals Work

### 3.1 Code Execution Flow

When JavaScript runs code:

1. parse source code
2. create execution context
3. create variable and function bindings
4. push context onto call stack
5. execute line by line
6. allocate objects/functions in memory as needed
7. pop context when done

This happens for:

- global code
- function calls
- module execution

---

### 3.2 Variable Lookup

If JavaScript sees:

```javascript
console.log(x);
```

it does not search memory randomly.

It walks the scope chain:

```text
current scope
  ->
outer scope
  ->
next outer scope
  ->
global scope
```

That is why nested functions can access outer variables and why shadowing works.

---

### 3.3 Property Lookup

If JavaScript sees:

```javascript
obj.toString();
```

it checks:

1. does `obj` itself have `toString`?
2. if not, check its prototype
3. then the next prototype
4. continue until found or `null`

This explains:

- why arrays have methods
- why plain objects inherit methods
- why prototype pollution is dangerous

---

### 3.4 Function Calls and Closures

Each function call creates a new execution context.

If the function returns another function, that inner function may keep access to outer variables through closures.

Cause-effect:

- outer function finishes
- closure still keeps needed environment alive
- those variables are not garbage collected yet

This is why closures are powerful and why they can also keep memory alive longer than expected.

---

## 4. Event Loop Internals

### 4.1 Why Async JavaScript Works

JavaScript itself executes synchronously on the call stack.

Asynchronous behavior comes from:

- browser APIs
- Node.js runtime APIs
- callback queues
- microtask queues
- event loop scheduling

So the right model is:

- JavaScript engine executes code
- host environment provides async APIs
- event loop schedules callbacks/promises back into execution

---

### 4.2 Call Stack, Web APIs, Queues

Browser-style mental model:

```text
Call Stack
Web APIs / Runtime APIs
Task Queue
Microtask Queue
Event Loop
```

Flow:

1. synchronous code runs on call stack
2. async API like `setTimeout` is handed to runtime
3. callback goes to task queue later
4. promises queue microtasks
5. event loop checks if stack is empty
6. microtasks run before next task

---

### 4.3 Task Queue vs Microtask Queue

Examples:

- task queue: `setTimeout`, DOM events, I/O callbacks
- microtask queue: `Promise.then`, `catch`, `finally`, `queueMicrotask`

Important rule:

- after current synchronous code finishes, JavaScript drains microtasks before taking the next task

Example:

```javascript
console.log("A");

setTimeout(() => console.log("B"), 0);

Promise.resolve().then(() => console.log("C"));

console.log("D");
```

Output:

```text
A
D
C
B
```

Why?

- `A` and `D` are synchronous
- promise callback is microtask
- timer callback is task

---

### 4.4 `async` / `await`

`async` / `await` is syntax built on top of promises.

It does not block the thread like synchronous waiting in many other languages.

Instead:

- the async function pauses logically
- execution resumes later through promise scheduling

So `await` is more like "split this function into continuation steps" than "freeze the thread."

---

## 5. Engine Optimizations

### 5.1 JIT Compilation

Modern engines like V8 use interpretation plus just-in-time optimization.

General idea:

- parse and run code quickly first
- observe runtime behavior
- optimize hot code paths

This is why JavaScript performance depends heavily on runtime patterns.

---

### 5.2 Hidden Classes / Shapes

JavaScript objects are dynamic, but engines optimize them using internal shapes or hidden classes.

If objects are created with consistent property layout, engines can optimize access better.

Example:

```javascript
function User(name, age) {
  this.name = name;
  this.age = age;
}
```

Objects built consistently are easier to optimize than objects mutated with random properties later.

Practical implication:

- stable object shapes can improve performance

---

### 5.3 Inline Caches

Engines remember past property access patterns and optimize repeated access.

Example:

```javascript
user.name
user.name
user.name
```

If access pattern stays predictable, the engine can speed it up.

Cause-effect:

- predictable structure helps optimization
- highly dynamic object behavior can reduce optimization opportunities

---

## 6. Why Questions

### Why Does `var` Behave Differently from `let`?

Because they are initialized differently during execution-context setup.

- `var` gets `undefined`
- `let` / `const` exist but are unavailable in the temporal dead zone until initialization

---

### Why Do Closures Work?

Because functions keep a reference to their lexical environment.

Without that preserved environment, returned inner functions could not access outer variables.

---

### Why Do Methods Sometimes Lose `this`?

Because `this` depends on call-site, not on where the function was originally defined.

So:

```javascript
obj.method()
```

and:

```javascript
const fn = obj.method;
fn();
```

do not behave the same way.

---

### Why Are Promises Executed Before `setTimeout(..., 0)`?

Because promise handlers are microtasks, and microtasks are drained before the event loop takes the next task.

---

### Why Can JavaScript Leak Memory Even with Garbage Collection?

Because garbage collection only frees unreachable objects.

If something is still reachable through:

- a closure
- a timer
- a global reference
- an event listener

it will remain alive.

---

## 7. What If Questions

### What If JavaScript Did Not Have Closures?

Then many common patterns would break:

- factory functions
- private state via closures
- callbacks with captured variables
- module patterns

Closures are a core part of JavaScript's design.

---

### What If Prototype Lookup Did Not Exist?

Then:

- inheritance would work very differently
- method reuse would be harder
- classes could not map naturally onto prototype-based behavior

JavaScript object reuse depends heavily on the prototype chain.

---

### What If Microtasks Did Not Exist?

Then promises would behave much less predictably and async sequencing would be harder to reason about.

Microtasks create consistent "run soon after current code" behavior.

---

### What If Objects Had Completely Random Shapes All the Time?

Then engines would have fewer optimization opportunities.

Your code would still work, but runtime performance could suffer.

---

### What If a Closure Keeps a Huge Object Alive?

Then that object stays in memory as long as the closure remains reachable.

This is a common source of accidental memory retention.

---

## 8. Practical Applications

### Debugging Async Bugs

Understanding:

- call stack
- microtasks
- tasks
- event loop

helps explain timing issues in:

- React apps
- Node.js APIs
- browser event handlers

---

### Writing Better Closures

Internals helps you reason about:

- private state
- stale closures
- memory retention
- callback behavior

This is especially useful in frontend frameworks.

---

### Avoiding Performance Problems

Understanding internals helps with:

- reducing unnecessary object churn
- keeping object shapes stable
- avoiding excessive sync work on the main thread
- reducing memory leaks

---

### Explaining Inheritance Clearly

Prototype chain knowledge helps you explain:

- how methods are shared
- why classes are syntax over prototypes
- why property shadowing happens

---

### Node.js and Browser Work

Internals are useful in:

- browser event handling
- API servers
- real-time apps
- UI rendering performance
- promise-heavy codebases

---

## 9. Comparison with Related Ideas

### JavaScript Internals vs JavaScript Syntax

Syntax is what you write.

Internals is what the engine does with it.

Example:

- syntax: `await fetchData()`
- internals: promise scheduling, continuation, microtask execution

---

### JavaScript Internals vs Browser Internals

They overlap, but they are not the same.

JavaScript internals:

- execution contexts
- scope
- call stack
- closures
- prototypes
- event loop interaction

Browser internals also include:

- DOM
- rendering
- layout
- paint
- browser networking

---

### JavaScript Internals vs Node.js Internals

Node.js uses JavaScript, but also adds runtime layers like:

- libuv
- I/O event handling
- process model
- module loading behavior

So JavaScript internals is the language/runtime model, while Node internals includes the host environment too.

---

### JavaScript Internals vs Python Internals

Both involve:

- execution model
- memory model
- scope
- object behavior

But JavaScript emphasizes:

- event loop
- prototype chain
- `this`
- microtasks

while Python emphasizes:

- reference counting
- descriptors
- GIL
- class model and method resolution

---

## 10. Diagrams and Mental Models

### Call Stack Model

```text
Global
  ->
foo()
  ->
bar()
  ->
baz()
```

Functions push frames onto the stack and pop them when done.

---

### Scope Chain Model

```text
inner scope
   ->
outer scope
   ->
global scope
```

Variable lookup walks this chain.

---

### Prototype Chain Model

```text
obj
  ->
prototype
  ->
parent prototype
  ->
Object.prototype
  ->
null
```

Property lookup walks this chain.

---

### Event Loop Model

```text
Call Stack
Microtask Queue
Task Queue
Event Loop
```

Rule:

- run sync code
- drain microtasks
- then process next task

---

## 11. Long-Term Retention Tips

### Learn in Layers

Memorize in this order:

1. execution context
2. call stack
3. lexical scope
4. closures
5. `this`
6. objects and prototype chain
7. event loop
8. promises and microtasks
9. garbage collection
10. engine optimization ideas

---

### Keep Three Master Diagrams

Retain:

1. call stack
2. scope chain
3. event loop

If those are clear, most JavaScript internals questions become easier.

---

### Use Contrast Pairs

Memorize these contrasts:

- `var` vs `let`
- stack vs heap
- function scope vs block scope
- value lookup vs property lookup
- task vs microtask
- regular function `this` vs arrow function `this`
- object own property vs prototype property

---

### Predict Tiny Snippets

The best way to retain JavaScript internals is to predict outputs before running code.

Practice:

- closure examples
- hoisting examples
- `this` examples
- promise vs timeout ordering
- prototype inheritance examples

---

## 12. Interview Answer Template

If asked, "Explain JavaScript internals", a strong short answer is:

- "JavaScript internals is the runtime model of the language: code runs inside execution contexts pushed onto the call stack, variables are resolved through lexical environments and the scope chain, objects use prototype-based inheritance for property lookup, memory lives on the heap with automatic garbage collection, and asynchronous behavior is coordinated through the event loop with task and microtask queues. Modern engines also optimize code dynamically using JIT techniques and object-shape optimizations."

---

## 13. Quick Revision Notes

- JavaScript execution is single-threaded on the call stack.
- Code runs inside execution contexts.
- Variable lookup follows the scope chain.
- Closures keep lexical environments alive.
- `this` depends on call-site for regular functions.
- Objects use the prototype chain for property lookup.
- Garbage collection is based on reachability.
- Async behavior uses the event loop.
- Promise handlers are microtasks.
- Microtasks run before the next task.
- Modern engines optimize JavaScript dynamically.
