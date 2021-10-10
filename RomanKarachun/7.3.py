import time
from contextlib import ContextDecorator

class time73(ContextDecorator):
    def __init__(self, f):
        self.f = f
    def __enter__(self):
        self.start = time.perf_counter()

    def __exit__(self, exc_type, exc, exc_tb):
        f = open(self.f, mode="w")
        f.write(f"Time passed: {time.perf_counter() - self.start:} seconds")
        f.close()
        return True

@time73("test73.txt")
def function(a, b):
    return (a + b) * (a - b)

def main():
    with time73("test73.txt"):
        print(function(101021, 155))

if __name__ == "__main__":
    main()
