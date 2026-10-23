Y3 S1 — Programming & Systems Foundations *(Nov 2026 → Apr 2027 exams · 15 credits)*

| Module | Credits · type | Feeds the arc |
| --- | --- | --- |
| CCS3300 Software Architecture | 3 · core | Layered design: input / device / logic / diagnostics |
| CCS3310 Software Engineering Methods | 3 · core | Requirements and acceptance criteria |
| CCS3311 Software Quality Assurance | 3 · core | Test design, boundary cases, test reports |
| CCS2360 Technology Challenge Competition | 3 · core | Small sensor/device prototype pitch |
| CCS3356 Natural Language Processing | 3 · elective | Complete the syllabus only |

**Plan:** Oct 23–31 is pre-semester setup. Nov–Dec: B–L in dependency order, with Linux and Git alongside Python. Jan–Feb: M and N; finish Project 1. March: O and C weeks 1–6 (P). April: examinations and review only. May bridge: C weeks 7–12 from Y3 S2 A; carry unfinished work into June. Block week numbers are study sequences, not university calendar weeks.

---

## A. Setup — week 1 (~4 h) **[M]**

- [x]  Install the latest stable Python (3.12–3.14); run `python --version`
- [x]  Install VS Code and the Python extension
- [x]  Set up a Linux shell: WSL2 Ubuntu (or native Ubuntu LTS)
- [x]  Inside Linux, run `gcc --version` and `git --version`; install with `apt` if missing
- [x]  Run `git config --global user.name` and `user.email`
- [x]  Generate an SSH key (`ssh-keygen -t ed25519`) and add the public key to GitHub
- [x]  Create folders `day04_strings/` … one per day as you go; add a one-line `README.md`
- [x]  Clone the 30 Days of Python repo (read-only reference); keep your own solutions in your own repo
- [x]  Make your first commit and push

## B. Gap check, Days 01–04 — week 1 (~3 h) **[M]**

- [ ]  Day 01–03: write a script that uses `int`, `float`, `str`, `bool`, `list`, converts types, and prints with an f-string
- [ ]  Use `len`, `range`, `type`, `input`, `print(sep=, end=)`
- [ ]  Write 5 expressions mixing `+ - * / // % **` and comparison/Boolean operators; predict results before running
- [ ]  Day 04 strings: index and slice a string, including `[::-1]`
- [ ]  Use `upper`, `lower`, `strip`, `split`, `join`, `replace`, `find`, `startswith`, `endswith`, `isdigit`
- [ ]  Format with f-strings, including width/precision (`f"{x:.2f}"`)
- [ ]  Parse `"SN123,Hub-A,OK"` into three variables with `split(",")`
- [ ]  Any step above fails? Redo that day's chapter exercises, then continue
- [ ]  **Proof:** solve 3 Day 04 exercises without notes

## C. Day 05 — Lists (current) — weeks 1–2 (~6 h) **[M]**

- [ ]  Read the full Day 05 chapter; type and run every example in a REPL
- [ ]  Create lists with `[]` and `list(...)`; check `type()` and `len()`
- [ ]  Index with positive and negative indexes; trigger an `IndexError` on purpose
- [ ]  Slice with `[start:stop:step]`; reverse with `[::-1]`
- [ ]  Modify with item assignment, `append`, `extend`, `insert`
- [ ]  Remove with `pop()`, `pop(i)`, `remove(x)`, `del`, `clear()`; note which ones raise errors
- [ ]  Show aliasing: `b = a` then change `b`; compare with `a.copy()` and `a[:]`
- [ ]  Show a nested list where shallow copy still shares inner lists; fix with `copy.deepcopy`
- [ ]  Sort with `sort()` vs `sorted()`; reverse with `reverse()` vs `reversed()`; use `key=` and `reverse=True`
- [ ]  Search with `in`, `not in`, `count`, `index`
- [ ]  Loop with `for`, `enumerate`, and `zip` over two lists
- [ ]  Concatenate with `+`, repeat with ; convert between string and list with `split`/`join`
- [ ]  Solve all Day 05 exercises without looking at solutions
- [ ]  Mini-exercise: list of 10 sensor readings → min, max, average, sorted copy, remove readings above a threshold, count readings below a threshold
- [ ]  **Proof:** explain mutability and the copy pitfalls aloud in 2 minutes

## D. Day 06 — Tuples — week 3 (~2 h) **[M]**

- [ ]  Read the chapter; run every example
- [ ]  Create a tuple, a one-item tuple `(1,)`, and an empty tuple
- [ ]  Index and slice a tuple
- [ ]  Try item assignment; read the `TypeError`
- [ ]  Pack and unpack: `a, b = (1, 2)`; swap with `a, b = b, a`
- [ ]  Star-unpack: `first, *rest = (1, 2, 3, 4)`
- [ ]  Return two values from a function (tuple) and unpack the result
- [ ]  Use a tuple as a dict key (`("Hub-A", "OK")`)
- [ ]  Convert between list and tuple; sort a list of tuples
- [ ]  Solve all Day 06 exercises
- [ ]  **Proof:** write 3 sentences on when to use a tuple instead of a list

## E. Day 07 — Sets — week 3 (~3 h) **[M]**

- [ ]  Read the chapter; run every example
- [ ]  Create sets with `{}` and `set(...)`; note that `{}` alone is a dict
- [ ]  `add`, `update`, `remove` vs `discard` (compare errors)
- [ ]  Remove duplicates from a list with `set`; restore order with `sorted`
- [ ]  `union`, `intersection`, `difference`, `symmetric_difference` (method and operator forms)
- [ ]  `issubset`, `issuperset`, `isdisjoint`
- [ ]  Time `x in big_list` vs `x in big_set` with `timeit`; write down the result
- [ ]  Solve all Day 07 exercises
- [ ]  **Proof:** given two lists of scanner serials, print serials in A only, B only, both

## F. Day 08 — Dictionaries — weeks 3–4 (~6 h) **[M]**

- [ ]  Read the chapter; run every example
- [ ]  Create dicts with `{}` and `dict(...)`
- [ ]  Access with `d[key]` (trigger a `KeyError`) and `d.get(key, default)`
- [ ]  Add and change items; `update`; `setdefault`
- [ ]  Remove with `pop`, `del`, `popitem`, `clear`
- [ ]  Loop over `keys()`, `values()`, `items()`
- [ ]  Check key membership with `in`
- [ ]  Copy with `dict.copy()`; show shallow-copy sharing with nested dicts
- [ ]  Build a nested structure: `{"SN123": {"model": "X1", "branch": "Hub-A", "status": "OK"}}`
- [ ]  Count items by status using a dict
- [ ]  Validate a record: required keys present, status in an allowed set, serial not empty; print every error
- [ ]  Solve all Day 08 exercises
- [ ]  **Proof:** build a serial → record index and look up 3 serials, one of them missing, without a crash

## G. Days 09–10 — Conditionals and Loops — week 5 (~4 h) **[M]**

- [ ]  Day 09: write `if/elif/else` chains; use `and`, `or`, `not`
- [ ]  Test truthiness: `0`, `""`, `[]`, `None`, `{}`
- [ ]  Use a conditional expression: `x = a if cond else b`
- [ ]  Validate user input: reject empty, non-numeric, out-of-range
- [ ]  Day 10: `for` over list, dict items, string; `while` with a counter
- [ ]  Use `break`, `continue`, and `for … else`
- [ ]  Write a nested loop that compares every pair in a list
- [ ]  Show why you must not remove items from a list while looping over it; fix by looping over a copy
- [ ]  Solve 5 exercises each from Days 09 and 10
- [ ]  **Proof:** FizzBuzz and a prime-number checker without notes

## H. Checkpoint A — Scanner Inventory & Status Filter — weeks 5–6 (~6 h) **[M]**

- [ ]  Write a 5-line spec: inputs, outputs, allowed statuses
- [ ]  Record fields: serial, model, branch, status, last_seen
- [ ]  Store records in a list of dicts; keep a dict index by serial; keep a set of allowed statuses; keep a tuple `(branch, status)` for grouping
- [ ]  Menu loop (`while`): add, list, filter by status, remove, summary, quit
- [ ]  Reject duplicate serials using the dict index
- [ ]  Reject statuses not in the allowed set
- [ ]  Filter by status with a loop (refactor later)
- [ ]  Summary: count per status using a dict
- [ ]  Write 4 sentences in the README: why list, tuple, set, dict were chosen
- [ ]  Commit with a message like `Add scanner inventory checkpoint A`
- [ ]  **Proof:** solve 3 collection exercises you have never seen, without copying a solution

## I. Days 11–14 — Functions, Modules, Comprehensions, Higher-order — weeks 7–8 (~12 h) **[M]**

- [ ]  Day 11: define and call functions; parameters vs arguments
- [ ]  Default parameters; keyword arguments; `args`; `*kwargs`
- [ ]  Return multiple values; unpack them
- [ ]  Local vs global scope; show why mutating globals is risky
- [ ]  Write docstrings
- [ ]  Write a recursive function (factorial) and its base case
- [ ]  Solve Day 11 exercises
- [ ]  Refactor Checkpoint A into small functions (`add_scanner`, `validate_record`, `summarize`)
- [ ]  Day 12: `import`, `from … import`, `as`; use `math`, `random`, `os`, `sys`
- [ ]  Create your own module; import it from another file
- [ ]  Use `if __name__ == "__main__":`
- [ ]  Split Checkpoint A into `inventory.py`, `validators.py`, `main.py`
- [ ]  Day 13: list comprehension; with condition; nested
- [ ]  Set and dict comprehensions
- [ ]  Rewrite two loops in Checkpoint A as comprehensions; keep the loop if it needs more than 2 clauses
- [ ]  Day 14: `lambda`; `map`; `filter`; `sorted(key=...)`
- [ ]  Sort scanners by `last_seen` using `key=`
- [ ]  Solve exercises for Days 12–14
- [ ]  **Proof:** rewrite one `for` loop three ways (loop, comprehension, `map`) and say which you prefer and why

