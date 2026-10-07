# expr200

Test task: insert `+`, `-` or nothing between digits `9876543210` (in this order) so that the expression equals `200`.

## Solution

The program enumerates all `3^9 = 19683` operator combinations with `itertools.product` and evaluates each expression with a simple left-to-right parser instead of `eval` — merged numbers like `210` are accumulated digit by digit.

```python
from itertools import product

DIGITS = "9876543210"


def evaluate(expr):
    total = 0
    num = 0
    sign = 1
    for ch in expr:
        if ch.isdigit():
            num = num * 10 + int(ch)
        else:
            total += sign * num
            sign = 1 if ch == "+" else -1
            num = 0
    return total + sign * num


def main():
    found = []
    for parts in product(("+", "-", ""), repeat=9):
        expr = DIGITS[0]
        for d, op in zip(DIGITS[1:], parts):
            expr += op + d
        if evaluate(expr) == 200:
            found.append(expr)

    for e in found:
        print(f"{e}=200")
    print("total:", len(found))


if __name__ == "__main__":
    main()
```

## Run

```bash
python main.py
```

## Output

```
9-8+7-6-5-4-3+210=200
9-8-7-6-5+4+3+210=200
98+76-5+43-2-10=200
98-7+65+43+2-1+0=200
98-7+65+43+2-1-0=200
total: 5
```

No dependencies, Python 3.8+.
