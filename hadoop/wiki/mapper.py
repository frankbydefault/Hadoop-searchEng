import sys
import re

for line in sys.stdin:
    if line.startswith("https://"):
        continue
    line = re.sub(r'(\W|https:\/\/([\w_-]+(?:(?:\.[\w_-]+)+))([\w.,@?^=%&:\/~+#-]*[\w@?^=%&\/~+#-]))+',' ',line.strip())
    words = line.split()

    for word in words:
        print('{}\t{}'.format(word,1))