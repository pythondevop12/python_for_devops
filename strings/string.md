# 🐍 Python Topic 3: Strings

## 📌 What is a String?

A **string** in Python is a sequence of characters enclosed in single, double, or triple quotes.

```python
name = 'Amit'
greeting = "Hello"
paragraph = """This is a multi-line string."""
```

---

## 🔢 String Indexing and Slicing

### Indexing
Access characters by position (starting from 0).

```python
text = "Python"
print(text[0])  # P
print(text[-1]) # n
```

### Slicing
Extract parts of a string.

```python
print(text[0:2])   # Py
print(text[2:])    # thon
print(text[:4])    # Pyth
```

---

## 🧰 Common String Methods

```python
message = "hello world"
print(message.upper())      # HELLO WORLD
print(message.lower())      # hello world
print(message.title())      # Hello World
print(message.capitalize()) # Hello world
print(message.strip())      # removes leading/trailing spaces
print(message.replace("world", "Python")) # hello Python
print(message.find("world")) # returns index
```

---

## 🔗 String Concatenation and Repetition

```python
first = "Hello"
second = "Amit"
combined = first + " " + second
print(combined)  # Hello Amit

repeat = "Hi! " * 3
print(repeat)    # Hi! Hi! Hi!
```

---

## 🧮 String Formatting

### Using `f-strings`
```python
name = "Amit"
age = 30
print(f"My name is {name} and I am {age} years old.")
```

### Using `format()`
```python
print("My name is {} and I am {} years old.".format(name, age))
```

---

## ✅ Summary Table

| Operation         | Syntax / Method              | Description                          |
|------------------|------------------------------|--------------------------------------|
| Indexing         | `text[0]`                    | Access character at index            |
| Slicing          | `text[1:4]`                  | Extract substring                    |
| Concatenation    | `str1 + str2`                | Combine strings                      |
| Repetition       | `str * n`                    | Repeat string                        |
| Uppercase        | `text.upper()`               | Convert to uppercase                 |
| Lowercase        | `text.lower()`               | Convert to lowercase                 |
| Replace          | `text.replace(a, b)`         | Replace substring                    |
| Find             | `text.find(sub)`             | Find index of substring              |
| Strip            | `text.strip()`               | Remove whitespace                    |
| Format           | `f"{var}"` or `format()`      | Insert variables into string         |

---

## 🧪 Quick Practice

```python
# Reverse a string
text = "Python"
print(text[::-1])  # nohtyP

# Count vowels in a string
vowels = "aeiou"
word = "education"
count = sum(1 for char in word if char in vowels)
print(count)  # 5
```

---
