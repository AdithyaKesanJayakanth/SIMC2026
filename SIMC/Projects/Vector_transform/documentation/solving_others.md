# Recovering Someone Else's Base Truth

How to reverse-engineer the hidden `BASE_TRUTH` vector from a teammate's published CSV, given only their repo.

## The Setup

Every teammate's challenge follows the same shape:

- A fixed hidden vector `base` (their `BASE_TRUTH`)
- A fixed displacement vector `p`
- A scalar `k` drawn per row from a small set `K_CHOICES`
- Each row of the CSV is `base + k * p`

The CSV is published; `base`, `p`, and the per-row `k` are not.

## What Recovery Requires

From the CSV alone, you can always recover:

- The **direction of `p`** (up to sign and scale), from differences between unique rows
- The **number of distinct `k` values**, from the count of unique rows
- The **line** the base lives on (any unique row, plus the direction)

What the CSV **cannot** tell you alone:

- Which point on the line is `base` — any unique row is a valid candidate for "base at `k = ?`", and the shift is ambiguous until you pin down the k→row mapping

So recovery comes down to: **find any extra constraint the author exposed that fixes the k→row mapping**.

## The Three Constraints That Usually Break Ambiguity

Check the teammate's repo for any of these, in order of usefulness:

1. **Formula is disclosed** (`docs/`, `README.md`, comments) — if `p` is written out explicitly (e.g. `p = [0,1,2,3,4,5]`), you know its exact scale, not just direction. Then `k` for each row is `(row - candidate_base) · p / (p · p)` and must be an integer.
2. **`K_CHOICES` is disclosed and contains 0** — then one unique row literally *is* the base. Identify it as the row whose neighbors (sorted along `p`) are one `p`-step away on each side.
3. **Code is committed with `BASE_TRUTH` or `INITIAL_VECTOR` hardcoded** — sometimes teammates forget to gitignore it, or leave a placeholder. Always check the source file before doing any math. **Caveat**: a hardcoded value may be a placeholder — verify it actually reproduces the CSV before trusting it.

If none of the above apply, you're stuck with a line of candidates and need a prior (small integers? nonneg? matches teammate's style from other work?).

## Recovery Procedure

1. **Clone the repo** into `Code/<Teammate>_vector_transform/`
2. **Read every file** — `README`, `docs/`, source code, config, gitignore. Note:
   - The transform formula (is `p` explicit?)
   - The `K_CHOICES` set (documented? does it contain 0?)
   - Any hardcoded vectors in source
   - Whether their committed code actually runs (syntax errors, missing files)
3. **Load the CSV**, strip any non-vector columns (iteration index, etc.), find unique rows
4. **Sort unique rows along `p`** — this gives them in k-order (ascending or descending)
5. **Verify spacing**: consecutive sorted rows should differ by exactly `p` (if `p` is known) or by a constant vector (if only direction is known — that vector *is* `p`)
6. **Pin `base`**:
   - If `K_CHOICES` contains 0: the row at that position (matching their k=0 convention) is `base`
   - Else: subtract `k*p` from each unique row for each candidate `k` assignment; the candidate where all rows collapse to the same vector is correct
7. **Sanity check**: for every row in the full CSV, `(row - base)` should be an integer multiple of `p`, and that multiple should be in `K_CHOICES`

## Case Study: Adithya (`AdithyaAnand24/SIMC-vector-transform`)

Fully disclosed everything needed:

- `docs/DOCUMENTATION.md` states the formula `v'_i = v_i + k * i` → `p = [0, 1, 2, 3, 4, 5]` exactly
- Same doc states `K_CHOICES = {-2, -1, 0, 1, 2}` → contains 0

### Unique rows (sorted by position along `p`)

| k  | CSV row               |
|----|-----------------------|
| -2 | `[1, -2,  5,  2, -2, -7]` |
| -1 | `[1, -1,  7,  5,  2, -2]` |
|  0 | `[1,  0,  9,  8,  6,  3]` |
|  1 | `[1,  1, 11, 11, 10,  8]` |
|  2 | `[1,  2, 13, 14, 14, 13]` |

Consecutive differences are all `[0, 1, 2, 3, 4, 5]` — confirms `p` exactly and confirms the sort order matches the k-ordering.

### Result

**`BASE_TRUTH = [1, 0, 9, 8, 6, 3]`** — the row where k=0.

Verified: subtracting `k * [0,1,2,3,4,5]` from every unique row produces `[1, 0, 9, 8, 6, 3]` for all five rows.

### Incidental findings

- `src/vector_transform.py` has a syntax error (malformed `def transform(k):`, `transformed_vector` undefined). The committed code would not run; the CSV was generated with a different/earlier version.
- `INITIAL_VECTOR = [1, 2, 3, 4, 5, 6]` in source is a placeholder — does not match the recovered base.
- `src/config.py` referenced in README does not exist in the repo.

## Common Failure Modes

- **Non-integer `p`** — differences won't look clean. Divide by the gcd of absolute values to normalize.
- **Noise added to rows** — unique row count will not match `|K_CHOICES|`; cluster first, then take cluster centroids as the "unique" rows.
- **Different seed / sampling logic** — doesn't affect recovery from the CSV (k distribution is still over `K_CHOICES`), only matters if you're trying to replay their generator.
- **CSV has extra columns** — iteration index, timestamp, k itself (yes, some people leak it). Drop non-vector columns before finding unique rows.
