# 🐍 Python Topic 1: Variables and Data Types

## 📌 What is a Variable?

A **variable** in Python is a name that refers to a value stored in memory. You can think of it as a container for data.

```python
name = "Amit"
age = 30
is_lead = True
```

## 🧠 Rules for Naming Variables

- Must start with a letter or underscore (`_`)
- Cannot start with a number
- Can contain letters, numbers, and underscores
- Case-sensitive (`Age` and `age` are different)

---

## 🧮 Data Types in Python

Python has several built-in data types. Here are the most common ones:

### 1. Numeric Types
- `int`: Integer numbers  
  ```python
  x = 10
  ```
- `float`: Decimal numbers  
  ```python
  pi = 3.14
  ```
- `complex`: Complex numbers  
  ```python
  z = 2 + 3j
  ```

### 2. Text Type
- `str`: String of characters  
  ```python
  greeting = "Hello, Amit!"
  ```

### 3. Boolean Type
- `bool`: True or False  
  ```python
  is_active = True
  ```

### 4. Sequence Types
- `list`: Ordered, mutable collection  
  ```python
  fruits = ["apple", "banana", "cherry"]
  ```
- `tuple`: Ordered, immutable collection  
  ```python
  coordinates = (10.0, 20.0)
  ```
- `range`: Sequence of numbers  
  ```python
  numbers = range(5)
  ```

### 5. Mapping Type
- `dict`: Key-value pairs  
  ```python
  employee = {"name": "Amit", "role": "Technical Lead"}
  ```

### 6. Set Types
- `set`: Unordered collection of unique items  
  ```python
  skills = {"Python", "Java", "SQL"}
  ```
- `frozenset`: Immutable version of a set  
  ```python
  frozen_skills = frozenset(["Python", "Java"])
  ```

---

## 🔍 Type Checking

Use `type()` to check the data type of a variable:

```python
print(type(name))      # <class 'str'>
print(type(age))       # <class 'int'>
print(type(is_lead))   # <class 'bool'>
```

---

## ✅ Summary Table

| Data Type   | Example         | Description                     |
|-------------|-----------------|---------------------------------|
| `int`       | `42`            | Whole numbers                   |
| `float`     | `3.14`          | Decimal numbers                 |
| `str`       | `"Hello"`       | Text                            |
| `bool`      | `True` / `False`| Logical values                  |
| `list`      | `[1, 2, 3]`     | Ordered, changeable collection  |
| `tuple`     | `(1, 2, 3)`     | Ordered, unchangeable collection|
| `dict`      | `{"a": 1}`      | Key-value pairs                 |
| `set`       | `{1, 2, 3}`     | Unique unordered items          |
| `frozenset` | `frozenset([1])`| Immutable set                   |

---

## 🧪 Quick Practice

```python
# Declare variables
language = "Python"
version = 3.11
is_fun = True

# Check types
print(type(language))  # str
print(type(version))   # float
print(type(is_fun))    # bool
```

---
