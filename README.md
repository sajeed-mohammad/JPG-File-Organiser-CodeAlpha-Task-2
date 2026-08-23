#  JPG File Organizer – Python Automation

##  Project Overview

The **JPG File Organizer** is a Python automation project developed as part of **CodeAlpha Python Programming Intern**.

The purpose of this project is to automate a simple repetitive file-management task. The program scans a source folder, identifies all `.jpg` image files, and automatically moves them into a separate folder named `JPG Files`.

This helps reduce manual effort and makes file organization faster and easier.

---

##  Objective

The main objective of this project is to automate the process of organizing JPG files.

Instead of manually searching for JPG files and moving them one by one, the Python script automatically:

- Scans the source folder
- Identifies JPG files
- Creates the destination folder if required
- Moves JPG files to the destination folder
- Displays the result of the operation

---

##  Features

-  Automatically scans the `source file` folder
-  Detects `.jpg` files
-  Supports `.jpg`, `.JPG`, and other capitalization variations
-  Automatically creates the `JPG Files` folder
-  Moves JPG files automatically
-  Ignores files with other extensions
-  Displays the total number of files moved
-  Handles cases where no JPG files are found
-  Simple and clear console output

---

##  Technologies Used

- **Python**
- **os module**
- **shutil module**

---

##  Python Concepts Used

- Variables
- Strings
- Lists
- `for` loops
- `if-else` statements
- File handling
- Directory handling
- String methods
- `os.path`
- `os.listdir()`
- `os.makedirs()`
- `os.path.isfile()`
- `shutil.move()`

---

##  Project Structure

```text
JPG-File-Organiser-CodeAlpha-Task-2/
│
├── jpgfileorganiser.py
│
├── source file/
│
└── JPG Files/
