def write_file(file_name, file_content):
    my_file = open(f"{file_name}.txt", mode='w')
    my_file.write(file_content)

def append_file(file_name, append_content):
    my_file = open(f"{file_name}.txt", mode='a')
    my_file.write(append_content)

def read_file(file_name):
    my_file = open(f"{file_name}.txt")
    return my_file.read()
