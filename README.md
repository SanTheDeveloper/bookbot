# 📚 BookBot: Command-Line Text Analysis Tool

BookBot is a simple, yet robust, command-line utility built to perform foundational text analysis on any book (plain text file). It generates a comprehensive report detailing the total **word count** and the sorted **frequency of every letter** in the text.

_Built as a project for the [Boot.dev](https://boot.dev) backend development curriculum._

## 🚀 Getting Started

### Prerequisites

You need Python 3 installed on your system.

### 🛠️ Installation & Usage

1.  **Clone the Repository:**

    ```bash
    git clone [https://github.com/SanTheDeveloper/bookbot](https://github.com/SanTheDeveloper/bookbot)
    cd bookbot
    ```

2.  **Run the Analyzer:**
    Pass the path to your desired text file as a command-line argument.

    ```bash
    # Analyze the provided example book (using main.py)
    python3 main.py books/frankenstein.txt

    # Example analyzing a different text file
    python3 main.py books/mobydick.txt
    ```

    > **Note:** If no file path is provided, the program validates the arguments, prints a usage message, and exits with a status code of `1`.

## ⚙️ How It Works (Core Process Flow)

The application follows a clean pipeline to transform raw text into a final report:

1.  **Argument Validation**: Checks for and retrieves the file path from `sys.argv`.
2.  **File Reading**: Performs safe File I/O to read the entire text into memory using a context manager.
3.  **Data Preparation**: Converts the entire text to **lowercase** and filters out **non-alphabetical characters** (spaces, symbols, punctuation) for the frequency analysis using the `.isalpha()` string method.
4.  **Analysis**:
    - Calculates the total word count by splitting the text using `.split()`.
    - Builds a dictionary of character frequencies using the `dict.get(key, 0)` technique for efficient counting.
5.  **Reporting**: Converts the frequency dictionary into a **sorted list** (descending by count) using a custom `sort_on` key function, and prints the final formatted report to the console.

## 🧠 Core Python Concepts Learned

This project was a practical exercise in applying foundational Python skills:

### Data Handling & Structures

- **Command-Line Arguments (`sys.argv`)**: Dynamically accepting input from the terminal for flexible tool usage.
- **Dictionaries**: Using dictionaries as hash maps for efficient, non-sequential data storage (tracking `character` → `count`).
- **Lists of Dictionaries**: Transforming analysis results into a structured, sortable format (e.g., `[{'char': 'e', 'num': 46043}, ...]`).

### Text Processing & Control Flow

- **File I/O**: Best practices for reading text files using the `with open(...)` context manager.
- **String Methods**: Mastering `.split()`, `.lower()`, and the conditional check `.isalpha()` for data preparation.
- **Custom Sorting Logic**: Implementing custom sorting using the `list.sort(reverse=True, key=...)` method to order character counts.
- **Error Handling**: Implementing `try...except` blocks and `sys.exit(1)` for robust command-line behavior.

## 📊 Sample Output

The report structure is designed for clarity and quick insight:

```text
============ BOOKBOT ============
Analyzing book found at books/frankenstein.txt...
----------- Word Count ----------
Found 75767 total words
--------- Character Count -------
e: 44538
t: 29493
a: 25894
... (All alphabetical characters sorted by count)
p: 5952
b: 4868
v: 3737
...
z: 235
============= END ===============
```

## 🚧 Project Structure

```text
bookbot/
├── books/                             # Directory to store text files
│   └── frankenstein.txt               # Example input book
├── main.py                            # Main application script (handles I/O, argument parsing, report printing)
├── stats.py                           # Core logic (get_word_count, get_char_count, sorting functions)
└── README.md                          # Project documentation
```

## 📜 License

This project is part of the Boot.dev curriculum. Feel free to use it as a learning resource!
