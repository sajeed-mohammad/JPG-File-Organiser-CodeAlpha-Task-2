#  JPG File Organizer – Python Automation

##  Project Overview

The **JPG File Organizer** is a Python automation project developed as part of **Python Development**.

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
##  Important Note for GitHub Testing

When this project is pushed to GitHub, the JPG files used during development and testing may already be organized and moved into the `JPG Files` folder.

Therefore, when someone clones or downloads this repository and runs the program, the `source file` folder may not contain any JPG files available for testing.

###  How to Test the Project

To test the JPG File Organizer:

1. Clone or download this repository.
2. Open the project in VS Code.
3. Open the `source file` folder.
4. Add a few `.jpg` image files manually.
5. Run `jpgfileorganiser.py`.
6. The program will detect the JPG files.
7. The JPG files will automatically be moved into the `JPG Files` folder.
8. Check the console output to verify the files were organized successfully.

> **Note:** If there are no JPG files inside the `source file` folder after downloading the repository, this is expected. Add a few `.jpg` files to the folder before running the program.
> ---

##  Project Structure

```text
JPG-File-Organiser-CodeAlpha-Task-2/
│
├── jpgfileorganiser.py
│
├── source file/
│
└── JPG Files/

```
## Author
**Mohammad Sajeed**


