def replace_char(string, to_put, index):
    string = string[:index] + to_put + string[index + 1:]
    return string