# 🔐 Offline Password Generator

A lightweight Python script that generates a secure **16-character random password** every time it is executed.

## Why I Built This

There are many excellent password generators and password managers available online. However, I wanted a simple tool that works completely offline.

An offline password generator:

* Doesn't require an internet connection.
* Doesn't send any data to remote servers.
* Has a smaller attack surface because it isn't exposed as an online service.
* Helps me better understand secure password generation in Python.

This project wasn't created to replace established password managers. Instead, it was built as a learning exercise and a lightweight utility for generating strong passwords locally.

## Features

* Generates a random 16-character password.
* Uses Python's cryptographically secure random number generator.
* Includes uppercase letters, lowercase letters, numbers, and special characters.
* No external dependencies.

## Requirements

* Python 3.x

## How to Run

```bash
python password_generator.py
```

## Example Output

```text
Generated Password:
X@7mQ!2rLp#9Nv$K
```

## Technologies Used

* Python
* `secrets`
* `string`

---

If you find this project useful or have suggestions for improvement, feel free to fork the repository or open an issue.