## J. Linux shell — see semester calendar above (~5 h) **[M]**

- [ ]  Navigate: `pwd`, `ls -la`, `cd`
- [ ]  Manage files: `mkdir`, `touch`, `cp`, `mv`, `rm`
- [ ]  View files: `cat`, `less`, `head`, `tail`, `tail -f`
- [ ]  Search: `grep -rn`, `find -name`
- [ ]  Read `ls -l` permissions (rwx); change with `chmod 644` and `chmod +x`
- [ ]  Pipes and redirects: `|`, `>`, `>>`, `2>`, `2>&1`
- [ ]  Environment variables: `export`, `echo $VAR`, add one to `~/.bashrc`
- [ ]  Exit codes: run a command, then `echo $?`; use `&&` and `||`
- [ ]  Processes: `ps aux`, `top` or `htop`, `kill`, `Ctrl+C`; run in background with `&`; `jobs`
- [ ]  Read a `man` page (`man grep`) and find one option you didn't know
- [ ]  Write a shell script with `#!/bin/bash`, `set -e`, one argument, one `if`
- [ ]  **Proof:** count how many log lines in a file contain `ERROR`, using one pipeline

## K. Days 15–21, 23, 28 — Python core — see semester calendar above (~25 h) **[M]**

- [ ]  Day 15: read a traceback bottom-up
- [ ]  Trigger and fix each on purpose: `TypeError`, `ValueError`, `KeyError`, `IndexError`, `AttributeError`, `NameError`, `ZeroDivisionError`, `FileNotFoundError`
- [ ]  Day 16: `datetime.now()`; timezone-aware `datetime.now(timezone.utc)`
- [ ]  `timedelta`; subtract two datetimes; `strftime` / `strptime`
- [ ]  ISO-8601 round trip: `isoformat()` and `fromisoformat()`
- [ ]  Solve Day 16 exercises; add timestamp handling to the inventory
- [ ]  Day 17: `try / except / else / finally`
- [ ]  Catch specific exceptions only; never use bare `except:`
- [ ]  `raise` an exception; re-raise with `raise`
- [ ]  Define a custom exception class (`class InvalidRecordError(Exception)`)
- [ ]  Replace printed errors in the inventory with exceptions
- [ ]  Day 18 (skim): `re.search`, `re.findall`, groups, `re.sub`
- [ ]  Write one regex that parses `2026-10-23T10:15:00Z WARN scanner=SN123 code=E42`
- [ ]  Day 19: `open` modes `r`, `w`, `a`; always `with open(...)`; set `encoding="utf-8"`
- [ ]  Read lines; write lines; handle `FileNotFoundError` and `PermissionError`
- [ ]  Read and write CSV with `csv.DictReader` / `DictWriter`
- [ ]  Read and write JSON with `json.load` / `json.dump`
- [ ]  Persist the inventory to a JSON file; reload on start
- [ ]  Day 20: `pip install`, `pip list`, `pip freeze > requirements.txt`, `pip install -r`, `pip uninstall`
- [ ]  Day 21: define a class with `__init__`, attributes, methods
- [ ]  Add `__repr__` and `__str__`; class vs instance attributes
- [ ]  Composition: `Inventory` holds many `Scanner` objects
- [ ]  One inheritance example; add `@property`
- [ ]  Refactor the inventory into `Scanner` and `Inventory` classes
- [ ]  Day 23: `python -m venv .venv`; activate; install inside; freeze; delete and recreate from `requirements.txt`
- [ ]  Day 28: explain GET/POST and status codes 200, 201, 400, 401, 404, 500
- [ ]  `pip install requests`; `requests.get(url, timeout=5)`
- [ ]  `response.raise_for_status()`; `response.json()`
- [ ]  Catch `requests.exceptions.Timeout` and `ConnectionError`
- [ ]  Fetch from a public test API (e.g. JSONPlaceholder) and print 3 fields
- [ ]  **Proof:** inventory runs from a fresh clone using only `requirements.txt` and the README

## L. Git workflow — see semester calendar above (~3 h) **[M]**

- [ ]  `git status`, `git add -p`, `git commit`, `git log --oneline`, `git diff`
- [ ]  Create a branch with `git switch -c feature/x`; merge it back
- [ ]  Push a branch; open a pull request on GitHub; merge it
- [ ]  Create a merge conflict on purpose (same line on two branches); resolve it
- [ ]  Undo a change with `git restore`; undo a commit safely with `git revert`
- [ ]  Write commit messages in the imperative, under 72 characters
- [ ]  **Proof:** work on a branch, open a PR on your own repo, merge it, delete the branch

## M. Python professional essentials — see semester calendar above (~24 h) **[M]**

- [ ]  `pathlib`: build paths with `/`; `Path.glob`; `read_text`, `write_text`; `exists`, `mkdir(parents=True)`
- [ ]  `sys.argv`; `sys.exit(code)`
- [ ]  `shutil.copy`; `subprocess.run([...], capture_output=True, text=True, check=True)`
- [ ]  `argparse`: add `-input`, `-output`, `-verbose`; return exit code 2 on bad input
- [ ]  Typing: annotate every function; use `list[int]`, `dict[str, float]`, `str | None`
- [ ]  Add a type alias; write one `Protocol`
- [ ]  Install `mypy` (or `pyright`); make the inventory type-check clean
- [ ]  `@dataclass` for `Reading`; try `frozen=True`
- [ ]  `Enum` for `Status`; replace status strings with it
- [ ]  `logging.basicConfig`; use `debug/info/warning/error`; one logger per module
- [ ]  Wire `-verbose` to log level; never log secrets
- [ ]  Install `ruff`; run `ruff check` and `ruff format`
- [ ]  VS Code debugger: set a breakpoint, step over/into, inspect variables, watch an expression
- [ ]  Generators: write a function with `yield` that reads a file lazily; write a generator expression
- [ ]  `collections`: `Counter`, `defaultdict`, `deque`; `itertools.islice`; `functools.lru_cache`
- [ ]  Context managers: use `with`; write one with `contextlib.contextmanager`; write one as a class with `__enter__`/`__exit__`
- [ ]  Packaging: create `pyproject.toml` with name, version, `[project.scripts]`
- [ ]  `pip install -e .`; run your CLI by its command name
- [ ]  Binary data: `bytes`, `bytearray`; `int.to_bytes` / `int.from_bytes`
- [ ]  `struct.pack` / `struct.unpack` with `<` and `>`; build and parse one 8-byte frame
- [ ]  Write a simple checksum (sum of bytes mod 256) and verify it on parse
- [ ]  `time.monotonic()`; write a loop with a timeout; write a retry with doubling delay
- [ ]  `threading.Thread` + `queue.Queue`: one producer thread, one consumer thread **[S]**
- [ ]  `asyncio.run`, `async def`, `await asyncio.sleep`, `asyncio.wait_for` **[T]**
- [ ]  `sqlite3`: create a table, insert, select **[T]**
- [ ]  **Proof:** `ruff` and `mypy` pass; one command runs your CLI with `-help`

## N. Project 1 — Reliable Virtual Device Monitor — see semester calendar above → early Feb (~25 h) **[M]**

*Contains the old Checkpoint B: the log analyzer is its first half.*

**Requirements and design** *(University tie-in: CCS3310, CCS3300)*

- [ ]  Write 8 numbered requirements (`REQ-01 …`), each with an acceptance criterion
- [ ]  Draw the architecture: Simulator → Frame encoder → Transport (queue or file) → Parser/validator → Analyzer → Reporter/CLI
- [ ]  Write one paragraph per component describing its single responsibility
- [ ]  Choose the package layout: `device_monitor/{simulator,frames,validator,analyzer,reporter,cli}.py`

**Build**

- [ ]  Simulator: generate telemetry (temperature, voltage, status) from a seeded random generator
- [ ]  Add fault injection: spike, stuck value, missing frames, corrupted byte
- [ ]  Frame format: start byte, length, type, payload, checksum, end byte
- [ ]  Frame encoder with `struct`; frame parser with `struct`
- [ ]  Validator: wrong length, bad checksum, unknown type, out-of-range value; collect errors instead of crashing
- [ ]  Analyzer: per-sensor min/max/mean; count faults by type; detect missing heartbeat using `time.monotonic()` timeout
- [ ]  Reporter: print summary; write results as JSON and CSV
- [ ]  Reader for CSV and JSON log files
- [ ]  CLI: `device-monitor simulate --seed 42 --count 1000` and `device-monitor analyze --input file`
- [ ]  Use `logging` with levels; `-verbose` switches to debug

**Tests** *(University tie-in: CCS3311)*

