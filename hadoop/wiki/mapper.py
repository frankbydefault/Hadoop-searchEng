#!/usr/bin/env python3
import sys
import re

for line in sys.stdin:
    if line.startswith("https://"):
        continue

    if line.startswith("--"):
        docnum = line.split()
        print(docnum[1])

    line = re.sub(r'(\W|https:\/\/([\w_-]+(?:(?:\.[\w_-]+)+))([\w.,@?^=%&:\/~+#-]*[\w@?^=%&\/~+#-]))+',' ',line.strip())
    words = line.split()

    for word in words:
        print('{}\t{}\t{}'.format(word,docnum[1],1))