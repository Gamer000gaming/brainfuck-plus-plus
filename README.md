# BF++ Language Specification

**BF++** is a minimalistic, single-character esolang that extends [Brainfuck](https://esolangs.org/wiki/Brainfuck) with extra instructions for clarity, usability, and power — without sacrificing simplicity.

## Instruction Set

### Original Brainfuck Instructions

| Symbol | Function |
|--------|----------|
| `>`    | Move pointer right |
| `<`    | Move pointer left |
| `+`    | Increment current cell |
| `-`    | Decrement current cell |
| `.`    | Output current cell as ASCII |
| `,`    | Input one ASCII character into current cell |
| `[`    | Jump forward past matching `]` if current cell == 0 |
| `]`    | Jump backward to matching `[` if current cell ≠ 0 |

---

### BF++ Extended Instructions

| Symbol | Function |
|--------|----------|
| `^`    | Copy current cell value to clipboard |
| `v`    | Paste clipboard value into current cell (overwrite) |
| `#`    | Set current cell to 0 |
| `&`    | End execution (halt program) |
| `(`    | Jump forward past matching `)` if current cell ≠ 0 |
| `)`    | Does nothing — used for `(` pairing |
| `:`    | Print current cell as an integer |
| `;`    | Input an integer into current cell |
| `*`    | Add clipboard value to current cell (`cell += clipboard`) |
| `/`    | Subtract clipboard value from current cell (`cell -= clipboard`) |
| `!`    | Debug: print current tape with pointer shown as `[value]` |

---

## Syntax Features

### Comments

Use `@` to comment the rest of a line:

```bfpp
+>++<@ This moves, adds, and comments
```

Only the code before `@` is executed.

---

### `times` Syntax (Macro Expansion)

You can repeat any sequence using:

```
times N, "<sequence>"
```

**Example:**

```
times 10, ">"  @ Expands to >>>>>>>>>>>
times 3, "+:"  @ Expands to +:+:+:
```

- Must be on its own line
- Quotes `"` required
- Supports multiple-character sequences

---

## Notes

- Clipboard acts like a register — not part of tape
- All math is 8-bit unsigned (0–255) with wraparound
- `!` stops printing after pointer if rest of tape is 0
- Minimal addition: `;^;*:` (5 characters)

---

## Interpreter Usage (Python)

```python
run_bfpp_live(program_text)
```

- Input handled via `input()` or passed-in function
- Output prints directly to console
- `preprocess_bfpp()` expands `times` and strips `@` comments

---

## Author Notes

BF++ is:
- Fully compatible with classic Brainfuck (any BF++ code can be converted to originla Brainfuck code)
- Just as powerful (Turing-complete)
- Much easier to read and use
