# React Internals

## What "React Internals" Means

React internals means understanding what React is doing underneath your components.

At the surface level, you write things like:

- components
- props
- state
- hooks
- effects
- refs
- event handlers

At the internals level, the important questions are:

- What does React mean by "render"?
- Why does updating state not update the variable immediately?
- How does React know whether to preserve or reset state?
- Why do keys matter?
- When does React touch the DOM?
- Why do effects run after rendering?
- Why do stale closures happen?
- How does React decide what to update?

So "React internals" is the runtime model of how React turns state and props into UI updates.

---

## Why It Matters

Understanding React internals helps you:

- debug stale state and stale closure bugs
- reason about re-renders
- understand why keys reset state
- place logic in the right phase: render, event, effect, ref
- avoid accidental mutation
- write components that are easier for React to optimize

If you only know surface APIs, React can feel magical.

If you understand internals, React starts to feel like a predictable UI engine.

---

## The Big Picture

A good high-level model is:

```text
Props / state / context change
        ->
React schedules work
        ->
Render phase computes the next UI tree
        ->
React compares old and new trees
        ->
Commit phase applies changes
        ->
Refs are updated
        ->
Effects run
```

This is the core cycle behind most React behavior.

---

## 1. The Basics

### 1.1 React Is a UI Engine, Not Just a Templating Library

React is not just "return JSX and it appears on screen."

React manages:

- component tree structure
- state storage
- re-render scheduling
- tree comparison
- DOM commit updates
- ref attachment
- effect execution

JSX is just the syntax you write. The important part is the runtime model behind it.

---

### 1.2 Components Are Pure Calculations During Render

React expects components to behave like pure functions during render.

Meaning:

- same inputs -> same output
- no side effects during render
- do not mutate props, state, or external values used for rendering

Example:

```jsx
function Greeting({ name }) {
  return <h1>Hello {name}</h1>;
}
```

Why React cares:

- React may render more than once
- React may stop and retry rendering
- React needs render to be safe and predictable

This is one of the deepest React rules.

---

### 1.3 State Lives in React, Not Inside Your Function

This is one of the most important React ideas.

Example:

```jsx
function Counter() {
  const [count, setCount] = useState(0);
  return <button onClick={() => setCount(count + 1)}>{count}</button>;
}
```

It feels like `count` lives inside `Counter`, but conceptually React stores state outside the function and gives the component a snapshot during each render.

Mental model:

```text
React state shelf
   ->
render #1 gets count = 0
render #2 gets count = 1
render #3 gets count = 2
```

This explains why state behaves differently from normal mutable JavaScript variables.

---

## 2. Core Components of the Runtime Model

### 2.1 Render Tree

React builds a tree of your UI.

Example:

```jsx
function App() {
  return (
    <div>
      <Header />
      <Profile />
    </div>
  );
}
```

Conceptual tree:

```text
App
 ->
div
 |- Header
 |- Profile
```

React associates state with positions in this tree.

That is why tree position matters so much.

---

### 2.2 Render Phase

Render phase means React calls your components to figure out what the next UI should look like.

React is basically asking:

- "If I call these components with current props, state, and context, what UI tree should I get?"

Important:

- render phase computes
- render phase does not yet mutate the DOM

This is why reading refs or doing DOM work in render is wrong.

---

### 2.3 Commit Phase

After rendering, React commits changes.

Commit phase is where React:

- applies DOM updates
- attaches refs
- finalizes what the screen should show

Simple model:

```text
Render = calculate
Commit = apply
```

This is the cleanest way to remember it.

---

### 2.4 State Snapshot

Each render sees a fixed snapshot of state.

Example:

```jsx
function Counter() {
  const [number, setNumber] = useState(0);

  return (
    <button onClick={() => {
      setNumber(number + 1);
      setNumber(number + 1);
      setNumber(number + 1);
    }}>
      +3
    </button>
  );
}
```

Why does this not add 3?

