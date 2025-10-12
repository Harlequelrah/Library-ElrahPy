import os

from elrahpy.fileskit import filestools
from elrahpy.fileskit.filestools import (
    delete_line,
    delete_line_startswith,
    insert_line,
    read_line,
    replace_line,
    reset_file,
    rewrite_content,
)


def test_should_copy_file_content():
    f1 = "f1.txt"
    f2 = "f2.txt"
    with open(f1, "w") as f1w:
        f1w.write("Hello")
    open(f2, "w").close()
    rewrite_content(f1, f2)
    with open(f2, "r") as f2r:
        line = f2r.readline()
        assert line.strip() == "Hello"
    os.remove(f1)
    os.remove(f2)


def test_should_reset_file():
    f = "f.txt"
    with open(f, "w") as fw:
        fw.write("Hello")
    reset_file(f)
    with open(f, "r") as fr:
        line = fr.readline()
        print("line", line)
        assert line == ""
    os.remove(f)


def test_should_read_line():
    f = "file.txt"
    lignes = ["Première ligne\n", "Deuxième ligne\n", "Troisième ligne\n"]
    with open(f, "a") as fa:
        fa.writelines(lignes)
    line = read_line(file=f, line=2)
    assert line == "Deuxième ligne\n"
    os.remove(f)


def test_should_delete_line():
    f = "file.txt"
    lignes = ["Première ligne\n", "Deuxième ligne\n", "Troisième ligne\n"]
    with open(f, "a") as fa:
        fa.writelines(lignes)
    delete_line(file=f, line=1)
    with open(f, "r") as fr:
        line = fr.readline()
    assert line == "Deuxième ligne\n"
    os.remove(f)


def test_should_deleteline_startswith():
    f = "file.txt"
    lignes = ["x-Première ligne\n", "y-Deuxième ligne\n", "x-Troisième ligne\n"]
    with open(f, "a") as fa:
        fa.writelines(lignes)
    delete_line_startswith(file=f, marker="x-")
    with open(f, "r") as fr:
        lines = fr.readlines()
        assert len(lines) == 1
        assert lines[0] == "y-Deuxième ligne\n"
    os.remove(f)


def test_should_repaceline():
    f = "file.txt"
    lignes = ["Première ligne\n", "Deuxième ligne\n", "Troisième ligne\n"]
    with open(f, "a") as fa:
        fa.writelines(lignes)
    replace_line(file=f, line=2, line_content="Hello\n")
    with open(f, "r") as fr:
        line2 = fr.readlines()[1]
        assert line2 == "Hello\n"
    os.remove(f)


def test_should_insert_line():
    f = "file.txt"
    lignes = ["Première ligne\n", "Troisième ligne\n"]
    with open(f, "a") as fa:
        fa.writelines(lignes)
    insert_line(file=f, line=2, line_content="Deuxième ligne\n")
    with open(f, "r") as fr:
        line2 = fr.readlines()[1]
        assert line2 == "Deuxième ligne\n"
    os.remove(f)
