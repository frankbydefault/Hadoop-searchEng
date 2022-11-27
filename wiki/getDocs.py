import wikipediaapi
import requests
import os
#Getting random titles from wikipedia

response = requests.get("https://en.wikipedia.org/w/api.php?action=query&format=json&list=random&rnnamespace=0&rnlimit=10").json()
data = response["query"]["random"]

wiki_wiki = wikipediaapi.Wikipedia(
        language='en',
        extract_format=wikipediaapi.ExtractFormat.WIKI
)

count = 0
print(f"[{'=='*count}>{'  '*(10 - count)}]", end="\r")
#fetching the articles and making the txts
for t in data:
        page_py = wiki_wiki.page(t['title'])

        if not os.path.exists("./wiki/carpeta1"):
                os.makedirs("./wiki/carpeta1")

        if not os.path.exists("./wiki/carpeta2"):
                os.makedirs("./wiki/carpeta2")

        text_file = open(f"./wiki/carpeta{1 if count < 5 else 2}/Documento{count+1}.txt", "w")
        count += 1

        text_file.write(page_py.text)
        text_file.close()
        print(f"[{'=='*count}>{'  '*(10 - count)}]", end="\r")
print(f"[{'=='*(count+1)}]")