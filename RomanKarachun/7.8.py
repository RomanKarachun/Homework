class MySquareIterator:
    def __init__(self, l):
        self.l = l
    def __iter__(self):
        self.n = -1
        self.e = len(self.l) - 1
        return self
    def __next__(self):
        if self.n < self.e:
            self.n += 1
            result = self.l[self.n] ** 2
            return result
        else:
            raise StopIteration
    
def main():
    lst = [1, 2, 3, 4, 5]
    itr = MySquareIterator(lst)
    for item in itr:
        print(item)
        
if __name__ == "__main__":
    main()
