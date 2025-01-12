def calculate_average(numbers):
    if not numbers:
        return 0  # Handle empty list
    return sum(numbers) / len(numbers)

# Incorrect usage leading to a ZeroDivisionError
average = calculate_average([])