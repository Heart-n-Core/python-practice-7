from app.io.input import read_file_builtin, read_file_with_pandas, read_text_from_console
from app.io.output import print_text_to_console, write_file_builtin


def main():
    console_text = read_text_from_console()
    builtin_text = read_file_builtin("data/data_from.txt")
    pandas_text = read_file_with_pandas("data/data_from.txt")

    outputs = {
        "Console input": console_text,
        "Built-in file read": builtin_text,
        "Pandas file read": pandas_text,
    }

    for label, text in outputs.items():
        print_text_to_console(f"{label}:")
        print_text_to_console(text)

    combined_result = "\n\n".join(f"{label}:\n{text}" for label, text in outputs.items())
    write_file_builtin("data/data_to.txt", combined_result)

if __name__ == '__main__':
    main()