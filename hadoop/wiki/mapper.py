#!/usr/bin/env python3
import sys
import re

docnum=0

for line in sys.stdin:
    if line.startswith("https://"):
        docnum=line.strip().split()[1]        
        continue

    line = re.sub(r'(\W|https:\/\/([\w_-]+(?:(?:\.[\w_-]+)+))([\w.,@?^=%&:\/~+#-]*[\w@?^=%&\/~+#-]))+',' ',line.strip())
    words = line.split()

    for word in words:
        print('{}\t{}\t{}'.format(word,docnum,1))