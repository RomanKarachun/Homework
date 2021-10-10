from contextlib import contextmanager

@contextmanager
def open_file(name):
    try:
        f = open(name, "w")
        yield f
    except Exception as error:
        print("Exception")
    finally:
        f.close()
with open_file('test72.txt') as f:
    f.write('Python has released version 3.10')