Because inside that render's event handler, `number` is the same snapshot value for all three calls.

React does not mutate `number` in place.

Cause-effect:

- render gives you one snapshot
- event handler closes over that snapshot
- updates are queued
- next render receives the updated result

---

### 2.5 Update Queue and Batching

React queues state updates and processes them after the event handler finishes.

This is batching.

Analogy:

- React is like a waiter taking the whole order before walking to the kitchen

Example:

```jsx
setNumber(n => n + 1);
setNumber(n => n + 1);
setNumber(n => n + 1);
```

This works because updater functions are applied in sequence during the next render.

Cause-effect:

- direct value form uses the old snapshot
- updater function form uses the queued previous result

---

### 2.6 Props, State, and Context

React uses three main input channels for rendering:

- props
- state
- context

Your component output should be a pure result of these inputs.

If any of them change, React may render again.

This is why React components are often described as UI formulas.

---

### 2.7 Keys and Identity

Keys are not just for list warnings.

Keys help React identify which component instance should be considered the "same" across renders.

Example:

```jsx
{isA ? <Counter key="A" /> : <Counter key="B" />}
```

Because the keys differ, React treats them as different component identities.

Effect:

- state is reset when identity changes

Without different keys, React may preserve state if the component stays in the same tree position.

---

### 2.8 Refs

Refs are escape hatches for imperative access.

Common use:

- access a DOM node
- store mutable values that should not trigger re-renders

Important timing rule:

- refs are set during commit, not during render

That is why `ref.current` is usually read in:

- event handlers
- effects

not during render.

---

### 2.9 Effects

Effects run after render and commit.

They exist because some work is not part of pure rendering:

- subscriptions
- timers
- fetching
- logging
- syncing to external systems

Think of effects as synchronization logic between React state and the outside world.

They are not for "any code after render." They are specifically for side effects.

---

## 3. How React Internals Work

### 3.1 Trigger -> Render -> Commit

Any visible screen update follows the same broad cycle:

1. something triggers work
2. React renders components
3. React commits changes

Typical triggers:

- initial mount
- state update
- parent re-render
- context change

Diagram:

```text
Trigger
  ->
Render
  ->
Commit
  ->
Browser paint
```

This is the backbone of React.

---

### 3.2 What Happens When State Updates

Example:

```jsx
setCount(count + 1);
```

What actually happens:

1. React queues an update
2. React schedules a re-render
3. during the next render, React computes the new UI
4. during commit, React updates the DOM if needed

Important:

- calling `setState` does not mutate the current render's variable
- it requests a future render

This explains many beginner and intermediate bugs.

---

### 3.3 Why State Is Tied to Tree Position

React preserves state based on where a component sits in the render tree.

Example:

```jsx
function App({ show }) {
  return (
    <div>
      {show ? <Counter /> : null}
    </div>
  );
}
```

If `Counter` disappears, its state is discarded.

If it appears again, React creates fresh state.

Key idea:

- state is tied to component identity at a specific position in the tree

This is why keys matter and why nested component definitions can accidentally reset state.

---

### 3.4 Why React Preserves Some DOM and Replaces Other DOM

React compares the previous rendered tree and the next rendered tree.

If something is the "same enough":

- React preserves it

If identity changes:

- React may replace that subtree

This affects:

- state preservation
- DOM reuse
- ref behavior
- input preservation

Example:

```jsx
<Clock time={time} />
```

If only `time` changes, React updates what changed rather than rebuilding everything.

---

### 3.5 Event Handlers and Stale Closures

Every render creates fresh functions and event handlers.

Those handlers capture the state values of that render.

That is why stale closures happen.

Example:

```jsx
function Example() {
  const [count, setCount] = useState(0);

  function handleLater() {
    setTimeout(() => {
      console.log(count);
    }, 1000);
  }
}
```

The timeout callback prints the `count` from the render where `handleLater` was created.

Cause-effect:

