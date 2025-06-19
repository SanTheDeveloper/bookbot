# 📚 BookBot - Text Analysis Tool

BookBot is a command-line text analysis tool that processes books (text files) and generates reports on word count and letter frequency. Built as part of the [Boot.dev](https://boot.dev) curriculum.

## 🧠 Concepts Learned

### Core Python Programming

- **File I/O Operations**: Reading text files (`open()`, `read()`), handling relative file paths
- **String Manipulation**: Case normalization (`.lower()`), character filtering (`isalpha()`), splitting text into words (`split()`)
- **Data Structures**: Dictionaries for tracking letter frequencies, converting dictionaries to sorted lists
- **Control Flow**: Loops (`for`, `while`), conditional logic (`if`/`elif`/`else`), function definitions
- **Data Processing**: Word counting, character frequency analysis, sorting results (`sorted()` + lambda functions)
- **Error Handling**: Basic exception handling (e.g., file not found)
- **Command-Line Execution**: Using `sys.argv`, script execution flow (`if __name__ == "__main__":`)

## ⚙️ How It Works

1. **Input**: Provide a `.txt` file path (e.g., `books/frankenstein.txt`)
2. **Processing**:
   - Extracts text and converts to lowercase
   - Splits text into words
   - Counts occurrences of each letter (a-z)
3. **Output**: Prints:
   - Total word count
   - Sorted letter frequencies (descending order)
   - Visual histogram of letter usage

## 🚀 Sample Output

```text
--- Begin report of books/frankenstein.txt ---
47486 words found in the document

The 'e' character was found 46043 times
The 't' character was found 30365 times
The 'a' character was found 26743 times
The 'o' character was found 25224 times
The 'i' character was found 22224 times
The 'n' character was found 22167 times
The 's' character was found 21128 times
The 'r' character was found 20576 times
The 'h' character was found 17631 times
The 'd' character was found 14610 times
The 'l' character was found 14407 times
The 'u' character was found 10396 times
The 'm' character was found 10001 times
The 'c' character was found 9244 times
The 'w' character was found 8987 times
The 'f' character was found 8732 times
The 'g' character was found 8611 times
The 'y' character was found 8032 times
The 'p' character was found 5997 times
The 'b' character was found 5591 times
The 'v' character was found 3880 times
The 'k' character was found 3746 times
The 'j' character was found 392 times
The 'x' character was found 370 times
The 'q' character was found 324 times
The 'z' character was found 234 times
--- End report ---
```
