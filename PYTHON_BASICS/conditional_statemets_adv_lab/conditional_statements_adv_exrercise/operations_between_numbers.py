n1 = int(input())
n2 = int(input())
operator = input()

result = 0

if operator == "+":
    result = n1 + n2
    even_or_odd = result % 2
    if even_or_odd == 0:
        print(f"{n1} {operator} {n2} = {result} - even")
    else:
        print(f"{n1} {operator} {n2} = {result} - odd")
elif operator == "-":
    result = n1 - n2
    even_or_odd = result % 2
    if even_or_odd == 0:
        print(f"{n1} {operator} {n2} = {result} - even")
    else:
        print(f"{n1} {operator} {n2} = {result} - odd")
elif operator == "*":
    result = n1 * n2
    even_or_odd = result % 2
    if even_or_odd == 0:
        print(f"{n1} {operator} {n2} = {result} - even")
    else:
        print(f"{n1} {operator} {n2} = {result} - odd")

if operator == "/" and n2 == 0:
    print(f"Cannot divide {n1} by zero")
elif operator == "/" and n2 != 0:
    result = n1 / n2
    print(f"{n1} {operator} {n2} = {result:.2f}")

if operator == "%" and n2 == 0:
    print(f"Cannot divide {n1} by zero")
elif operator == "%" and n2 != 0:
    result = n1 % n2
    print(f"{n1} {operator} {n2} = {result}")