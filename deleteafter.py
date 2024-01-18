import os


def file_delete():
    file_to_delete = ["comments.csv", "Full Comments.csv"]

    for f in file_to_delete:
        os.remove(f)