- [ ]  Learn `pytest`: `assert`, `pytest.raises`, fixtures, `tmp_path`, `@pytest.mark.parametrize`
- [ ]  Derive test cases using boundary values (min, min−1, max, max+1) and write them down
- [ ]  At least 15 tests: valid frame, short frame, long frame, bad checksum, boundary values, empty file, missing file, malformed CSV row
- [ ]  One test with a mock for the clock or the transport
- [ ]  Save the `pytest` output as a test report in the repo

**Quality and release**

- [ ]  `mypy` and `ruff` pass
- [ ]  README: install, run, example output, 3 error scenarios, architecture diagram
- [ ]  Tag `v0.1` and push

**University tie-in (optional)**

- [ ]  CCS2360: write a one-page pitch for a sensor-monitoring prototype, reusing your architecture diagram **[T]**

## O. NumPy prep for Machine Learning — see semester calendar above (~6 h) **[S]**

- [ ]  `pip install numpy`; create arrays with `np.array`, `arange`, `linspace`, `zeros`, `ones`
- [ ]  Check `dtype`, `shape`, `ndim`; use `reshape`
- [ ]  Index and slice 1-D and 2-D arrays; use boolean masks
- [ ]  Compare a Python loop with a vectorized operation using `timeit`
- [ ]  Use `mean`, `std`, `min`, `max`, `sum` with `axis`
- [ ]  Understand broadcasting: add a row vector to a matrix
- [ ]  Dot product with `np.dot` and `@`
- [ ]  Load your simulator CSV with NumPy and compute its statistics

## P. C foundations, weeks 1–6 — see semester calendar above → Mar (~36 h) **[M]**

*Reference: Beej's Guide to C and the C chapters of your university material. Compile every program with `gcc -std=c17 -Wall -Wextra -g`.*

**Week 1 — Toolchain**

- [ ]  Write, compile, run `hello.c`
- [ ]  Run the stages separately: `gcc -E`, `gcc -S`, `gcc -c`, then link
- [ ]  Look at the object file with `nm` and `objdump -d` (just look)
- [ ]  Write a minimal `Makefile` with `all` and `clean`

**Week 2 — Types and control flow**

- [ ]  Use `int`, `char`, `unsigned`, `long`, `size_t`; include `<stdint.h>` and use `uint8_t`, `uint16_t`, `int32_t`
- [ ]  Print with `printf` format specifiers (`%d %u %zu %x %c %s %f`)
- [ ]  Show integer overflow of `unsigned char` and signed `int`; write down what is defined and what is not
- [ ]  Show integer promotion and implicit casts; fix with explicit casts
- [ ]  `if/else`, `switch`, `for`, `while`, `do-while`
- [ ]  **Proof:** FizzBuzz and "sum 1..N" in C

**Week 3 — Functions, headers, separate compilation**

- [ ]  Write function prototypes; call before definition
- [ ]  Split a program into `main.c`, `util.c`, `util.h`; add include guards
- [ ]  Compile with `gcc -c` per file, then link
- [ ]  Use `static` for file-private functions
- [ ]  Replace one `#define` constant with `enum` or `static const`; list one macro pitfall
- [ ]  **Proof:** a 3-file program builds with one `make`

**Week 4 — Arrays and strings**

- [ ]  Declare arrays; use `sizeof(arr)/sizeof(arr[0])`
- [ ]  Write a null-terminated string by hand; print it
- [ ]  Use `strlen`, `strcmp`, `strncpy`, `snprintf`; explain why `strcpy` is unsafe
- [ ]  Trigger an out-of-bounds write; compile with `fsanitize=address`; read the report
- [ ]  **Proof:** write your own `my_strlen` and `my_strcmp`

**Week 5 — Pointers 1**

- [ ]  `&` and ; print an address; dereference a pointer
- [ ]  Write `swap(int *a, int *b)`
- [ ]  Return a result through an output pointer
- [ ]  Always check for `NULL`; trigger a null dereference and read the crash
- [ ]  Explain `const int *p`, `int *const p`, `const int *const p`
- [ ]  **Proof:** draw memory boxes for a swap on paper

**Week 6 — Pointers 2**

- [ ]  Pointer arithmetic over an array; show `p + 1` moves by `sizeof(*p)`
- [ ]  Show array-to-pointer decay in a function parameter; show `sizeof` differs
- [ ]  Pointer to pointer; `char *argv[]` in `main`
- [ ]  A function pointer used as a callback (`int (*cmp)(int, int)`)
- [ ]  **Proof:** explain 3 differences between an array and a pointer

**Exit gate — Y3 S1** **[M]**

- [ ]  Project 1 is tagged `v0.1`, tested, with a README
- [ ]  You can pick list / tuple / set / dict for a new problem without notes
- [ ]  You can write and debug a small C program with pointers; the weeks 1–6 proofs pass
- [ ]  University architecture, requirements and SQA deliverables are on schedule

---

## Semester alignment additions — Y3 S1

- [ ] **[M] [ADDED] November:** Map CCS3310 requirements to Project 1 acceptance tests; keep a small backlog and record one development iteration.
- [ ] **[M] [ADDED] November–January:** For CCS3300, compare two architecture options and record one decision with constraints and tradeoffs.
- [ ] **[M] [ADDED] January–February:** For CCS3311, create a requirement-to-test matrix and a defect log; distinguish unit, integration and acceptance testing.
- [ ] **[M] [ADDED] November:** Check CCS2360 team, entry, judging and submission requirements; schedule its prototype/pitch before its actual deadline.
- [ ] **[M] [ADDED] November–March:** Complete CCS3356 lectures, NLP practicals, assessments and revision; keep a syllabus checklist without adding an unrelated NLP side project.
- [ ] **[M] [ADDED] March gate:** Run Project 1 from a clean environment; explain its architecture and show requirements, tests and one fixed defect before April revision.

# Y3 S2 — C++, Linux Systems & First ML *(Jun 2027 → Oct 2027 exams · 15 credits)*

| Module | Credits · type | Feeds the arc |
| --- | --- | --- |
| CCS3313 Advanced Software Design | 3 · core | Interfaces, ownership, testable C++ design |
| CCS3302 Introduction to Research Methods | 3 · core | Reproducible benchmarks of your own programs |
| SMA2307 Discrete Mathematics | 3 · core | State machines, graphs, counting |
| SMA2202 Linear Algebra | 3 · elective | Vectors, matrices, rotations (later: `tf2`, filters, ML) |
| CCS4340 Machine Learning | 3 · elective | Supervised learning, evaluation, data leakage |

**Plan:** May bridge: C weeks 7–12 (A), continuing into June if needed. June: packet parser (B). July–August: C++ (C); September: Linux systems (D) and Project 2 (E). F and H follow the ML and linear algebra modules from June to September; G is a small recurring session. October: examinations and review only. I is optional only after core gates pass. The original 155 h mandatory estimate excludes some parallel work; count all selected blocks before committing.

---

## A. C foundations, weeks 7–12 — see semester calendar above (~36 h) **[M]**

**Week 7 — Structs, enums, unions**

- [ ]  Define a `struct`; use `typedef`; initialize with designated initializers (`.id = 1`)
- [ ]  Pass a struct by value, then by pointer; compare behavior
- [ ]  Build an array of structs and loop over it
- [ ]  Model device states with an `enum`; print a state name with a `switch`
- [ ]  Write one `union` and read the same bytes as two types
- [ ]  Print `sizeof` and `offsetof` for a struct; reorder fields to remove padding
- [ ]  Write down why you will **parse bytes explicitly** instead of casting a buffer to a packed struct
- [ ]  **Proof:** explain struct padding using your own `offsetof` output

**Week 8 — Memory**

- [ ]  Draw stack vs heap for a small program
- [ ]  Use `malloc`, `calloc`, `realloc`, `free`; always check for `NULL`
- [ ]  State the ownership rule in one sentence: who allocates, who frees
- [ ]  Cause on purpose, under ASan: a leak, a double free, a use-after-free; read each report
- [ ]  Implement a growable `int` array (`push`, `get`, `free`) that doubles capacity
- [ ]  Run it under ASan with zero errors
- [ ]  **Proof:** find a planted bug in a 30-line program using only the ASan report

**Week 9 — Bit operations**

- [ ]  Use `& | ^ ~ << >>` on `uint8_t`
- [ ]  Write `set_bit`, `clear_bit`, `toggle_bit`, `test_bit`
- [ ]  Print any byte in binary and hex
- [ ]  Extract a 3-bit field from a byte with a mask and a shift
- [ ]  Write a program that detects host endianness
- [ ]  Write `read_u16_be(const uint8_t *buf)` and `write_u16_be(uint8_t *buf, uint16_t v)`
- [ ]  **Proof:** pack and unpack three flags into one byte without notes

**Week 10 — `const`, `static`, `volatile`, file I/O**

- [ ]  Mark every read-only parameter `const`; fix the warnings that appear
- [ ]  Use a `static` local variable and a file-scope `static` function
- [ ]  Explain `volatile` in two sentences, plus one sentence on what it does **not** do (not atomic, not a thread primitive)
- [ ]  `fopen`, `fgets`, `fprintf`, `fclose`; check every return value
- [ ]  `fread` / `fwrite` a binary file of structs
- [ ]  Use `errno` and `perror`
- [ ]  **Proof:** read a text file of readings into an array and print the maximum

**Week 11 — GDB and sanitizers**

