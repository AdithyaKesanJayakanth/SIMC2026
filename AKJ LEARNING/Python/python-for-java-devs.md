---
tags:
  - simc
---

# Python for Java Developers

## Philosophy in one sentence

Java is statically typed, verbose, OO-by-default, compile-then-run — every variable has a declared type, every method lives inside a class, and the compiler catches type errors before the program runs. Python is dynamically typed, terse, multi-paradigm, interpreted — types are attached to values not variables, code runs top-to-bottom as the interpreter reads it, and you can write a useful program in three lines without a single class. The mental shift: ==stop declaring, start describing.== You're not telling the computer what kind of box to allocate; you're telling it what to do with the data.

## The syntax shock list

Quick-fire list of "things that LOOK different but mean the same":

| Java | Python | Notes |
|------|--------|-------|
| `;` at end of every statement | No semicolons | Line breaks end statements |
| `{ ... }` for blocks | Indentation (4 spaces) | ==Indentation IS the syntax== |
| `// comment` and `/* ... */` | `# comment` and `"""docstring"""` | Triple-quoted strings double as multiline comments |
| `int x = 5;` | `x = 5` | No type required, no semicolon |
| `System.out.println(x);` | `print(x)` | |
| `public static void main(...)` | `if __name__ == "__main__":` | Entry point pattern |
| `import java.util.*;` | `import math` or `from math import sqrt` | Module-based imports |
| `&&` `\|\|` `!` | `and` `or` `not` | Words, not symbols |
| `true` / `false` / `null` | `True` / `False` / `None` | Capitalized |
| `i++` | `i += 1` | ==No `++` or `--` in Python== |

> [!warning] Indentation is not cosmetic
> A misaligned line is a `IndentationError`. Pick 4 spaces (PEP 8 standard) and never mix tabs and spaces. Your editor should be set to "insert spaces for tab" when editing Python.

## Variables and types

No declaration needed. Type is inferred from the value. ==The same variable can hold different types at different times== (dynamic typing). Python has type hints (see [[type-hints]]) but they're documentation only — not enforced at runtime.

```java
int x = 5;
String name = "Alice";
double[] arr = {1.0, 2.0, 3.0};
boolean done = false;
```

```python
x = 5
name = "Alice"
arr = [1.0, 2.0, 3.0]
done = False

x = "now I'm a string"   # legal in Python, illegal in Java
```

> [!info] Everything is an object
> In Python, `int`, `float`, `bool`, even functions and classes are objects. `(5).bit_length()` works. There are no primitive types vs boxed types like Java's `int` vs `Integer`.

## Data structures

The big four, side by side:

| Concept | Java | Python | Notes |
|---------|------|--------|-------|
| Ordered, mutable collection | `ArrayList<Integer>` | `list` (`[1, 2, 3]`) | |
| Ordered, immutable collection | (none idiomatic) | `tuple` (`(1, 2, 3)`) | Python has both |
| Key-value map | `HashMap<String, Integer>` | `dict` (`{"a": 1}`) | |
| Unique values | `HashSet<Integer>` | `set` (`{1, 2, 3}`) | |
| Fixed-size, typed array | `int[]` | NumPy `np.ndarray` | Plain Python lists are dynamic and heterogeneous |

Creation and access for each:

```python
# list — like ArrayList, but more powerful
nums = [1, 2, 3, 4]
nums.append(5)
first = nums[0]
last = nums[-1]       # negative indexing! Java doesn't have this
slice = nums[1:3]     # [2, 3] — also no native Java equivalent
nums[1:3] = [20, 30]  # slice assignment, replaces in place

# tuple — immutable list
point = (3, 4)
x, y = point          # tuple unpacking — unpacks both values at once
a, b, c = 1, 2, 3     # works on the right side too

# dict — like HashMap
ages = {"alice": 30, "bob": 25}
ages["alice"]               # 30, KeyError if missing
ages.get("dave", 0)         # 0 if missing, no exception
ages["dave"] = 22           # add or overwrite
"alice" in ages             # True
for key, value in ages.items():
    print(key, value)

# set — like HashSet
unique = {1, 2, 3}
unique.add(4)
2 in unique                 # True
unique | {5, 6}             # union
unique & {2, 3, 9}          # intersection
```

> [!tip] `nums[-1]` is the last element
> Python supports negative indexing natively. `nums[-1]` is the last element, `nums[-2]` is second-to-last. ==Java has nothing like this.== Saves a ton of `nums.size() - 1` boilerplate.

