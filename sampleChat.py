# Python program to demonstrate all types of operators using match-case

a = int(input("Enter 1st number: "))
b = int(input("Enter 2nd number: "))

op = -1  # initialize to a non-zero value

while op != 0:
    print(
        "\nChoose your option:\n"
        "1 → Arithmetic\n"
        "2 → Logical\n"
        "3 → Conditional (Ternary)\n"
        "4 → Bitwise\n"
        "5 → Relational\n"
        "6 → Membership\n"
        "7 → Identity\n"
        "0 → Exit"
    )

    op = int(input("Enter your choice: "))

    match op:
        case 1:  # Arithmetic
            print("Arithmetic Operators ------>")
            print(f"a + b = {a + b}")
            print(f"a - b = {a - b}")
            print(f"a * b = {a * b}")
            print(f"a / b = {a / b}")
            print(f"a // b = {a // b}")
            print(f"a % b = {a % b}")
            print(f"a ** b = {a ** b}")

        case 2:  # Logical
            print("Logical Operators ------>")
            print(f"a and b = {a and b}")
            print(f"a or b = {a or b}")
            print(f"not a = {not a}")
            print(f"not b = {not b}")

        case 3:  # Conditional (Ternary)
            print("Conditional (Ternary) Operator ------>")
            bigger = a if a > b else b
            print(f"Bigger number is: {bigger}")
            smaller = a if a < b else b
            print(f"Smaller number is: {smaller}")

        case 4:  # Bitwise
            print("Bitwise Operators ------>")
            print(f"a & b = {a & b}")
            print(f"a | b = {a | b}")
            print(f"a ^ b = {a ^ b}")
            print(f"~a = {~a}")
            print(f"a << 1 = {a << 1}")
            print(f"a >> 1 = {a >> 1}")

        case 5:  # Relational
            print("Relational Operators ------>")
            print(f"a == b → {a == b}")
            print(f"a != b → {a != b}")
            print(f"a > b → {a > b}")
            print(f"a < b → {a < b}")
            print(f"a >= b → {a >= b}")
            print(f"a <= b → {a <= b}")

        case 6:  # Membership
            print("Membership Operators ------>")
            list1 = [a, b, 10, 20]
            print(f"a in list1 → {a in list1}")
            print(f"b not in list1 → {b not in list1}")

        case 7:  # Identity
            print("Identity Operators ------>")
            x = a
            y = b
            print(f"a is x → {a is x}")
            print(f"a is not b → {a is not b}")
            print(f"id(a) = {id(a)}, id(b) = {id(b)}")

        case 0:
            print("Exiting the program...")

        case _:
            print("Invalid choice!")


print("types of datastructures in python -------------->")
# List example (mutable, allows duplicates)
fruits = ["apple", "banana", "cherry"]
fruits.append("mango")  # Add an item
fruits[1] = "grapes"    # Change item
print("List:", fruits)

# Tuple example (immutable, allows duplicates)
colors = ("red", "green", "blue", "red")
print("Tuple:", colors)
print("First color:", colors[0])

# Dictionary example (key-value pairs)
student = {
    "name": "Sravani",
    "age": 15,
    "grade": "10th"
}
student["age"] = 16  # Update value
student["city"] = "Hyderabad"  # Add new key-value
print("Dictionary:", student)

# Set example (unordered, no duplicates)
numbers = {1, 2, 3, 3, 4}
numbers.add(5)  # Add element
numbers.remove(2)  # Remove element
print("Set:", numbers)