- [ ]  Compile with `g -O0`; start `gdb ./a.out`
- [ ]  Use `break`, `run`, `next`, `step`, `print`, `bt`, `info locals`, `watch`, `x/16xb`
- [ ]  Compile with `fsanitize=address,undefined`; trigger a signed-overflow report and read it
- [ ]  List 5 kinds of undefined behavior with a one-line example each
- [ ]  Try `Werror` on an old program; fix every warning
- [ ]  **Proof:** debug a crashing program using `bt` and `print` only

**Week 12 — Data structures in C**

- [ ]  Array-based stack (`push`, `pop`, `peek`)
- [ ]  Singly linked list (`insert`, `remove`, `free_all`)
- [ ]  Ring buffer with fixed array, `head`, `tail`, and clear full/empty rules
- [ ]  Assert-based tests for all three; zero ASan errors
- [ ]  **Proof:** whiteboard the ring buffer wrap-around and the full vs empty condition

## B. C packet parser — see semester calendar above (~12 h) **[M]**

- [ ]  Write the frame spec: `SOF 0xAA | LEN | TYPE | PAYLOAD[LEN] | CRC8 | EOF 0x55`; maximum payload size; list the message types
- [ ]  Implement `crc8` (polynomial `0x07`); check it against two hand-computed values
- [ ]  Define `typedef enum` for parse results (`OK`, `NEED_MORE`, `BAD_CRC`, `BAD_EOF`, `TOO_LONG`)
- [ ]  Implement a byte-by-byte state machine `parser_feed(parser_t *, uint8_t byte, frame_t *out)`
- [ ]  Handle resynchronization: discard bytes until the next `SOF`
- [ ]  Write assert tests: valid frame, truncated frame, bad CRC, bad EOF, oversize `LEN`, zero-length payload, garbage before `SOF`, two frames back to back
- [ ]  Add a loop that feeds 100 000 random bytes; run under ASan/UBSan with no errors
- [ ]  README: spec, how to build, how to test
- [ ]  Commit and push as `c-packet-parser`
- [ ]  **Proof:** a classmate-style review: explain every state transition without reading the code

## C. Modern C++ — see semester calendar above (~60 h) **[M]**

*Reference: learncpp.com and cppreference.com. Compile with `g++ -std=c++20 -Wall -Wextra -Wpedantic -g`.*

**Week 1 — From C to C++**

- [ ]  Compile and run `hello.cpp`; use `std::cout`, `std::string`, `namespace std`
- [ ]  Use `auto` and range-based `for`
- [ ]  Use references (`int&`, `const std::string&`); show why references can't be null
- [ ]  Overload two functions
- [ ]  **Proof:** port your C `my_strlen` and `swap` to C++ using references

**Week 2 — Containers**

- [ ]  `std::vector`: `push_back`, `size`, indexing, `at`, iterate
- [ ]  `std::array`, `std::map`, `std::unordered_map`, `std::set`
- [ ]  Iterators: `begin`, `end`; erase while iterating the safe way
- [ ]  `std::string_view`; structured bindings (`auto [k, v] : map`)
- [ ]  **Proof:** count word frequency in a text file with `unordered_map`

**Week 3 — Algorithms, lambdas, `optional`**

- [ ]  `std::sort` with a lambda; `std::find_if`; `std::transform`; `std::accumulate`
- [ ]  Lambda captures: by value `[=]`, by reference `[&]`, explicit `[x]`
- [ ]  `std::optional` as a return type for "maybe a value"
- [ ]  **Proof:** filter and sort a vector of readings with algorithms and no hand-written loops

**Week 4 — Classes**

- [ ]  Write a class with a constructor, member-initializer list, and destructor
- [ ]  Use `private` / `public`; mark getters `const`
- [ ]  Mark single-argument constructors `explicit`
- [ ]  Write the "rule of zero" in one sentence and apply it
- [ ]  Compose one class from another (`Device` has a `Sensor`)
- [ ]  Overload `operator<<` for printing
- [ ]  **Proof:** design a `Reading` class and justify each `const` and `explicit`

**Week 5 — RAII and ownership**

- [ ]  Show a leak with raw `new` / `delete` and an early `return`
- [ ]  Fix it with `std::unique_ptr` and `std::make_unique`
- [ ]  Write a small RAII class that closes a `FILE*` in its destructor
- [ ]  Use `std::shared_ptr` once; explain when `weak_ptr` is needed to break a cycle
- [ ]  Draw an ownership diagram for your project design (who owns whom)
- [ ]  **Proof:** zero `new` / `delete` in your code and zero ASan findings

**Week 6 — Copy and move**

- [ ]  Observe copy construction with a class that prints from each special member
- [ ]  Write a move constructor and move assignment
- [ ]  Use `std::move` and explain what it actually does
- [ ]  Choose pass-by-value, `const&`, or `&&` for three example parameters
- [ ]  **Proof:** explain the rule of 0 / 3 / 5 with one example each

**Week 7 — Polymorphism and templates**

- [ ]  Write an abstract interface class (`ISensor`) with a pure `virtual` method
- [ ]  Add `override`, `final`, and a virtual destructor; explain why the destructor is virtual
- [ ]  Write two implementations (`FakeSensor`, `NoisySensor`) and call them through the interface
- [ ]  Write a function template and a small class template (`RingBuffer<T, N>`)
- [ ]  Use `std::variant` + `std::visit` for three event types **[S]**
- [ ]  **Proof:** swap `FakeSensor` for `NoisySensor` without touching the caller

**Week 8 — CMake and tests**

- [ ]  Layout: `include/`, `src/`, `tests/`, top-level `CMakeLists.txt`
- [ ]  Build a static library target and an executable that links it
- [ ]  Set warnings with `target_compile_options`; set `CMAKE_CXX_STANDARD 20`
- [ ]  Add GoogleTest with `FetchContent`; write 3 tests; run with `ctest`
- [ ]  Export `compile_commands.json`
- [ ]  **Proof:** a fresh clone builds and tests with two commands

**Week 9 — Quality tooling and error handling**

- [ ]  Build with ASan + UBSan via a CMake option; run all tests under it
- [ ]  Run `clang-tidy` and `clang-format`; fix the first 10 findings
- [ ]  Time a function with `std::chrono::steady_clock`; repeat 30 times; record mean and standard deviation
- [ ]  Compare exceptions, `std::optional`, and error codes; write a 5-line decision rule
- [ ]  Use GDB on a C++ program: `break` in a method, `print` a `std::vector`
- [ ]  **Proof:** inject a bug; find it with a sanitizer or GDB, not by reading

**Week 10 — Consolidation**

- [ ]  Re-implement the C packet parser as a C++ class with the same tests
- [ ]  Compare line count, bug risk, and readability in 5 sentences

## D. Linux systems — see semester calendar above (~18 h) **[M]**

**Week 1 — Processes, signals, file descriptors**

- [ ]  Explain process vs thread in your own words
- [ ]  In C, `fork()` a child, `exec` a command, `wait()` for it; print the exit code
- [ ]  Install a `SIGINT` handler with `sigaction`; keep the handler tiny
- [ ]  Use `open`, `read`, `write`, `close`; compare with buffered `stdio`
- [ ]  Run `strace` on a small program; find the `write` syscall
- [ ]  **Proof:** explain what happens between `Ctrl+C` and your handler running

**Week 2 — Threads and synchronization**

- [ ]  `std::thread`, `join`, passing arguments
- [ ]  `std::mutex` with `std::lock_guard`
- [ ]  Create a data race on purpose; catch it with `fsanitize=thread`
- [ ]  `std::condition_variable`: write a bounded producer/consumer queue
- [ ]  Create a deadlock on purpose; fix it with `std::scoped_lock`
- [ ]  **Proof:** explain why `volatile` does not fix your race

**Week 3 — Sockets and networking**

- [ ]  Explain IP, port, DNS, TCP vs UDP; try `ip addr`, `ping`, `curl`, `ss -tulpn`, `dig`
- [ ]  Write a TCP echo server and client with `socket`, `bind`, `listen`, `accept`, `connect`, `send`, `recv`
- [ ]  Add a length-prefixed message so `recv` partial reads are handled
- [ ]  Write a UDP sender and receiver
- [ ]  Add a timeout with `poll`
- [ ]  **Proof:** send 1 000 framed messages over TCP with zero loss and print the count

## E. Project 2 — C++ Virtual Sensor Device — see semester calendar above (~20 h) **[M]**

**Requirements and design** *(University tie-in: CCS3313, SMA2307)*

- [ ]  Write 8 numbered requirements with acceptance criteria
- [ ]  Define interfaces first: `ISensor`, `ITransport`, `ILogger`
- [ ]  Model the device as a state machine: `INIT → IDLE → SAMPLING → FAULT → SHUTDOWN`; draw it as a graph (Discrete Math tie-in) and write the transition table
- [ ]  Write a short design rationale: ownership, threading, error strategy

**Build**

- [ ]  `DeviceStateMachine` driven by an event queue
- [ ]  Sensor simulation with configurable noise and fault flags (disconnect, stuck, spike)
- [ ]  Protocol: reuse your frame format; implement encoder/decoder with CRC
- [ ]  CLI: run for N seconds, set sample rate, enable faults, write frames to stdout or a TCP socket
- [ ]  Logging with levels and timestamps
- [ ]  Optional Python harness that connects over TCP and checks frames **[S]**

**Tests and measurement** *(University tie-in: CCS3302 Research Methods)*

