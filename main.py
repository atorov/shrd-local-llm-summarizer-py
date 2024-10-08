def save_text_to_file(text: str, file_path: str) -> None:
    """
    Save a string of text to a specified file path.

    :param text: The text to be saved.
    :param file_path: The path to the file to be written.
    """
    with open(file_path, 'w') as file:
        file.write(text)


save_text_to_file('Hello, world!', 'hello.txt')
