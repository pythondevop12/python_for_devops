# Conditional Statements, Loops, Loop Control, and Comprehensions in Python

This document provides a detailed explanation of **Conditional Statements**, **Loops**, **Loop Control**, and **Comprehensions** in Python with examples.

---

## 1. Conditional Statements

Conditional statements allow decision-making in programs by executing code blocks based on conditions.

### Syntax

```python
if condition:
    # code to execute if condition is True
elif another_condition:
    # code to execute if this condition is True
else:
    # code to execute if all conditions are False
```

### Example

```python
x = 10

if x > 0:
    print("Positive number")
elif x == 0:
    print("Zero")
else:
    print("Negative number")
```

---

## 2. Loops

Loops are used to repeat a block of code multiple times.

### 2.1 `for` Loop

Iterates over a sequence (list, tuple, string, range, etc.).

```python
for i in range(5):
    print(i)
```

Output:

```
0
1
2
3
4
```

#### Iterating over a list

```python
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)
```

### 2.2 `while` Loop

Executes as long as the condition is True.

```python
count = 0
while count < 5:
    print("Count:", count)
    count += 1
```

---

## 3. Loop Control Statements

Python provides statements to alter loop execution.

### 3.1 `break`

Exits the loop immediately.

```python
for i in range(10):
    if i == 5:
        break
    print(i)
```

Output:

```
0
1
2
3
4
```

### 3.2 `continue`

Skips the current iteration and moves to the next.

```python
for i in range(5):
    if i == 2:
        continue
    print(i)
```

Output:

```
0
1
3
4
```

### 3.3 `pass`

Acts as a placeholder; does nothing.

```python
for i in range(3):
    if i == 1:
        pass  # Placeholder for future code
    print(i)
```

Output:

```
0
1
2
```

---

## 4. Comprehensions

Comprehensions provide a concise way to create collections.

### 4.1 List Comprehension

Creates a new list in a single line.

```python
squares = [x**2 for x in range(6)]
print(squares)
```

Output:

```
[0, 1, 4, 9, 16, 25]
```

### 4.2 Dictionary Comprehension

Creates dictionaries dynamically.

```python
numbers = {x: x**2 for x in range(5)}
print(numbers)
```

Output:

```
{0: 0, 1: 1, 2: 4, 3: 9, 4: 16}
```

### 4.3 Set Comprehension

Creates a set with unique values.

```python
unique = {x % 3 for x in range(10)}
print(unique)
```

Output:

```
{0, 1, 2}
```

### 4.4 Conditional Comprehensions

Adding conditions inside comprehensions.

```python
even_squares = [x**2 for x in range(10) if x % 2 == 0]
print(even_squares)
```

Output:

```
[0, 4, 16, 36, 64]
```

---

## 5. Summary

* **Conditional statements** (`if`, `elif`, `else`) allow decision-making.
* **Loops** (`for`, `while`) execute blocks repeatedly.
* **Loop control** (`break`, `continue`, `pass`) modify loop execution.
* **Comprehensions** (list, dict, set) provide a concise way to create collections.

---

✅ You can **copy** this content directly or download it as a `.md` file.