- [ ]  GoogleTest: every legal and illegal state transition (table-driven)
- [ ]  GoogleTest: protocol round-trip; malformed frames
- [ ]  Write a measurement protocol: question, variables, number of runs, how you control noise
- [ ]  Measure time per frame and memory use over 30 runs; report mean ± standard deviation in a table
- [ ]  GitHub Actions: build, `ctest`, and an ASan/UBSan job

**Release**

- [ ]  README with build, run, state diagram, protocol table, measurement table
- [ ]  Tag `v0.1` and push

## F. Machine Learning, practical side — see semester calendar above **[M] ~10 h · [S] ~12 h**

- [ ]  **[M]** Install `scikit-learn`, `matplotlib`, `jupyter` in a venv
- [ ]  **[M]** Run the standard workflow once: load data → split → fit → predict → score
- [ ]  **[M]** `train_test_split` with a fixed `random_state`
- [ ]  **[M]** Scale features with `StandardScaler`; fit on train only; explain why
- [ ]  **[M]** Train `LinearRegression` and `LogisticRegression`; read the coefficients
- [ ]  **[M]** Compute accuracy, precision, recall, F1, confusion matrix; explain when accuracy misleads
- [ ]  **[M]** Use `cross_val_score` (k-fold)
- [ ]  **[M]** Create an overfit and an underfit model; plot train vs validation score
- [ ]  **[M]** Demonstrate data leakage once (scaling before splitting) and measure the effect
- [ ]  **[S]** *Telemetry Anomaly Detector:* export labeled frames from your C++ device (fault flag = label) to CSV
- [ ]  **[S]** Build features: rolling mean, rolling standard deviation, rate of change
- [ ]  **[S]** Split **by time**, not randomly; explain why
- [ ]  **[S]** Baseline: a fixed threshold rule; record precision and recall
- [ ]  **[S]** Model: `RandomForestClassifier` or `IsolationForest`; compare with the baseline
- [ ]  **[S]** Error analysis: list 10 mistakes, say why each happened
- [ ]  **[S]** Write a 1-page finding with one table and one plot; commit the notebook

## G. DSA drip — one item every ~2 weeks (~20 h) **[S]**

- [ ]  Dynamic array in C++ (no `std::vector`) with amortized growth; state its Big-O
- [ ]  Singly linked list: insert, delete, reverse
- [ ]  Stack and queue (ring buffer) with templates
- [ ]  Hash map with chaining: insert, find, erase, resize
- [ ]  Binary search (iterative); explain the off-by-one trap
- [ ]  Insertion sort and merge sort; compare timing on 10⁵ elements
- [ ]  Quick sort with a clear pivot rule; state worst case
- [ ]  Recursion: factorial, Fibonacci, and one recursive-to-iterative conversion
- [ ]  Graph as an adjacency list; BFS and DFS; shortest path on an unweighted graph
- [ ]  For each item above, write its time and space complexity in the README

## H. Linear Algebra practice for robotics — see semester calendar above (~6 h) **[S]**

- [ ]  NumPy: vector add, scalar multiply, dot product, norm
- [ ]  Matrix multiply, transpose, `np.linalg.inv`, `np.linalg.solve`
- [ ]  Solve a 2×2 linear system by hand and with NumPy; compare
- [ ]  Build a 2-D rotation matrix; rotate 5 points by 30°
- [ ]  Compose two rotations; confirm the order matters
- [ ]  Build a 3×3 homogeneous transform (rotate + translate) and apply it to points

## I. Zephyr starter — only if ahead of schedule — see semester calendar above (~8 h) **[T]**

- [ ]  Buy one Zephyr-supported board and a USB cable
- [ ]  Follow the official Zephyr *Getting Started Guide* for your OS until `west` and the SDK work
- [ ]  Build and run `samples/hello_world` for `native_sim`
- [ ]  Build `samples/basic/blinky` for your board; flash it; confirm the LED blinks

## Semester alignment additions — Y3 S2

- [ ] **[M] [ADDED] June:** For CCS3302, formulate a small research question connected to the device project; define variables, baseline and evaluation method.
- [ ] **[M] [ADDED] June–July:** Keep a literature matrix of 5–10 relevant sources: problem, method, result, limitation and relevance; store citations with the university-required style.
- [ ] **[M] [ADDED] July–August:** For CCS3313, refactor Project 2 behind interfaces; document ownership and dependency direction, then justify one design pattern only where it solves a real problem.
- [ ] **[M] [ADDED] June–September:** Maintain separate SMA2307 and SMA2202 syllabus checklists and weekly problem practice; link graphs/state machines and vectors/matrices to this roadmap without duplicating whole courses.
- [ ] **[M] [ADDED] June–September:** Map CCS4340 assessments to the ML block; record dataset provenance, split method, preprocessing and a reproducible baseline.
- [ ] **[M] [ADDED] August–September:** Identify industrial-training eligibility, application lead times and university approval steps; prepare an initial CV and apply ahead of confirmed placement deadlines.
- [ ] **[M] [ADDED] September:** Shortlist capstone questions, discuss feasibility with a potential supervisor, and identify required hardware before Y4 begins.

## Exit gate — Y3 S2 **[M]**

- [ ]  `c-packet-parser` and Project 2 are tagged and public, with tests and CI
- [ ]  You can fix an ASan / UBSan finding without help and explain the cause
- [ ]  You can explain stack vs heap, ownership, RAII, and a race condition on a whiteboard
- [ ]  ML coursework and Research Methods deliverables are on schedule

---

# Y4 S1 — Firmware, IoT & Deep Learning on the Edge *(Nov 2027 → Apr 2028 exams · 16 credits — heaviest semester)*

| Module | Credits · type | Feeds the arc |
| --- | --- | --- |
| CCS3301 Capstone Project Part 1 | 3 · core | Requirements, feasibility, baseline, prototype |
| CCS3440 Artificial Intelligence | 4 · core | Search and planning (BFS, UCS, A*) reused in robot planning |
| IHM1301 Human Behavior and Ethics | 3 · core | Safety requirements, human oversight, safe-stop |
| CCS4310 Deep Learning | 3 · elective | PyTorch training, regularization, evaluation |
| CCS4353 Internet of Things | 3 · elective | Sensing, protocols, device-to-server telemetry |

**Plan:** November: hardware setup (A), start Zephyr (B), and start capstone planning (I). November–February: B, then Project 3 (C); D and E follow Deep Learning and AI coursework. January–March: selected Embedded Linux tasks (F), reusing them for IoT. March: capstone validation and Part 1 submission preparation. April: examinations and required submissions. May bridge: finish F, then TinyML (G) and ROS basics (H) as capacity permits. B alone is estimated at 72 h; A+B+C+D+E+I total about 142 h, before F/G/H. Do not use the old 95 h mandatory estimate.
**Overload rule:** drop `[T]` first, then ROS 2 basics (move to Y4 S2 April), then Embedded Linux.
**Re-check at semester start:** Zephyr, ROS 2, ExecuTorch and LiteRT docs. Command names and board support change between releases.

---

## A. Hardware setup — see semester calendar above (~4 h) **[M]**

- [ ]  Confirm you own: one Zephyr-supported board, a USB cable, a breadboard, jumper wires, one I2C sensor (IMU or temperature), one LED + resistor, one button
- [ ]  Buy a cheap logic analyzer (8-channel USB) if you don't have one
- [ ]  Buy a Raspberry Pi (for Block F) and a microSD card **[S]**
- [ ]  Follow the official Zephyr *Getting Started Guide*; get `west` and the SDK working
- [ ]  Build `samples/hello_world` for `native_sim` and run it
- [ ]  Build and flash `samples/basic/blinky` for your board; confirm the LED
- [ ]  Open the serial console (`screen`, `minicom`, or `west` monitor) and read the boot log

## B. Zephyr firmware, weeks 1–12 — see semester calendar above (~72 h) **[M]**

**Week 1 — Your own application**

- [ ]  Create an application folder outside the Zephyr tree with `CMakeLists.txt`, `prj.conf`, `src/main.c`
- [ ]  Build with `west build -b <board> -p auto`; flash with `west flash`
- [ ]  Print with `printk` and with the logging subsystem (`LOG_MODULE_REGISTER`, `LOG_INF`, `LOG_ERR`)
- [ ]  Change the log level in `prj.conf`
- [ ]  **Proof:** rebuild from scratch, flash, and read your log lines without help

**Week 2 — Threads and time**

- [ ]  Create two threads with `K_THREAD_DEFINE`; give them different priorities
- [ ]  Use `k_msleep`; run a periodic task with `k_timer`
- [ ]  Observe preemption: a busy high-priority thread starves a lower one
- [ ]  Explain cooperative vs preemptive threads
- [ ]  **Proof:** blink two LEDs (or two log streams) at different rates from two threads

**Week 3 — Synchronization and messaging**

- [ ]  `k_mutex`: protect a shared counter
- [ ]  `k_sem`: signal from one thread to another
- [ ]  `k_msgq`: send sensor readings from a producer thread to a consumer thread
- [ ]  `k_work` and a work queue: defer processing out of an ISR
- [ ]  Explain priority inversion and name Zephyr's mitigation
- [ ]  **Proof:** producer/consumer with a full queue handled without losing or crashing

**Week 4 — GPIO and interrupts**

- [ ]  Read the board's devicetree: find the `led0` and `sw0` aliases
- [ ]  Use `gpio_dt_spec`; configure an input and an output
- [ ]  Attach a button interrupt callback; toggle the LED
- [ ]  Keep the ISR tiny: set a flag or submit work; do the rest in a thread
- [ ]  Debounce in software (ignore edges within a time window)
- [ ]  **Proof:** count 20 button presses with zero double-counts

