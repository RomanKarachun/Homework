from contextlib import contextmanager

@contextmanager
def open_file(name):
    f = open(name, "w")
    yield f
    f.close()
with open_file('test72.txt') as f:
    f.write('Python has released version 3.10')
