import wikipediaapi
import requests
import os
#Getting random titles from wikipedia

limit = 10
response = requests.get(f"https://en.wikipedia.org/w/api.php?action=query&format=json&list=random&rnnamespace=0&rnlimit={limit}").json()
data = response["query"]["random"]
try:
        size = os.get_terminal_size()[0]
except OSError:
        size = 40

wiki_wiki = wikipediaapi.Wikipedia(
        language='en',
        extract_format=wikipediaapi.ExtractFormat.WIKI
)

count = 0
print(f"[{' '*(size-7)}]   0%", end="\r")
#fetching the articles and making the txts
for t in data:
        page_py = wiki_wiki.page(t['title'])

        if not os.path.exists("./hadoop/wiki/carpeta1"):
                os.makedirs("./hadoop/wiki/carpeta1")

        if not os.path.exists("./hadoop/wiki/carpeta2"):
                os.makedirs("./hadoop/wiki/carpeta2")

        with open(f"./hadoop/wiki/carpeta{1 if count < 5 else 2}/Documento{count+1}.txt", "w") as f:
                f.write(page_py.fullurl + '\n')
                count += 1
                f.write(page_py.text)

        print(f"[{'='* (c :=(((size - 8) // limit) * count))}>{' '*(size - c - 8)}] {' '*(3 - len(str(count * 100 // limit)))}{count * 100 // limit}%", end="\r")
print(f"[{'='*(size-7)}] 100%")