**Week 5 — Devicetree and Kconfig**

- [ ]  Open the generated `zephyr.dts` in the build folder and read your board's nodes
- [ ]  Write a `.overlay` that adds an alias and enables a peripheral
- [ ]  Change `prj.conf` options; use `west build -t menuconfig` to find one
- [ ]  Explain the difference between devicetree (hardware) and Kconfig (software options)
- [ ]  **Proof:** move an LED to a different pin using only an overlay

**Week 6 — UART and framing**

- [ ]  Send text over the UART with the polling API
- [ ]  Receive with the interrupt-driven API into a ring buffer
- [ ]  Port your **C packet parser** to Zephyr and feed it UART bytes
- [ ]  Send a framed telemetry packet (same format as Y3 S2) from the board to your PC
- [ ]  Read it on the PC with a small Python script and verify the CRC
- [ ]  **Proof:** 1 000 frames received with zero CRC errors, then break the cable and watch your timeout fire

**Week 7 — I2C sensor**

- [ ]  Wire the I2C sensor; scan the bus for its address
- [ ]  Read the sensor's datasheet: find the WHO_AM_I register and the data registers
- [ ]  Read WHO_AM_I using raw I2C calls and check it matches the datasheet
- [ ]  Read a measurement through Zephyr's sensor API (`sensor_sample_fetch`, `sensor_channel_get`)
- [ ]  Handle a missing device: return an error and log it
- [ ]  **Proof:** print one converted reading per second in real units

**Week 8 — ADC, PWM, SPI**

- [ ]  ADC: read one channel; convert counts to millivolts; state the resolution and reference
- [ ]  PWM: dim an LED at three duty cycles; measure the frequency with the logic analyzer **[S]**
- [ ]  SPI: describe CPOL/CPHA and chip-select in your own words; run one loopback or sensor read **[S]**
- [ ]  Compare UART, I2C, SPI, CAN in a 4-row table: wires, speed, addressing, typical use
- [ ]  **Proof:** pick the right bus for 3 given sensors and justify each choice

**Week 9 — Timing and jitter**

- [ ]  Toggle a GPIO inside a timer-driven 100 Hz loop
- [ ]  Capture the pin with the logic analyzer; measure period and jitter
- [ ]  Measure scheduling latency with `k_cycle_get_32()`
- [ ]  Repeat with a busy higher-priority thread; record how jitter changes
- [ ]  Write mean, maximum, and standard deviation in a table
- [ ]  **Proof:** state whether your system is hard or soft real-time and why

**Week 10 — Reliability**

- [ ]  Enable the watchdog; feed it from one thread; stop feeding it and watch the reset
- [ ]  Define an error policy: retry, degrade, or safe-stop for each failure you know
- [ ]  Enable thread-stack analysis and check stack headroom
- [ ]  Use `__ASSERT` for impossible states
- [ ]  Cause a crash on purpose (null dereference); read the fault dump
- [ ]  **Proof:** write the 5-line error policy for your node

**Week 11 — Testing**

- [ ]  Run the node on `native_sim`
- [ ]  Write 3 tests with `ztest` (`ZTEST`)
- [ ]  Run them with `west twister`
- [ ]  Put the hardware access behind one function so tests can replace it
- [ ]  Test the framing and CRC code on the PC with no hardware
- [ ]  **Proof:** CI-style run: one command builds and tests everything

**Week 12 — Debugging and BLE**

- [ ]  Debug on hardware with `west debug` (SWD + GDB): breakpoint, step, `bt`, inspect a variable
- [ ]  Read `west build -t rom_report` and `ram_report`; note the biggest consumers
- [ ]  If your board has BLE: run the peripheral sample; connect with a phone app **[S]**
- [ ]  Add a custom GATT characteristic that notifies a sensor value **[S]**

## C. Project 3 — Zephyr Sensor Node — see semester calendar above → Jan (~20 h) **[M]**

**Requirements and design** *(University tie-in: CCS3301, IHM1301)*

- [ ]  Write 8 numbered requirements with measurable acceptance criteria (e.g. "report sensor loss within 500 ms")
- [ ]  Write the failure table: failure, effect, how detected, response
- [ ]  State the node's states: `INIT → CALIBRATE → SAMPLE → REPORT → FAULT → SAFE`; draw the diagram and the transition table
- [ ]  Write one paragraph on human oversight and what "safe" means for this node

**Build**

- [ ]  Fixed-rate sampling thread (timer-driven)
- [ ]  Framed telemetry over UART with CRC
- [ ]  Command handling over UART: `start`, `stop`, `set_rate`
- [ ]  Fault injection: unplug the sensor; send a corrupt command; overflow the queue
- [ ]  Watchdog and safe state on repeated faults
- [ ]  Structured logging

**Tests and measurement**

- [ ]  `ztest` / Twister tests on `native_sim` for the state machine and parser
- [ ]  Measure sampling jitter and CPU load; report mean, max, standard deviation
- [ ]  Record flash and RAM usage from the `rom_report` / `ram_report`

**Release**

- [ ]  README with wiring diagram, build and flash steps, protocol table, results table
- [ ]  Record a 60-second video of it running and recovering from a fault
- [ ]  Tag `v0.1` and push

## D. Deep Learning in PyTorch — see semester calendar above (parallel with the module, ~14 h) **[M]**

- [ ]  Install PyTorch in a venv; create tensors; check `shape`, `dtype`, `device`
- [ ]  Use `autograd`: compute a gradient with `backward()` and verify it by hand for `y = x²`
- [ ]  Write a training loop: forward, loss, `zero_grad`, `backward`, `step`
- [ ]  Define an `nn.Module` (small MLP); use `Dataset` and `DataLoader`
- [ ]  Choose a loss and an optimizer; explain learning rate, batch size, epoch
- [ ]  Evaluate in `eval()` mode under `torch.no_grad()`
- [ ]  Overfit a tiny batch on purpose (sanity check that the model can learn)
- [ ]  Add dropout and weight decay; compare validation curves
- [ ]  Save and load a model with `state_dict`
- [ ]  Fix random seeds; log each run's settings and results to a CSV
- [ ]  **Proof:** reproduce the same accuracy twice from a clean run

## E. AI module algorithms — see semester calendar above (~12 h) **[M]**

- [ ]  Represent a grid world (walls, start, goal) in Python
- [ ]  Implement BFS and DFS; print the path
- [ ]  Implement uniform-cost search with `heapq`
- [ ]  Implement A* with the Manhattan heuristic; count nodes expanded by each method
- [ ]  Explain admissible and consistent heuristics with one example each
- [ ]  Write unit tests: reachable goal, unreachable goal, start = goal
- [ ]  Keep the A* code in its own module; you will reuse it in Y4 S2
- [ ]  **Proof:** compare BFS, UCS, A* in a 3-row table (path length, nodes expanded)

## F. Embedded Linux on a Raspberry Pi — see semester calendar above → Feb (~36 h) **[S]**

**Week 1 — Bring-up**

- [ ]  Flash Raspberry Pi OS (Lite); enable SSH headless; log in over the network
- [ ]  `systemctl status`, `journalctl -u`, `ps`, `htop`
- [ ]  Copy files with `scp`; sync a folder with `rsync`

**Week 2 — Gateway reads the node**

- [ ]  Connect the Zephyr board to the Pi by USB; find `/dev/ttyACM0`
- [ ]  Open the port in C++ with `termios` (8N1, raw mode)
- [ ]  Reuse your C++ frame decoder; print decoded readings
- [ ]  Handle partial reads and reconnects

**Week 3 — Run it as a service**

- [ ]  Write a `systemd` unit for the gateway with `Restart=on-failure`
- [ ]  Enable it at boot; reboot the Pi; confirm it starts
- [ ]  Kill the process; confirm `systemd` restarts it
- [ ]  Read its logs with `journalctl`

**Week 4 — Device tree and buses**

- [ ]  Look at `/proc/device-tree`
- [ ]  Enable I2C with `raspi-config`; run `i2cdetect -y 1`
- [ ]  Read a sensor from Linux user space through `/dev/i2c-1`
- [ ]  Write 5 sentences: how Linux device tree differs from Zephyr's

**Week 5 — Cross-compile and MQTT** *(University tie-in: CCS4353)*

- [ ]  Build the gateway natively on the Pi; then cross-compile it for `aarch64` with a CMake toolchain file **[S]**
- [ ]  Install `mosquitto`; publish a test message with the CLI tools
- [ ]  Publish decoded telemetry from the gateway to an MQTT topic
- [ ]  Subscribe from your laptop and plot the values
- [ ]  Describe the data path device → gateway → broker → subscriber for your IoT assignment

**Week 6 — Yocto** **[T]**

- [ ]  Follow the Yocto Project quick build for `qemux86-64`; build `core-image-minimal`
- [ ]  Boot the image in QEMU; log in
- [ ]  Write down what a *layer*, a *recipe*, and an *image* are

## G. TinyML on the node — see semester calendar above → Mar (~24 h) **[S]**

