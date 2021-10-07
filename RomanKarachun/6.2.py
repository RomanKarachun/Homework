class HistoryDict:
    def __init__(self, new, len_new=10):
        self.new = new
        self.len_new = len_new
        self.saved = []
    def set_value(self, key, value):
        self.new[key] = value
        self.saved.append(key)
        if len(self.saved) > self.len_new:
            self.saved.pop(0)
    def get_history(self):
        return self.saved
def main():
    d = HistoryDict({"foo": 42})
    d.set_value("bar", 43)
    print(d.get_history())
if __name__ == "__main__":
    main()
