# Memory Scanner

A Python application to scan and modify memory values of a running process.

## Features

- Scan memory for specific values in a running process
- Filter addresses that change to a new value
- Modify memory values at specific addresses

## Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/yourusername/memory-scanner.git
    cd memory-scanner
    ```

2. Install the required dependencies:

    ```bash
    pip install -r requirements.txt
    ```

## Usage

1. Run the application:

    ```bash
    python cli.app
    ```

2. Follow the prompts to enter the process name, initial value, new value, and modification value.

## Project Structure

```filetree
memory-scanner
├── cli
│   └── app.py
├── src
│   ├── __init__.py
│   ├── memory_scanner.py
│   └── utils.py
├── tests
│   ├── __init__.py
│   └── test_memory_scanner.py
├── requirements.txt
└── README.md