- [ ]  Choose one task: IMU gesture (3 classes) or vibration anomaly (normal vs abnormal)
- [ ]  Record the dataset from your node: 3 classes × at least 100 windows each; save as CSV
- [ ]  Split by recording session, not by random row; explain why
- [ ]  Train a small model in PyTorch (MLP or 1-D CNN); record accuracy and confusion matrix
- [ ]  Quantize to int8 (post-training); compare accuracy with the float model
- [ ]  Pick the runtime by board CPU: Cortex-M → ExecuTorch or LiteRT for Microcontrollers; other CPUs → LiteRT for Microcontrollers
- [ ]  Add the runtime as a Zephyr module; run a dummy inference on the board
- [ ]  Run the real model on the board; compare its outputs with the host outputs on the same inputs
- [ ]  Measure inference time with `k_cycle_get_32()`; record flash and RAM before and after adding the model
- [ ]  Write a results table: accuracy (host float, host int8, device), latency, RAM, flash
- [ ]  Add a fallback: if the model fails or times out, the node uses a plain threshold rule

## H. ROS 2 basics — see semester calendar above → Mar (~24 h) **[S]**

*If Y4 S1 is overloaded, move this block to the May 2028 bridge or June 2028; April is the Y4 S1 examination month.*

**Install and explore**

- [ ]  Get Ubuntu 26.04 (native, VM, or WSL2)
- [ ]  `sudo apt install ros-lyrical-desktop`; add `source /opt/ros/lyrical/setup.bash` to `~/.bashrc`
- [ ]  Confirm `echo $ROS_DISTRO` prints `lyrical`
- [ ]  Run `turtlesim` and `turtle_teleop_key`
- [ ]  Use `ros2 node list`, `ros2 topic list`, `ros2 topic echo`, `ros2 topic pub`, `ros2 service call`
- [ ]  Open `rqt_graph` and read the graph

**Write nodes**

- [ ]  Create a workspace `~/ros2_ws`; run `colcon build`; `source install/setup.bash`
- [ ]  Write a Python publisher and subscriber with `rclpy`
- [ ]  Write the same pair in C++ with `rclcpp`
- [ ]  Define a custom message (`SensorReading.msg`) and use it
- [ ]  Add a parameter and change it at runtime
- [ ]  Write a launch file that starts both nodes
- [ ]  Explain QoS: reliable vs best-effort, and which one a sensor stream should use

**Frames and simulation**

- [ ]  Publish a static transform; open `ros2 run tf2_tools view_frames`
- [ ]  Write a URDF for a 2-link robot; show it in RViz
- [ ]  Install `ros-lyrical-ros-gz`; run `gz sim` with a shapes world
- [ ]  Spawn a differential-drive robot; bridge `cmd_vel` with `ros_gz_bridge`; drive it with `teleop_twist_keyboard`
- [ ]  **Safe-stop node:** publish zero velocity when your sensor topic has been silent for 500 ms
- [ ]  **Proof:** kill the sensor publisher and watch the simulated robot stop

## I. Capstone Part 1 — see semester calendar above (~20 h, mostly university deliverables) **[M]**

- [ ]  Write the problem statement in 3 sentences
- [ ]  Name the users and the harm of a failure
- [ ]  Write 6–10 measurable requirements (number, unit, condition)
- [ ]  Failure-modes table: failure, effect, detection, response
- [ ]  Baseline: the simplest non-AI solution you will beat
- [ ]  Metrics: how you will decide the project worked
- [ ]  Architecture diagram: node → gateway → (optional) ROS 2 / model
- [ ]  Test strategy: unit, integration, end-to-end, fault injection
- [ ]  Risk list with one mitigation each
- [ ]  Ethics and safety paragraph: human oversight, privacy, limits *(IHM1301 tie-in)*
- [ ]  Justify AI in 5 sentences, or write "no AI needed" and why
- [ ]  Minimal simulation-first prototype that runs end to end once
- [ ]  Review the plan with your supervisor; record the feedback
- [ ]  Keep every hardware experiment low-voltage and supervised

## Semester alignment additions — Y4 S1

- [ ] **[M] [ADDED] November:** Start Capstone Part 1 block I now: confirm supervisor, proposal format, assessment rubric and approval dates; do not wait until March.
- [ ] **[M] [ADDED] November–December:** Review relevant literature, agree scope and baseline, and submit proposal/ethics material on the university schedule.
- [ ] **[M] [ADDED] November:** Draw the circuit and check voltage levels, current limits, pull-ups and shared ground before powering hardware; learn to verify voltage and continuity with a multimeter.
- [ ] **[M] [ADDED] December–February:** For CCS4353, document device identity, authentication, MQTT access rules and loss-of-network behavior; demonstrate one recovery test.
- [ ] **[M] [ADDED] November–March:** Complete CCS3440 and CCS4310 syllabus tasks beyond the selected search/PyTorch exercises; maintain a module assessment checklist for each.
- [ ] **[M] [ADDED] January–March:** For IHM1301, record stakeholders, foreseeable misuse, data consent/privacy, accessibility and human oversight where relevant to the capstone.
- [ ] **[M] [ADDED] February–March:** Confirm training placement, university approval, supervisor contacts, reporting format and start date; keep employer code and data separate unless reuse is permitted.
- [ ] **[M] [ADDED] March:** Review Part 1 evidence with the supervisor, record feedback and lock a feasible Part 2 scope before April exams.

## Exit gate — Y4 S1 **[M]**

- [ ]  Zephyr node runs on hardware; its tests pass; README and video exist
- [ ]  You can explain interrupt vs thread context, queue behavior, and one timing measurement from your own node
- [ ]  You can train, save, and evaluate a PyTorch model and explain overfitting using your own curves
- [ ]  A* and BFS/UCS implementations pass their tests
- [ ]  Capstone plan is approved, scoped, and measurable

---

# Y4 S2 — Robotics & Intelligent Machines Capstone *(Jun 2028 → Oct 2028 exams · 15 credits)*

| Module | Credits · type | Feeds the arc |
| --- | --- | --- |
| CCS4301 Capstone Project Part 2 | 3 · core | Implement, validate, report, demo |
| CCS4601 Industrial Training | 6 · core · non-GPA | Document real production practice |
| CCS4354 Tensors and Graphs (with programming) | 3 · elective | Tensors for ML/perception; graph algorithms for planning |
| SMA2305 Numerical Analysis | 3 · elective | Numerical stability, integration, filtering |

**Plan:** May bridge: start Integration (A) after the node/gateway prerequisites, and finish ROS basics (Y4 S1 H) before C. June–July: integration acceptance tests plus coursework B; begin D immediately. July–August: C only if selected and feasible, alongside capstone experiments. August–September: report, demo, portfolio and applications (D/E). October: final examinations, training/capstone submissions and corrections. A+D+E total about 110 h; B+C add about 65 h, excluding industrial training and university coursework.
**If ROS 2 basics are unfinished:** complete Y4 S1 H in the May bridge or June, before ROS integration (C).
**Re-check at semester start:** Zephyr, ROS 2, Gazebo, Nav2 docs.

---

## A. Integration — see semester calendar above (~40 h) **[M]**

**Repo and protocol**

- [ ]  One repo layout: `node/` (Zephyr), `gateway/` (C++), `tools/` (Python), `docs/`
- [ ]  Write the protocol document: frame layout, message table, version byte, one rule for compatibility
- [ ]  Add a protocol version check to both sides; reject unknown versions with a logged error

**Gateway**

- [ ]  Decode and validate frames; count good, bad-CRC, and dropped frames
- [ ]  Detect telemetry timeout; raise a `STALE` state
- [ ]  Reconnect to the serial port after unplug/replug without restarting
- [ ]  Log with levels and timestamps; expose counters (frames, errors, reconnects)
- [ ]  Run end to end on the PC: node on `native_sim` ↔ gateway over a host pseudo-terminal or TCP

**Fault injection**

- [ ]  Write the fault matrix (≥ 8 rows): sensor disconnect, corrupt frame, truncated frame, serial unplug, gateway crash and restart, slow consumer, queue overflow, node reset
- [ ]  For each row: expected response, how to inject it, how to check it
- [ ]  Script the injections in Python; run all; record pass/fail in a table

**Tests and CI**

- [ ]  Unit tests (node and gateway), integration tests, one end-to-end test
- [ ]  GitHub Actions: build gateway; run unit tests; build the Zephyr app for `native_sim`; run Twister; sanitizer job
- [ ]  Fix every CI failure; keep the badge green

**Profiling**

- [ ]  Latency: round-trip request/echo, 30 runs; report mean, standard deviation, 95th percentile; state how you handled clock differences
- [ ]  Memory: gateway resident memory over a 1-hour run; note any growth
- [ ]  Throughput: highest frame rate with zero loss
- [ ]  Write one paragraph on method and one on limitations

**Secure coding**

- [ ]  Check every length field before using it; list where you do it
- [ ]  Fuzz the parser (random bytes or `libFuzzer`) for at least 10 minutes with sanitizers on
- [ ]  Search the repo history for secrets; move configuration to ignored files
- [ ]  Pin dependency versions
- [ ]  Read the Zephyr MCUboot / firmware-update docs; sign one image with `imgtool`; explain rollback and confirm **[S]**

## B. Tensors, Graphs, Numerical Analysis — see semester calendar above (~15 h) **[S]**

*(University tie-in: CCS4354, SMA2305)*

