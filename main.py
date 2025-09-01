# main.py

import calculator

def main():
    print("Simple Calculator")
    a = float(input("Enter first number: "))
    b = float(input("Enter second number: "))
    op = input("Choose operation (+, -, *, /): ")

    if op == "+":
        result = calculator.add(a, b)
    elif op == "-":
        result = calculator.subtract(a, b)
    elif op == "*":
        result = calculator.multiply(a, b)
    elif op == "/":
        try:
            result = calculator.divide(a, b)
        except ValueError as e:
            print("Error:", e)
            return
    else:
        print("Invalid operation")
        return

    print(f"Result: {result}")

if __name__ == "__main__":
    main()
