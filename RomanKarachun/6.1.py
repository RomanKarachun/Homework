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
    c = Counter(start=42)
    c.increment()
    print(c.get())

    print("************************")

    c = Counter()
    c.increment()
    print(c.get())
    c.increment()
    print(c.get())

    print("************************")

    c = Counter(start=42, stop=43)
    c.increment()
    print(c.get())
    c.increment()
    print(c.get())

if __name__ == "__main__":
    main()