- [ ]  NumPy: `reshape`, `transpose`, `einsum` on a 3-D array
- [ ]  State the broadcasting rule; make one broadcast bug and fix it
- [ ]  Repeat three operations in PyTorch; add a batch dimension
- [ ]  Graphs: adjacency list vs matrix; write BFS, DFS, and Dijkstra with `heapq`
- [ ]  Explain how Dijkstra relates to your A*
- [ ]  Floating point: print machine epsilon; compare two floats with a tolerance
- [ ]  Implement bisection and Newton's method; compare iterations
- [ ]  Implement the trapezoid rule and Simpson's rule; compare errors
- [ ]  Solve an ODE with Euler and with RK4 at the same step size; plot the errors
- [ ]  `np.linalg.solve` and `np.linalg.cond`; show an ill-conditioned system

## C. ROS 2 integration — see semester calendar above (~50 h) **[S]**

**Bridge**

- [ ]  Gateway publishes `SensorReading` and `NodeStatus` topics with `rclcpp`; choose QoS and write down why
- [ ]  Record a session with `ros2 bag record`; replay with `ros2 bag play`; run a test against the replay
- [ ]  Publish `diagnostic_msgs/DiagnosticStatus`; view it in `rqt`
- [ ]  Check the current status of the Zephyr–Zenoh bridge and micro-ROS; write a 5-line decision note (default: keep the gateway)

**Robot behavior in Gazebo**

- [ ]  Robot stops when the node reports `FAULT` or telemetry is stale
- [ ]  Robot resumes only after N consecutive good readings (hysteresis)
- [ ]  Connect your A* to a grid map; make the robot follow the path with a simple controller; record success over 10 runs
- [ ]  Or run the Nav2 quick-start in simulation; record success over 10 runs
- [ ]  Log time-to-stop after a fault; repeat 30 times; report mean and maximum

**State estimation**

- [ ]  Complementary filter for tilt from accelerometer + gyroscope
- [ ]  1-D Kalman filter for noisy position; compare with the raw signal
- [ ]  Compute RMSE against ground truth from the simulation

**Optional**

- [ ]  Read the `ros2_control` docs; explain controller manager, hardware interface, controller **[T]**
- [ ]  Use the TinyML model's output in the robot's decision, with the threshold fallback active **[T]**

## D. Capstone delivery — see semester calendar above (~40 h) **[M]**

- [ ]  Freeze scope: list what is MUST, SHOULD, IF TIME; set a freeze date; stop adding features after it
- [ ]  Write an acceptance test script that checks every requirement and prints a pass/fail table
- [ ]  Define each experiment: question, variables, number of runs, metric
- [ ]  Run each experiment 30 times; save raw data in the repo
- [ ]  Compare with the baseline from Capstone Part 1; plot the difference
- [ ]  Write the report sections: abstract · introduction · requirements · architecture · method · experiments · results · limitations · safety · conclusion · references
- [ ]  Write a limitations section that names what was **not** tested
- [ ]  Write the safety/reliability boundary: what the system must never do and what stops it
- [ ]  Demo script (5 minutes); rehearse twice; record a backup video
- [ ]  Test the README on a fresh clone on another machine; fix every missing step
- [ ]  Provide one command or script that runs the demo
- [ ]  Tag `v1.0`
- [ ]  *(Industrial Training tie-in)* list the practices you saw at work: code review, tickets, deployment, incident handling, testing; map each to your capstone workflow in the training report

## E. Portfolio and hiring — see semester calendar above (~30 h) **[M]**

**Portfolio (3 repos)**

- [ ]  Device Monitor (Python), Virtual Sensor Device (C++ + anomaly detector), Capstone — each has: one-line description, screenshot or video, build/run steps, tests, results table, limitations
- [ ]  Pin the 3 repos on your GitHub profile
- [ ]  Put work-related code in the portfolio only with written permission and no confidential data

**CV and profile**

- [ ]  Choose **one** target role: Embedded Software, Robotics Software, Embedded Linux, or Edge AI
- [ ]  One-page CV, projects first; each bullet follows "Built X with Y; measured Z"
- [ ]  List only skills you can defend in an interview
- [ ]  Update LinkedIn headline and GitHub README to match the target role

**Interview drills**

- [ ]  Implement a ring buffer from memory
- [ ]  Reverse a linked list from memory
- [ ]  Explain stack vs heap
- [ ]  Explain `volatile`, `const`, `static`
- [ ]  Explain RAII and why it prevents leaks
- [ ]  Explain mutex vs semaphore and priority inversion
- [ ]  Explain interrupts vs polling
- [ ]  Compare UART, I2C, SPI, CAN
- [ ]  Read a hex dump of a frame and find length, payload, CRC
- [ ]  Debug a segfault live with GDB
- [ ]  Find which process owns a TCP port on Linux
- [ ]  Explain your capstone in 2 minutes and in 10 minutes
- [ ]  Prepare 3 stories: a bug you found, a trade-off you made, a failure you recovered from
- [ ]  Do 3 mock interviews with a friend or recorded self-review

**Applications**

- [ ]  Build a shortlist of 15 roles
- [ ]  Check official career pages: Vega Innovations, Zone24x7, Iconic Devices / NORVI, Synopsys, Bosch, Siemens, ABB, NVIDIA; verify eligibility
- [ ]  Keep a tracking table: company, role, date, contact, status
- [ ]  Tailor the CV to each posting's top 5 requirements
- [ ]  Send at least 10 applications; follow up once after 2 weeks
- [ ]  Rust: finish one beginner embedded Rust tutorial for your board family; write 5 sentences comparing it with C **[T]**

## Semester alignment additions — Y4 S2

- [ ] **[M] [ADDED] Before placement:** Confirm CCS4601 attendance, logbook, supervision, assessment and confidentiality requirements; record the actual training period rather than assuming June–October.
- [ ] **[M] [ADDED] Weekly during training:** Update the logbook with work, learning, hours and supervisor sign-off as required; track report and evaluation deadlines.
- [ ] **[M] [ADDED] June:** Agree capstone milestones with the supervisor around placement hours; schedule recurring reviews and reserve reporting time from the start.
- [ ] **[M] [ADDED] June–September:** Maintain full CCS4354/SMA2305 syllabus checklists; the existing B exercises are supplementary and follow the actual teaching order.
- [ ] **[M] [ADDED] Before TinyML deployment:** Verify operators, model conversion, quantization, memory and runtime support for the exact board; the original CPU-only runtime rule is insufficient.
- [ ] **[M] [ADDED] Before experiments:** Define units, calibration, sampling rate, sample size and success criteria. Use the retained 30-run tasks as initial targets; justify repetition counts and variability with your supervisor.
- [ ] **[M] [ADDED] August–September:** Freeze features, complete acceptance tests and save raw results; give the supervisor a complete report draft before the agreed review deadline.
- [ ] **[M] [ADDED] October:** Complete final exams, viva/demo, capstone corrections and training submissions according to actual university dates; archive final submission receipts.
- [ ] **[S] [ADDED] After core submissions:** Finish deferred TinyML, ROS, Yocto or other optional boxes in a separately dated continuation plan; retain all unfinished boxes.

## Exit gate — Y4 S2 **[M]**

- [ ]  Capstone meets its acceptance criteria and a stranger can reproduce the demo from the README
- [ ]  Three portfolio repos are public, tested, and documented
- [ ]  CV is focused on one role and at least 10 applications are sent
- [ ]  Training report and capstone report are submitted

---

# Weekly rhythm (every semester)

- [ ]  **Session 1 (build):** one box-group from the current block, typed by hand, no copy-paste
- [ ]  **Session 2 (build):** continue the same block; finish its exercise
- [ ]  **Session 3 (apply):** use the topic in the current project (sensor records, log parsing, device logic)
- [ ]  **Session 4 (review, 30–45 min):** explain the topic aloud; fix one failing test; commit and push
- [ ]  **Weekly check:** tick only boxes you could redo without notes; leave the rest open
- [ ]  **Exam weeks:** keep only Session 4; resume where you stopped

# When you fall behind

- Do not skip a **[M]** block. Defer **[T]**, then **[S]**, in that order; retain every checkbox in a dated backlog. Mandatory university assessments remain required regardless of a roadmap priority tag.
- Behind by more than 2 weeks at the end of a block: cut the block's repeat exercises, keep the **Proof** box.
- Y4 S1 overload order: `[T]` → ROS 2 basics (move to Y4 S2) → Embedded Linux → TinyML.
- A box you cannot finish in 3 sessions: write down exactly where you got stuck, then look it up or ask.

# Market notes (directional — verify against live postings)

- Demand centers on **embedded Linux, Zephyr, C++**; Rust is a differentiator, not a baseline
- Few postings target juniors and most are onsite → **tested, reproducible projects are your proof**
- Original source claim: recruiter and job-board reports (mid-2026), not official statistics; not independently verified in this revision

# References

- 30 Days of Python: https://github.com/Asabeneh/30-Days-Of-Python · Python docs: https://docs.python.org/3/
- Beej's Guide to C: https://beej.us/guide/bgc/
- Learn C++: https://www.learncpp.com/ · C++ reference: https://en.cppreference.com/
- CMake: https://cmake.org/cmake/help/latest/guide/tutorial/ · GDB: https://www.gnu.org/software/gdb/documentation/
- GoogleTest: https://google.github.io/googletest/
- Zephyr: https://docs.zephyrproject.org/latest/ · Yocto: https://docs.yoctoproject.org/
- ROS 2: https://docs.ros.org/ · Gazebo: https://gazebosim.org/ · Nav2: https://docs.nav2.org/
- scikit-learn: https://scikit-learn.org/stable/ · PyTorch: https://pytorch.org/docs/ · ExecuTorch: https://pytorch.org/executorch/