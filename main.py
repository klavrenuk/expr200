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
