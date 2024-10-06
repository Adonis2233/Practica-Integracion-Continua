def sum(a, b):
    return a + b

try:
    a = int(input('Enter 1st number: '))
    b = int(input('Enter 2nd number: '))

    print(f'Sum of {a} and {b} is {sum(a, b)}')

except ValueError:
    print("Invalid input. Please enter valid integers.")
