def my_function(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        print("Error: Division by zero")
        return None

result = my_function(10, 0)
print(result)  # Output: Error: Division by zero
None
result = my_function(10,2)
print(result) # Output 5.0