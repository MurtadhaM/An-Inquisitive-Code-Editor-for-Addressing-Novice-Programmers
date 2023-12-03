# Common Misconceptions & Mistakes in Python
# ==========================================
1. **Misunderstanding of language-specific behavior**: In Python, the `is` operator checks for identity, not equality. This can lead to unexpected results:
    
```python

a = [1, 2, 3]
    b = [1, 2, 3]
    print(a == b)  # True
    print(a is b)  # False
```

2. **Off-by-one errors**: These often occur in loops or when working with ranges:

```python
for i in range(10):  # This loop runs 10 times, not 9
        print(i)
```

3. **Mutability misconceptions**: Lists are mutable, while tuples are not:

```python
a = [1, 2, 3]
    a[0] = 10  # This is fine

    b = (1, 2, 3)
    b[0] = 10  # This raises a TypeError
```

4. **Ignoring error return values**: Python functions often raise exceptions instead of returning error values, but these should not be ignored:

```python
try:
    x = int("not a number")  # Raises ValueError
except ValueError:
    pass  # Ignoring the error can lead to problems later
```

5. **Memory management mistakes**: Python handles memory management automatically, but holding onto large amounts of data can still cause problems:
```python
a = [0] * 10**8  # This list takes up a lot of memory
```

6. **Concurrency issues**: Python's Global Interpreter Lock (GIL) prevents true parallelism in threads, but race conditions can still occur:

```python
import threading

    counter = 0

    def increment_counter():
    global counter
        for _ in range(1000000):
        counter += 1  # This is not thread-safe

    t1 = threading.Thread(target=increment_counter)
    t2 = threading.Thread(target=increment_counter)

    t1.start()
    t2.start()

    t1.join()
    t2.join()

    print(counter)  # Likely not 2000000
```

7. **SQL Injection**: Always use parameterized queries or prepared statements to prevent SQL injection:

```python
import sqlite3

    # NEVER do this
    user_id = "1; DROP TABLE users;"
    cursor.execute(f"SELECT * FROM users WHERE id = {user_id}")

    # Instead, do this
    user_id = 1
    cursor.execute("SELECT * FROM users WHERE id = ?", (user_id,))
```

8. **Hardcoding values**: Avoid hardcoding values that might change:

```python
tax_rate = 0.2  # Instead, consider loading this from a config file or environment variable
```

9. **Not understanding the difference between deep and shallow copying**: Shallow copies share references with the original object, while deep copies do not:

```python
import copy

    a = [[1, 2, 3], [4, 5, 6]]
    b = copy.copy(a)  # Shallow copy
    c = copy.deepcopy(a)  # Deep copy

    a[0][0] = 10

    print(b)  # [[10, 2, 3], [4, 5, 6]]
    print(c)  # [[1, 2, 3], [4, 5, 6]]
```

10. **Not writing tests or ignoring failing tests**: Always write tests for your code and pay attention when they fail:

```python
def test_addition():
    assert 1 + 1 == 2  # This test should pass

    def test_subtraction():
    assert 1 - 1 == 1  # This test should fail
```
