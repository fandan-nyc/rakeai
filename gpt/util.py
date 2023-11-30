import getpass

def get_user():
    return getpass.getuser()

def load_file(path):
    with open(path, "r") as f:
        file_content = f.read()
    return file_content

