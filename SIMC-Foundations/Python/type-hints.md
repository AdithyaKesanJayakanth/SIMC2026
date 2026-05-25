---
tags:
  - simc
---

# Python Type Hints

## What it is

Type hints (a.k.a. **annotations**, added in Python 3.5, [PEP 484](https://peps.python.org/pep-0484/)) let you write the **expected types** of function parameters and return values directly in the function signature. They are ==pure documentation== — Python does not enforce them at runtime.

```python
def simulate_die_rolls(n: int) -> np.ndarray:
    ...
```

Reads as: *"function `simulate_die_rolls` takes parameter `n`, which should be an `int`, and returns a `np.ndarray`."*

| Part | Meaning |
|------|---------|
| `n: int` | parameter `n` should be an `int` |
| `-> np.ndarray` | function returns a `np.ndarray` |
| `:` at end of `def` line | the regular Python colon that opens the function body (NOT a type hint) |

## Java analogy

You already know this pattern from CSA — Java requires types everywhere:

```java
public int[] simulateDieRolls(int n) { ... }
```

Same intent. The critical difference:

| | Java | Python |
|---|---|---|
| Required? | **Yes** | **No** — optional |
| Enforced at runtime? | **Yes** — won't compile | **No** — interpreter ignores them |
| Without types? | Won't compile | Works identically |

These two Python functions behave **exactly the same** at runtime:

```python
def simulate_die_rolls(n: int) -> np.ndarray:
    return np.random.randint(1, 7, size=n)

def simulate_die_rolls(n):
    return np.random.randint(1, 7, size=n)
```

> [!warning] Type hints are not checked at runtime
> ```python
> simulate_die_rolls("hello")   # Python does NOT complain here
> ```
> The interpreter happily passes `"hello"` in. The crash (if any) happens **inside** the function when something downstream chokes on a string. To catch type errors *before* running, use a separate tool like `mypy` or `pyright`.

## Why bother?

1. **Self-documenting code.** Future-you reading `def cluster(data, k)` has no idea what `data` is. `def cluster(data: np.ndarray, k: int) -> np.ndarray` is unambiguous.
2. **IDE autocomplete.** VS Code, PyCharm, etc. use type hints to suggest methods and catch typos in real time.
3. **Static checkers** (`mypy`, `pyright`) verify type correctness before you run, catching whole classes of bugs.
4. **Team work.** When Vishnu or Adithya read your SIMC code, they shouldn't have to step through the body to figure out what a function returns.

