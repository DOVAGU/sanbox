"""
CP1404/CP5632 - Practical
Answer the following questions:
1. When will a ValueError occur?（if the user inputs a non-integer value, a ValueError will occur.）
2. When will a ZeroDivisionError occur?（A ZeroDivisionError will occur when the denominator entered by the user is zero.）
3. Could you change the code to avoid the possibility of a ZeroDivisionError?
"""

try:
    numerator = int(input("Enter the numerator: "))
    denominator = int(input("Enter the denominator: "))
    if denominator == 0:
        raise ZeroDivisionError("Cannot divide by zero!")
    fraction = numerator / denominator
    print(fraction)
except ValueError:
    print("Numerator and denominator must be valid numbers!")
except ZeroDivisionError as error:
    print(error)
print("Finished.")

