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
#fetching the articles and making the txts
for t in data:
        page_py = wiki_wiki.page(t['title'])

        if not os.path.exists("./carpeta1"):
                os.makedirs("./carpeta1")

        if not os.path.exists("./carpeta2"):
                os.makedirs("./carpeta2")


        if count <5:
                text_file = open("./carpeta1/"+t['title']+".txt", "w")
                count += 1
        else:
                text_file = open("./carpeta2/"+t['title']+".txt", "w")

        text_file.write(page_py.text)
        text_file.close()