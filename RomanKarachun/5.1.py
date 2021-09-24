with open("unsorted_names.txt") as f, open("sorted_names.txt", "w") as fw:
    [fw.write(x+"\n") for x in sorted([x for x in ",".join(f.readlines()).split(",")])]
