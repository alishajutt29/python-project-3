# 🧠 General Knowledge Quiz — Python Programming (Project 4)

A simple command-line quiz game built as **Project 4** of the DecodeLabs
Python Programming Industrial Training (Batch 2026).

This project focuses on **control flow** — using if-else logic and
variables to direct a program based on user input.

## ✨ Features

- Asks 3 general knowledge questions
- Checks each answer using if-else logic
- Cleans up user input (removes extra spaces, ignores capitalization)
  so "Paris", " paris", and "PARIS" all count as correct
- Keeps a running score
- Prints the final score out of 3 at the end

## 🚀 How to Run

```bash
python3 quiz.py
```

Example run:

```
General Knowledge Quiz
-----------------------
Q1. What is the capital of France? paris
Correct!
Q2. How many continents are there? 7
Correct!
Q3. What is the largest planet in our solar system? mars
Wrong. The correct answer is Jupiter.
-----------------------
Your final score is 2 out of 3.
```

## 🧠 Concepts Used

| Concept            | Where it's used                                      |
|--------------------|--------------------------------------------------------|
| Variables          | `score` keeps track of correct answers                  |
| if-else logic      | Checking each answer against the correct one             |
| String methods     | `.strip()` and `.lower()` to clean up user input          |
| f-strings          | Displaying the final score                                |

## 📂 Project Structure

```
quiz-python/
├── quiz.py
├── README.md
└── .gitignore
```

## 🏢 About

Built as part of the **DecodeLabs Industrial Training Kit — Python
Programming, Batch 2026**.

🌐 www.decodelabs.tech
