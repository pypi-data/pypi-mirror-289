# Wise Print

<p align="left">
  <a href="https://pypi.python.org/pypi/wise_print"><img alt="PyPI" src="https://img.shields.io/pypi/v/wise_print.svg"></a>
</p>

`wise_print` is a lightweight Python package designed to enhance the debugging process in small scripts. It provides a customizable replacement for the built-in `print` function, allowing you to include additional contextual information in your output without the need for a full-fledged logging package.

## Overview

When debugging small scripts, you might not want to set up a logging configuration or deal with the overhead of logging frameworks. `wise_print` offers an easy way to add context to your print statements, making it easier to track the origin of messages and debug your code.

With `wise_print`, you can easily configure your output to include details such as:

- **Timestamp**: When the print statement was executed.
- **File Name**: The file in which the print statement was called.
- **Line Number**: The line number where the print statement was invoked.

## Installation

You can install `wise_print` using pip. Simply run:

```bash
pip install wise_print
```

## Usage

Here’s how you can use `wise_print` in your script:

1. **Import and Configure `wise_print`**:

   ```python
   from wise_print import CustomPrinter
   
   # Create an instance of CustomPrinter
   printer = CustomPrinter(include_time=True, include_file=True, include_line=True, separator=' | ')
   
   # Activate the custom print function
   printer.activate()
   ```

2. **Use `print` as Usual**:

   After activating `wise_print`, you can use the `print` function normally:

   ```python
   print("This is a debug message")
   ```

   The output will include the timestamp, filename, and line number based on your configuration.

3. **Deactivate `wise_print`**:

   To return to the standard `print` behavior, simply deactivate `wise_print`:

   ```python
   printer.deactivate()
   print("This is a standard print message")
   ```

## Example

Here’s a complete example demonstrating the use of `wise_print`:

```python
from wise_print import CustomPrinter

# Create and configure the custom printer
printer = CustomPrinter(include_time=True, include_file=True, include_line=True, separator=':')
printer.activate()

# Example print statements
print("Starting process...")
for i in range(3):
    print(f"Processing item {i}")

# Deactivate custom print
printer.deactivate()
print("Process finished.")
```

Output might look like:

```
2024-08-09T12:34:56:/path/to/your/script.py:8 | Starting process...
2024-08-09T12:34:56:/path/to/your/script.py:9 | Processing item 0
2024-08-09T12:34:56:/path/to/your/script.py:9 | Processing item 1
2024-08-09T12:34:56:/path/to/your/script.py:9 | Processing item 2
Process finished.
```

## Comparison with Python's `logging` Package

`wise_print` and Python’s built-in `logging` package serve different purposes and have distinct advantages and limitations. Here’s a comparison to help you decide when to use each:

| Feature               | `wise_print`                          | `logging`                              |
|-----------------------|---------------------------------------|----------------------------------------|
| **Ease of Use**       | Simple and straightforward for small scripts. | Requires setup and configuration, but very flexible. |
| **Configuration**     | Minimal configuration required.       | Highly configurable with multiple handlers and formatters. |
| **Output**            | Directly replaces `print` statements. | Supports multiple output destinations (console, files, remote servers). |
| **Performance**       | Lightweight and fast.                 | Can be slower due to extensive features and configurations. |
| **Context Information** | Includes timestamp, filename, and line number. | Can include extensive context and metadata (log levels, exception info, etc.). |
| **Flexibility**       | Limited to custom print behavior.     | Highly flexible with log levels, formatting, and custom handlers. |
| **Use Case**          | Best for quick debugging in small scripts. | Ideal for production code and complex applications requiring detailed logging. |

### When to Use `wise_print`

- **Quick Debugging**: When you need to quickly add context to print statements in small scripts or during early development stages.
- **Simplicity**: When you prefer a lightweight, straightforward solution without the complexity of logging configurations.
- **Minimal Setup**: When you want to avoid setting up a logging framework for small or one-off scripts.

### When to Use `logging`

- **Production Code**: For applications where detailed and configurable logging is required, including different log levels and multiple output destinations.
- **Complex Applications**: When you need advanced logging features such as logging to files, sending logs over the network, or integrating with external logging systems.
- **Structured Logging**: When you need structured and rich log information, including exceptions, context data, and custom log levels.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.

## Contributing

Contributions are welcome! Please fork the repository and submit a pull request with your changes.
