from contextlib import contextmanager

@contextmanager
def open_file(name):
    try:
        f = open(name, "w")
        yield f
    except Exception as error:
        pass
    finally:
        f.close()
with open_file('test74.txt') as f:
    print('Exception not occure')
    f.write('Python has released version 3.10')
