from math import floor


def rewrite_content(ficher_source: str, ficher_destination: str):
    with open(ficher_source, "r") as fs:
        lines = fs.readlines()
    with open(ficher_destination, "w") as fd:
        fd.writelines(lines)


def reset_file(file: str):
    with open(file, "w") as ficher:
        ficher.close()


def read_line(file: str, line: int):
    with open(file, "r") as f:
        return f.readlines()[line - 1]


def delete_line(file: str, line: int):
    with open(file, "r") as ficher:
        a = ficher.readlines()
        if 1 <= line < len(a):
            del a[line - 1]
    with open(file, "w") as ficher:
        ficher.writelines(a)


def delete_line_startswith(file: str, marker: str):
    with open(file, "r") as ficher:
        a = ficher.readlines()
    for line in a:
        if line.startswith(marker):
            a.remove(line)
    with open(file, "w") as ficher:
        ficher.writelines(a)


def replace_line(file: str, line: int, line_content: str):
    with open(file, "r") as ficher:
        a = ficher.readlines()
    with open(file, "w") as ficher:
        ficher.writelines(a[0 : line - 1])
        ficher.write(line_content)
        ficher.writelines(a[line:])


def insert_line(file: str, line: int, line_content: str):
    with open(file, "r") as ficher:
        a = ficher.readlines()
    with open(file, "w") as ficher:
        ficher.writelines(a[0 : line - 1])
        ficher.write(line_content)
        ficher.writelines(a[line - 1 :])
