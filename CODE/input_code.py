"""
A List of functions that contain common mistakes in Python code
"""
import threading
import copy
# 1. Misunderstanding of Language-Specific Behavior
def language_specific_behavior_mistake():
    result = "5" + 5
    return result
# 2. Off-by-One Errors
def off_by_one_error():
    my_list = [1, 2, 3, 4, 5]
    for i in range(6):
        print(my_list[i])
# 3. Mutability Misconceptions
def mutability_mistake():
    my_list = [1, 2, 3]
    my_list.append(4)
    my_tuple = (1, 2, 3)
    my_tuple[0] = 0  # This will raise an error
# 4. Ignoring Error Return Values
def ignoring_error_return_values():
    try:
        result = int("abc")
    except ValueError:
        pass  # Error is ignored
# 5. Memory Management Mistakes
def memory_management_mistake():
    while True:
        data = " " * (1024 ** 2)  # Allocating a large amount of memory in a loop
# 6. Concurrency Issues
counter = 0
def increment_counter():
    global counter
    for _ in range(1000000):
        counter += 1
def concurrency_issue():
    thread1 = threading.Thread(target=increment_counter)
    thread2 = threading.Thread(target=increment_counter)
    thread1.start()
    thread2.start()
    thread1.join()
    thread2.join()
    print("Counter:", counter)
# 7. SQL Injection
def sql_injection():
    user_input = "admin'; DROP TABLE users--"
    query = f"SELECT * FROM users WHERE username='{user_input}'"
    # Execute query with user input
# 8. Hardcoding Values
def hardcoding_values():
    def calculate_area(radius):
        pi = 3.14  # Hardcoded value
        return pi * radius ** 2
# 9. Not Understanding the Difference Between Deep and Shallow Copying
def not_understanding_copy():
    original_list = [[1, 2, 3], [4, 5, 6]]
    shallow_copy = copy.copy(original_list)
    deep_copy = copy.deepcopy(original_list)
    original_list[0][0] = 0  # This will affect both shallow_copy and deep_copy
# 10. Not Writing Tests or Ignoring Failing Tests
def not_writing_tests():
    def divide(a, b):
        return a / b  # No error handling or tests for division by zero
    result = divide(5, 0)
    return result
