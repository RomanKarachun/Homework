import re
import collections
with open("lorem_ipsum.txt") as f:
    text = f.read()

words = re.compile(r"[\w']+").findall(text)
counts = collections.Counter(words).most_common(3)
print(counts)
