

---

# 📅 Week 1: Getting Started with Python

Welcome to Week 1 of your Python journey! 🎉
This week, you’ll set up your environment, write your first program, and explore Python basics: **comments, strings, variables, arithmetic operations, and built-in functions.**

---

## 1. ✨ What is Programming?

Programming is the process of writing instructions for a computer to follow.
Python is simple, powerful, and widely used in **web development, data science, AI, and automation.**

---

## 2. ⚙️ Installing Python

1. Download Python from [python.org](https://www.python.org/downloads/).
2. During installation, check ✅ **“Add Python to PATH”**.
3. Verify installation:

```bash
python --version
```

---

## 3. 🐚 Python Interactive Shell (REPL)

The Python shell lets you test code quickly. Go to start and write cmd or git bash, then a command prompt will be open. Write you pthyon script after >>> as it is shown below.

```python
>>> print("Hello, Python!")
Hello, Python!
>>> 2 + 3
5
```

---

## 4. 💻 Setting Up VS Code

1. Download [VS Code](https://code.visualstudio.com/).
2. Install the **Python extension**.
3. Create your first file: `hello.py`.

---

## 5. 📝 Writing Your First Program

```python
print("Hello, World!")
```

Run it:

```bash
python hello.py
```

✅ Congratulations—you’ve just written your first Python program!

---

# 🐍 Python Basics

## 6. 💬 Comments in Python

Comments are ignored by Python but helpful for humans.

### Single-line

```python
# This is a single-line comment
```

### Inline

```python
print("Learning Python")  # This explains the line
```

### Multi-line (docstring style)

```python
"""
This is a multi-line comment.
Good for detailed explanations.
"""
```

---

## 7. 🔤 Strings in Python

A **string** is text inside quotes.

```python
s1 = 'Hello'
s2 = "World"
s3 = """This is 
a multi-line string."""
```

Strings are powerful:

```python
name = "Python"
print(len(name))      # 6
print(name.upper())   # PYTHON
print(name.lower())   # python
print(name[0])        # P
print(name[-1])       # n
```

---

## 8. 📊 Variables

Variables store values.

```python
name = "Alice"     # string
age = 25           # integer
height = 5.7       # float
is_student = True  # boolean
```

Check type:

```python
print(type(height))   # <class 'float'>
```

---

## 9. ⚡ Common Built-in Functions

Python has many built-in functions. Here are the **most useful ones** for beginners:

### 1. `print()` → Displays output

```python
print("Hello, Python!")
```

### 2. `len()` → Returns the length of strings, lists, etc.

```python
print(len("Python"))  # 6
```

### 3. `type()` → Returns the data type

```python
print(type(25))       # <class 'int'>
print(type("Hi"))     # <class 'str'>
```

### 4. `str()`, `int()`, `float()`, `bool()` → Type conversion

```python
print(int("10"))     # 10 (string to integer)
print(float(5))      # 5.0
print(str(123))      # "123"
print(bool(""))      # False (empty string is False)
```

### 5. `input()` → Takes user input

```python
name = input("Enter your name: ")
print("Hello,", name)
```

### 6. `max()`, `min()` → Finds maximum or minimum value

```python
print(max(3, 7, 2))   # 7
print(min(3, 7, 2))   # 2
```

### 7. `sum()` → Adds items in a list

```python
numbers = [1, 2, 3, 4]
print(sum(numbers))   # 10
```

### 8. `round()` → Rounds a number

```python
print(round(3.14159, 2))  # 3.14
```

### 9. `abs()` → Absolute value

```python
print(abs(-7))       # 7
```

### 10. `sorted()` → Returns a sorted list

```python
print(sorted([3, 1, 4, 2]))  # [1, 2, 3, 4]
```

---

## 10. ➕➖ Arithmetic Operations

```python
a = 10
b = 3

print(a + b)   # 13
print(a - b)   # 7
print(a * b)   # 30
print(a / b)   # 3.333...
print(a // b)  # 3 (floor division)
print(a % b)   # 1 (remainder)
print(a ** b)  # 1000 (power)
```

---

# ✅ Exercises

1. Write a program that prints your name, age, and favorite hobby.
2. Use single-line, inline, and multi-line comments in your code.
3. Create three strings: one single-line, one multi-line, and one with your full name. Print their lengths.
4. Use at least **5 built-in functions** (`len()`, `type()`, `max()`, `sum()`, `round()`).
5. Perform all arithmetic operations (`+ - * / // % **`) on two numbers.
6. Take input from the user and greet them with their name.

---

🎯 **By the end of Week 1, you will be able to:**

* Install and run Python.
* Write and run programs in VS Code.
* Use different types of comments.
* Work with variables and strings.
* Apply common built-in functions.
* Perform arithmetic operations.

---





