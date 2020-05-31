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
print("Pass" if find_files(".c", "./testdir") == ['./testdir\\subdir1\\a.c', './testdir\\subdir3\\subsubdir1\\b.c',
                                                  './testdir\\subdir5\\a.c', './testdir\\t1.c']
      else "Fail")
print("Test finding .h file")
print("Pass" if find_files(".h", "./testdir") == ['./testdir\\subdir1\\a.h', './testdir\\subdir3\\subsubdir1\\b.h',
                                                  './testdir\\subdir5\\a.h', './testdir\\t1.h']
      else "Fail")
print("Test finding .gitkeep file")
print("Pass" if find_files(".gitkeep", "./testdir") == ['./testdir\\subdir2\\.gitkeep', './testdir\\subdir4\\.gitkeep']
      else "Fail")
print("Test extreme case: no suffix given")
print("Pass" if find_files("", "./testdir") == ['./testdir\\subdir1\\a.c', './testdir\\subdir1\\a.h',
                                                './testdir\\subdir2\\.gitkeep', './testdir\\subdir3\\subsubdir1\\b.c',
                                                './testdir\\subdir3\\subsubdir1\\b.h', './testdir\\subdir4\\.gitkeep',
                                                './testdir\\subdir5\\a.c', './testdir\\subdir5\\a.h', './testdir\\t1.c',
                                                './testdir\\t1.h']
      else "Fail")
print("Test extreme case: wrong suffix given")
print("Pass" if find_files(".py", "testdir") == []
      else "Fail")
