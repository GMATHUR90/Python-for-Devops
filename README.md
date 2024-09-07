# Python for DevOps

Welcome to the **Python for DevOps** repository! This project is a collection of Python scripts and tools that focus on various DevOps-related tasks. The primary purpose of this repository is for personal learning, covering topics such as file handling, encryption, AWS automation, regular expressions, and more. This repository aims to enhance Python skills and explore its applications in DevOps scenarios.

## Table of Contents

- [Introduction](#introduction)
- [Table of Contents](#table-of-contents)
- [Folder Structure](#folder-structure)
- [Scripts Overview](#scripts-overview)
- [Installation Instructions](#installation-instructions)
- [Usage Guide](#usage-guide)
- [Contributing](#contributing)
- [License](#license)

## Folder Structure

Here's an overview of the folder structure in this repository:

```plaintext
.
├── argparse/                   # Command-line argument parsing scripts
├── aws_boto_library/           # AWS automation scripts using Boto3
├── data_structures/            # Examples of Python data structures
├── disk_utils/                 # Disk utility scripts (e.g., fdisk, blkid, lsblk)
├── encryption/                 # Encryption and hashing scripts
├── file_handling/              # File operations and handling scripts
├── regex_library/              # Regular expression examples and tasks
└── utils/                      # Various utility scripts
```
# Scripts Overview
Here’s a summary of some of the key scripts and their functionalities:

## Command-Line Tools
- **`argparse/Command_line_tool_using_argparse.py`**: Demonstrates how to use `argparse` to create command-line tools in Python.
- **`argparse/Using_Click.py`**: Uses the `Click` library to create a more user-friendly command-line interface.

## AWS Automation
- **`aws_boto_library/Python_Task-1_Creating_S3_Bucket_using_Boto3.py`**: Automates the creation of an S3 bucket using the `boto3` library.
- **`aws_boto_library/Python_Task-3_Creating_EC2_Instance_Using_Boto3.py`**: Automates the creation of an EC2 instance using `boto3`.

## Data Structures
- **`data_structures/Data_Structure_Binary_Tree.py`**: Implements a binary tree.
- **`data_structures/Data_Structure_Graph.py`**: Implements a graph and its traversal methods.

## File Handling
- **`file_handling/File_Task_1_Reverse_the_content_of_a_file.py`**: Reverses the content of a file.
- **`file_handling/File_Task_2_Print_specific_line.py`**: Prints specific lines from a log file based on a pattern.

## Encryption and Security
- **`encryption/Encrypting_Text_Hashing_&_Hashlib.py`**: Demonstrates text hashing and encryption using Python's `hashlib`.
- **`encryption/Encryption_With_Cryptography.py`**: Uses the `cryptography` library for encryption tasks.

## Regular Expressions
- **`regex_library/Regex_Task_3_Extract_All_the_IP_Addresses.py`**: Extracts all IP addresses from a log file using regular expressions.
- **`regex_library/Regex_Task_4_Extract_dates_in_the_format_of_yyyy-mm-dd.py`**: Extracts dates in `yyyy-mm-dd` format from a log file using regular expressions.

# Installation Instructions
To get started, clone the repository to your local machine:

```bash
git clone https://github.com/GMATHUR90/rhcsa-prep.git
cd rhcsa-prep
```
# Project Setup and Usage Guide

## Prerequisites

Make sure you have Python 3.x installed. You can check your Python version with:

```bash
python3 --version
```
# If there are any required dependencies for specific scripts, install them using pip:
```bash
pip install -r requirements.txt
```
If there is no requirements.txt file, refer to the individual scripts to see which libraries need to be installed (e.g., boto3, cryptography, Click).

# Contributing
This repository is for personal learning purposes only. Contributions, issues, or pull requests from others are not being accepted at this time.

# License
This repository is licensed under the MIT License. See the LICENSE file for more details.