- render creates handler
- handler captures snapshot
- later async work still sees old snapshot

This is one of the most important React-plus-JavaScript interactions.

---

## 4. Relationships, Processes, and Cause-Effect

### 4.1 Why Purity Matters

If components are pure during render, React can:

- render more than once safely
- restart rendering safely
- optimize rendering behavior
- keep behavior predictable

If render had uncontrolled side effects, React would become unreliable.

So purity is not style preference. It is an architectural requirement.

---

### 4.2 Why Effects Run After Commit

Effects interact with the outside world.

React waits until the UI is committed so those effects can work against the real committed state.

Cause-effect:

- render computes desired UI
- commit applies it
- effect runs afterward to sync external systems

This is why DOM measurement or subscriptions belong in effects, not render.

---

### 4.3 Why Keys Reset State

React uses tree position plus identity to decide whether state should persist.

If you change the key:

- React treats it as a different component instance
- old state is discarded
- new state is created

This is useful and dangerous.

Useful for:

- resetting forms
- switching profiles/chats cleanly

Dangerous when:

- unstable keys accidentally cause unnecessary remounts

---

### 4.4 Why Re-renders Don’t Always Mean DOM Changes

A re-render means React recalculated the next UI.

It does **not** necessarily mean React changed the DOM.

Cause:

- render computes
- commit only applies actual differences

This is why "a component re-rendered" is not the same as "the DOM was rebuilt."

---

## 5. Simple Examples

### Basic render cycle

```jsx
function Counter() {
  const [count, setCount] = useState(0);
  return <button onClick={() => setCount(count + 1)}>{count}</button>;
}
```

What happens:

- click triggers update
- React queues update
- component re-renders
- DOM text changes in commit

---

### State snapshot example

```jsx
setCount(count + 1);
setCount(count + 1);
```

Both use the same `count` snapshot from that render.

---

### Correct queued update example

```jsx
setCount(c => c + 1);
setCount(c => c + 1);
```

Each updater uses the latest queued value.

---

### Key-based reset example

```jsx
<Chat key={user.id} user={user} />
```

Changing `user.id` forces React to create a fresh component identity.

---

### Ref timing example

```jsx
const ref = useRef(null);

useEffect(() => {
  ref.current?.focus();
}, []);
```

Works because refs are attached by commit time.

---

## 6. Why Questions

### Why Does React Say State Is a Snapshot?

Because each render gets a fixed view of state values.

That render cannot see future updates instantly.

---

### Why Do Event Handlers See Old Values Sometimes?

Because they close over the render in which they were created.

This is not React being random. It is a direct result of React renders plus JavaScript closures.

---

### Why Are Components Supposed to Be Pure?

Because React may call them multiple times and expects rendering to be safe, repeatable, and free from side effects.

---

### Why Do Keys Matter So Much?

Because keys participate in identity, and identity controls state preservation and subtree reuse.

---

### Why Doesn’t `setState` Change the Value Immediately?

Because `setState` queues work for a future render instead of mutating the current render's snapshot.

---

## 7. What If Questions

### What If I Define a Component Inside Another Component?

Then a new component function can be created every render.

Effect:

- React may treat it as a different component
- state can reset unexpectedly

That is why top-level component definitions are safer.

---

### What If I Mutate State Directly?

Example:

```jsx
state.user.name = "Aman";
```

Then React may not get the clean state transition model it expects.

Effect:

- bugs
- stale UI
- harder debugging

React expects state updates to go through state setters with immutable-style replacement.

---

### What If I Use Array Index as a Key?

It can work for static lists.

But if list ordering changes:

- component identity can shift incorrectly
- state can move to the wrong item

This is why stable data identity is preferred for keys.

---

### What If I Do Side Effects During Render?

Then React behavior becomes unreliable because render may happen multiple times or be restarted.

Side effects belong in:

- event handlers
- effects

not render.

---

### What If I Read `ref.current` During Render?

