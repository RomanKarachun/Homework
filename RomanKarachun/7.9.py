class EvenRange:
    def __init__(self, start, end):
        self.start = start
        self.end = end
        self._flag = False
        self._index = 1

    def __iter__(self):
        self._flag = True
        return self

    def __next__(self):
        if self.start < self.end:
            if self.start %2 !=0:
                self.start += 1
            
            if self.start != self.end:
                self.start += 1
                return self.start - 1
        if self._index:
            if not self._flag:
                return "Out of numbers!"
            self._index = 0
            return "Out of numbers!"
        raise StopIteration
        
def main():
    er1 = EvenRange(7,11)
    n = next(er1)
    print(n)
    n = next(er1)
    print(n)
    print(next(er1))
    print(next(er1))
    er2 = EvenRange(3, 14)
    for number in er2:
        print(number)

if __name__ == "__main__":
    main()
