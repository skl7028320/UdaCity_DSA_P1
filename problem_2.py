import os


def find_files(suffix, path):
    if os.path.isfile(path):
        if path.endswith(suffix):
            return [path]
        else:
            return []

    output = list()

    sub_path_list = os.listdir(path)
    for sub_path in sub_path_list:
        small_output = find_files(suffix, os.path.join(path, sub_path))
        output.extend(small_output)

    return output


print("Test finding .c file")
print(find_files(".c", "./testdir"))
print("Test finding .h file")
print(find_files(".h", "./testdir"))
print("Test finding .gitkeep file")
print(find_files(".gitkeep", "./testdir"))
print("Test extreme case: no suffix given")
print(find_files("", "./testdir"))
print("Test extreme case: wrong suffix given")
print(find_files(".py", "testdir"))
