with open(lorem_ipsum.txt) as f:
    text = f.read()

words = re.compile(r"[\w']+", re.U).findall(text)   # re.U == re.UNICODE
counts = collections.Counter(words)
