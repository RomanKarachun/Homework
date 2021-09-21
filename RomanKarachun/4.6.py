def get_shortest_word(s: str) -> str:
    words = s.split()
    a =  words[0]        
    for word in words[0:]:
        if len(word) > len(a):
            a = word
    return a
print(get_shortest_word('Python is simple and effective!'))
print(get_shortest_word('Any pythonista like namespaces a lot.'))