> [!tip] Slicing is your new best friend
> `nums[start:stop:step]` returns a new list. All three are optional. `nums[:3]` = first three. `nums[-3:]` = last three. `nums[::-1]` = reversed copy. `nums[::2]` = every other element. ==This single feature replaces dozens of lines of Java loops.==

## Strings

```java
String greeting = "Hello, " + name + "! You are " + age + " years old.";
String f = String.format("Hello, %s! You are %d years old.", name, age);
```

```python
greeting = f"Hello, {name}! You are {age} years old."          # f-string (PREFER THIS)
greeting = "Hello, {}! You are {} years old.".format(name, age)  # older style
greeting = "Hello, " + name + "! You are " + str(age) + " years old."  # works but ugly
```

> [!tip] Always use f-strings
> ==Python's f-strings (the `f"..."` prefix)== are the modern way to interpolate. They support format specifiers too: `f"{pi:.4f}"` → `"3.1416"`, `f"{n:,}"` → `"1,000,000"`, `f"{x:>10}"` → right-pad to 10 chars. Equivalent to Java's `String.format` but inline and readable.

Common string operations:

```python
s = "Hello, World"
s.lower()              # "hello, world"
s.upper()              # "HELLO, WORLD"
s.split(", ")          # ["Hello", "World"]
", ".join(["a", "b"])  # "a, b"  — opposite of split
s.strip()              # remove leading/trailing whitespace
s.replace("World", "Python")
len(s)                 # 12  — len() works on everything
s[0]                   # "H"  — strings index like lists
s[-5:]                 # "World"  — strings slice like lists
"World" in s           # True
```

## Control flow

### if / elif / else

```java
if (x > 0) {
    System.out.println("positive");
} else if (x == 0) {
    System.out.println("zero");
} else {
    System.out.println("negative");
}
```

```python
if x > 0:
    print("positive")
elif x == 0:           # not "else if"
    print("zero")
else:
    print("negative")
```

> [!warning] `elif` not `else if`
> Easy one to trip on. Python uses `elif` as a single keyword. There is no `else if`.

Python also supports chained comparisons that read like math:

```python
if 0 < x < 100:        # equivalent to (x > 0 and x < 100)
    print("in range")
```

### for loops

The biggest mental shift: ==Python's `for` is always "for each"==, never "for i = 0; i < n; i++". To get an index counter, you ask for one explicitly.

```java
for (int i = 0; i < n; i++) {
    System.out.println(i);
}

for (int x : nums) {
    System.out.println(x);
}
```

```python
for i in range(n):            # 0, 1, 2, ..., n-1
    print(i)

for x in nums:                 # for-each, like Java
    print(x)

for i, x in enumerate(nums):   # if you need BOTH index and value
    print(i, x)

for a, b in zip(list1, list2): # iterate two lists in parallel
    print(a, b)
```

> [!tip] `enumerate` for index + value
> ==Java's `for (int i = 0; i < nums.size(); i++) { int x = nums.get(i); ... }`== becomes `for i, x in enumerate(nums):`. One line. Cleaner.

`range()` quick reference:

| Call | Yields |
|------|--------|
| `range(5)` | 0, 1, 2, 3, 4 |
| `range(2, 5)` | 2, 3, 4 |
| `range(0, 10, 2)` | 0, 2, 4, 6, 8 |
| `range(10, 0, -1)` | 10, 9, 8, ..., 1 |

### while loops

Nearly identical to Java. No do-while in Python.

```python
while x > 0:
    x -= 1

# Python's pattern for "do-while":
while True:
    do_something()
    if done:
        break
```

### break, continue

Same as Java. Python adds a curious `else` clause on loops that runs if the loop completes without hitting `break` — useful but rare, don't worry about it yet.

## Truthiness

In Java, `if` requires a boolean. In Python, every value has a truthiness — empty containers, 0, None, and empty strings are "falsy"; everything else is "truthy".

```java
if (list != null && !list.isEmpty()) { ... }
```

```python
if my_list:    # True if non-empty AND not None
    ...
```

> [!warning] Falsy values in Python
> `False`, `None`, `0`, `0.0`, `""`, `[]`, `{}`, `()`, `set()` are ALL falsy. ==Watch out: `if x:` does NOT mean "if x is not None" — it ALSO triggers on 0 and empty string.== Use `if x is not None:` when that matters (e.g., distinguishing "user passed 0" from "user passed nothing").

