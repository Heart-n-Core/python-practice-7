def print_text_to_console(text):
    """Print text to the console."""
    print(text)


def write_file_builtin(path, content):
    """Write content to a file using Python builtins."""
    with open(path, "w", encoding="utf-8") as file:
        file.write(content)
