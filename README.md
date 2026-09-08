# 🔐 Random Password Generator — Python Programming (Project 3)

A command-line tool built as **Project 3** of the DecodeLabs Python
Programming Industrial Training (Batch 2026).

This project focuses on **importing built-in modules** (`random` and
`string`) and using them to generate secure, random passwords.

## ✨ Features

- Asks the user for a desired password length
- Validates input (rejects text or lengths under 4)
- Generates a random password using letters (upper + lower) and digits
- Uses `''.join()` for efficient string building instead of repeated
  concatenation

## 🚀 How to Run

```bash
python3 password_generator.py
```

Example run:

```
Random Password Generator
--------------------------
Enter desired password length: 10

Your generated password is: aT8kLq2Zx9
```

## 🧠 Concepts Used

| Concept              | Where it's used                              |
|----------------------|-----------------------------------------------|
| Module imports       | `import random`, `import string`               |
| `string` constants   | `string.ascii_letters`, `string.digits`         |
| `random.choice()`    | Picking a random character from the pool        |
| `''.join()`          | Building the final password string efficiently  |
| Input validation     | `try/except` for non-numeric input              |

## 📂 Project Structure

```
password-generator-python/
├── password_generator.py
├── README.md
└── .gitignore
```

## 🏢 About

Built as part of the **DecodeLabs Industrial Training Kit — Python
Programming, Batch 2026**.

🌐 www.decodelabs.tech
