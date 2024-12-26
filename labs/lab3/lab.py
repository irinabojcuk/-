def read_file(file_name):
    with open(file_name, 'r') as file:
        return file.read()


def write_file(file_name, content):
    with open(file_name, 'w') as file:
        file.write(content)


def append_to_file(file_name, text):
    with open(file_name, "a+") as f:
        f.write('\n' + text)


