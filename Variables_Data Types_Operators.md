# Variables, Data Types, and Operators

This document provides a detailed explanation of **Variables**, **Data Types**, and **Operators** in programming (with examples in Python). These are the fundamental building blocks of any programming language.

---

## 1. Variables

A **variable** is a named storage location used to hold data. It acts as a container for values.

### Characteristics of Variables

* Must have a unique name (identifier).
* Can store different data types (numbers, strings, lists, etc.).
* Value can be changed during program execution.

### Rules for Naming Variables

1. Must start with a letter or underscore (`_`).
2. Cannot start with a number.
3. Can contain letters, numbers, and underscores.
4. Case-sensitive (`age` and `Age` are different).

### Example

```python
x = 10        # integer variable
name = "John" # string variable
pi = 3.14     # float variable
is_active = True # boolean variable
```

---

## 2. Data Types

Data types specify the type of data a variable can hold.

### Common Data Types in Python

#### 2.1 Numeric Types

* **int** → Whole numbers (e.g., `10`, `-5`)
* **float** → Decimal numbers (e.g., `3.14`, `-0.99`)
* **complex** → Numbers with real and imaginary parts (e.g., `2 + 3j`)

#### 2.2 Sequence Types

* **str** → String of characters (e.g., `'hello'`)
* **list** → Ordered, mutable collection (e.g., `[1, 2, 3]`)
* **tuple** → Ordered, immutable collection (e.g., `(1, 2, 3)`)

#### 2.3 Set Types

* **set** → Unordered, unique collection (e.g., `{1, 2, 3}`)
* **frozenset** → Immutable set

#### 2.4 Mapping Type

* **dict** → Key-value pairs (e.g., `{"name": "John", "age": 25}`)

#### 2.5 Boolean Type

* **bool** → True or False values

#### 2.6 None Type

* **None** → Represents absence of value

### Example

```python
age = 25              # int
height = 5.9          # float
message = "Hello"     # str
numbers = [1, 2, 3]   # list
person = {"name": "Ava", "age": 22} # dict
unique = {1, 2, 2, 3} # set → {1, 2, 3}
```

---

## 3. Operators

Operators are symbols that perform operations on variables and values.

### Types of Operators

#### 3.1 Arithmetic Operators

Used for mathematical operations.

| Operator | Description         | Example       |
| -------- | ------------------- | ------------- |
| `+`      | Addition            | `5 + 3 = 8`   |
| `-`      | Subtraction         | `5 - 3 = 2`   |
| `*`      | Multiplication      | `5 * 3 = 15`  |
| `/`      | Division            | `5 / 2 = 2.5` |
| `//`     | Floor Division      | `5 // 2 = 2`  |
| `%`      | Modulus (remainder) | `5 % 2 = 1`   |
| `**`     | Exponentiation      | `2 ** 3 = 8`  |

#### 3.2 Comparison Operators

Used to compare values (returns `True` or `False`).

| Operator | Description           | Example          |
| -------- | --------------------- | ---------------- |
| `==`     | Equal to              | `5 == 5 → True`  |
| `!=`     | Not equal             | `5 != 3 → True`  |
| `>`      | Greater than          | `5 > 3 → True`   |
| `<`      | Less than             | `5 < 3 → False`  |
| `>=`     | Greater than or equal | `5 >= 5 → True`  |
| `<=`     | Less than or equal    | `5 <= 3 → False` |

#### 3.3 Logical Operators

Used to combine conditional statements.

| Operator | Description                            | Example                    |
| -------- | -------------------------------------- | -------------------------- |
| `and`    | True if both conditions are True       | `(5 > 3 and 2 < 4) → True` |
| `or`     | True if at least one condition is True | `(5 > 3 or 2 > 4) → True`  |
| `not`    | Reverses result                        | `not (5 > 3) → False`      |

#### 3.4 Assignment Operators

Used to assign values.

| Operator | Example   | Equivalent to |
| -------- | --------- | ------------- |
| `=`      | `x = 5`   | Assigns value |
| `+=`     | `x += 3`  | `x = x + 3`   |
| `-=`     | `x -= 2`  | `x = x - 2`   |
| `*=`     | `x *= 2`  | `x = x * 2`   |
| `/=`     | `x /= 2`  | `x = x / 2`   |
| `//=`    | `x //= 2` | `x = x // 2`  |
| `%=`     | `x %= 2`  | `x = x % 2`   |
| `**=`    | `x **= 3` | `x = x ** 3`  |

#### 3.5 Bitwise Operators

Used for bit-level operations.

| Operator | Description | Example       |     |         |
| -------- | ----------- | ------------- | --- | ------- |
| `&`      | AND         | `5 & 3 → 1`   |     |         |
| \`       | \`          | OR            | \`5 | 3 → 7\` |
| `^`      | XOR         | `5 ^ 3 → 6`   |     |         |
| `~`      | NOT         | `~5 → -6`     |     |         |
| `<<`     | Left Shift  | `5 << 1 → 10` |     |         |
| `>>`     | Right Shift | `5 >> 1 → 2`  |     |         |

#### 3.6 Membership Operators

| Operator | Description                              | Example                     |
| -------- | ---------------------------------------- | --------------------------- |
| `in`     | Returns True if value is in sequence     | `"a" in "apple" → True`     |
| `not in` | Returns True if value is not in sequence | `"x" not in "apple" → True` |

#### 3.7 Identity Operators

| Operator | Description                               | Example      |
| -------- | ----------------------------------------- | ------------ |
| `is`     | Returns True if both refer to same object | `x is y`     |
| `is not` | Returns True if not same object           | `x is not y` |

---

## 4. Summary

* **Variables** store data.
* **Data Types** define the type of data.
* **Operators** perform operations on data.

These three concepts are the foundation of programming and are essential for building any software application