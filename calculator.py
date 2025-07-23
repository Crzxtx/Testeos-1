"""Simple command-line calculator."""

def add(x, y):
    return x + y


def subtract(x, y):
    return x - y


def multiply(x, y):
    return x * y


def divide(x, y):
    if y == 0:
        raise ZeroDivisionError("Cannot divide by zero")
    return x / y


def main():
    print("Basic Calculator")
    try:
        x = float(input("Enter first number: "))
        y = float(input("Enter second number: "))
        op = input("Enter operation (+, -, *, /): ").strip()
    except ValueError:
        print("Invalid input. Please enter numeric values.")
        return

    if op == '+':
        result = add(x, y)
    elif op == '-':
        result = subtract(x, y)
    elif op == '*':
        result = multiply(x, y)
    elif op == '/':
        try:
            result = divide(x, y)
        except ZeroDivisionError as e:
            print(e)
            return
    else:
        print("Invalid operation")
        return

    print(f"Result: {result}")


if __name__ == "__main__":
    main()