It may be `null` or not yet reflect the committed DOM.

Render is too early for imperative DOM assumptions.

---

## 8. Practical Applications

### Debugging Form Reset Bugs

Understanding tree position and keys helps explain why inputs sometimes preserve value and sometimes reset.

---

### Fixing Stale Closure Problems

React internals helps with:

- timers
- async handlers
- subscriptions
- old state in callbacks

This is common in real apps.

---

### Performance Tuning

Understanding render vs commit helps you reason about:

- unnecessary re-renders
- expensive child trees
- identity stability
- memoization decisions

---

### Correct Effect Placement

React internals helps decide whether logic belongs in:

- render
- event handler
- effect
- ref

This is one of the biggest practical differences between beginner and advanced React code.

---

### Building Reliable Dynamic UIs

Internals helps with:

- tabs
- chat windows
- dashboards
- modal flows
- routed screens
- list-heavy components

because all of these depend on state preservation and identity.

---

## 9. Comparison with Related Ideas

### React Internals vs JavaScript Internals

JavaScript internals explains:

- closures
- event loop
- prototype chain
- call stack

React internals builds on top of that and adds:

- render/commit phases
- state snapshots
- tree identity
- effect timing
- component purity

React bugs often come from mixing these two mental models incorrectly.

---

### React Render vs Browser Render

React render means:

- React calls your components to compute the next UI

Browser render usually means:

- layout
- paint
- compositing

These are not the same thing.

This distinction prevents lots of confusion.

---

### React State vs Normal Variables

Normal JavaScript variable:

- you can mutate it directly

React state:

- managed by React
- tied to component identity and render position
- updated through queued renders

---

### Effect vs Event Handler

Event handler:

- runs because the user or code triggered an event

Effect:

- runs because rendering committed and React needs to sync external systems

This is a very important architectural distinction.

---

## 10. Diagrams and Mental Models

### Core Render Model

```text
State/props/context change
   ->
Render phase computes next tree
   ->
Commit phase applies real changes
   ->
Effects run
```

---

### State Identity Model

```text
state is tied to:
component type + position in render tree + key
```

Change one of those and state may reset.

---

### Closure Model

```text
render #1 creates handler with count = 0
render #2 creates handler with count = 1
```

Each render has its own captured values.

---

## 11. Long-Term Retention Tips

### Learn These in Order

Memorize React internals in this sequence:

1. render vs commit
2. state snapshot
3. queued updates and batching
4. tree position and keys
5. refs
6. effects
7. stale closures

If those are solid, most React behavior becomes easier to predict.

---

### Use One Anchor Sentence

Use this:

- "React computes UI in render, applies it in commit, preserves state by tree identity, and runs effects afterward."

That sentence captures a lot.

---

### Keep Three Master Diagrams

Retain:

1. trigger -> render -> commit
2. state tied to tree position
3. stale closure across renders

These three explain most React bugs.

---

### Practice Prediction

Before running code, predict:

- whether state is preserved
- whether a closure is stale
- whether an effect runs now or after commit
- whether a key change causes reset

This is the best way to make React internals stick.

---

## 12. Interview Answer Template

If asked, "Explain React internals", a strong short answer is:

- "React works by treating components as pure render functions over props, state, and context. A state update queues work for a future render rather than mutating the current render's values. During render, React computes the next component tree. During commit, React applies actual DOM changes, updates refs, and then runs effects. React preserves state based on component identity in the render tree, which is why position and keys matter so much. Many React bugs come from misunderstanding this model, especially state snapshots, stale closures, and effect timing."

---

## 13. Quick Revision Notes

- Render means compute, not mutate DOM.
- Commit means apply changes.
- State lives in React, not inside the component function.
- Each render sees a snapshot of state.
- State updates are queued and batched.
- Event handlers capture the render they were created in.
- State is tied to tree position and key-based identity.
- Refs are attached during commit.
- Effects run after commit.
- Components should stay pure during render.
