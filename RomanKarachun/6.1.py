class Counter:
    def __init__(self, start = 0, stop = -1):
        self.start = start
        self.stop = stop
        
    def get(self):
        return self.start

    def increment(self):
        if self.start + 1 == self.stop:
            raise Exception("Maximal value is reached.")
        else:
            self.start += 1
            

            
def main():
    first = Counter(start=42)
    first.increment()
    print("first =", first.get())

    print("************************")

    second = Counter()
    second.increment()
    print("second =", second.get())
    second.increment()
    print("second =", second.get())

    print("************************")

    third = Counter(start=42, stop=43)
    third.increment()
    print("third =", third.get())

if __name__ == "__main__":
    main()
