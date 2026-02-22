def read_text_from_console():
    """Read text input from the console."""
    return input("Enter text: ")


def read_file_builtin(path):
    """Read file contents using Python builtins."""
    with open(path, "r", encoding="utf-8") as file:
        return file.read()


def read_file_with_pandas(path):
    """Read file contents using pandas."""
    import pandas as pd

    data_frame = pd.read_csv(path, header=None)
    return "\n".join(data_frame.iloc[:, 0].astype(str).tolist())
