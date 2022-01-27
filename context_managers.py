# with open('notes.txt', 'w') as file:
#     file.write('chaos')

# won't work
# with open('notes2.txt') as file:
#     pass

# how to make a custom context manager. need the enter and exit methods
from contextlib import contextmanager


class ManagedFile:
    def __init__(self, filename) -> None:
        self.filename = filename
        self.file = None

    def __enter__(self):
        print('enter')
        self.file = open(self.filename, 'w')
        return self.file

    def __exit__(self, exc_type, exc_value, exc_traceback):
        if self.file:
            self.file.close()
        print('exc:', exc_type, exc_value, exc_traceback)
        
        print('exit')

with ManagedFile('notes3.txt') as mf:
    mf.write('orderrr')


# can also create contextmanager in 
@contextmanager
def open_managed_file(filename):
    f = open(filename, 'w')
    try:
        yield f
    finally:
        f.close()

with open_managed_file('notes4.txt') as omf:
    omf.write('more chaos')