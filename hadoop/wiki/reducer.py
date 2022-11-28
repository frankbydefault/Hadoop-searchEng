#!/usr/bin/env python3
import sys

current_word = None
current_count = 0
word = None

words = {}

# word (doc,val)
for line in sys.stdin:
    line = line.strip()
    word, docnum, count = line.split('\t',3)
    
    try:
        count = int(count)
    except ValueError:
        continue

    if word not in words:
        words[word] = [[i, 0] for i in range(1, 11)]
    
    words[word][int(docnum) - 1][1] += int(count)

for word in words:
    string = f"{word}\t"
    for docnum, count in [v for v in words[word] if v[1] != 0]:
        string += f"({docnum},{count})"
    print(string)