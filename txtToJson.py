import json
# your mongo stuff goes here

def getURL(numdoc):
    with open(f"wiki/carpeta{1 if numdoc < 6 else 2}/Documento{numdoc}.txt", "r") as f:
        URL= f.readline().strip()

    return URL 

file_content = {}
with open("output.txt","r") as f:
    for line in f:
        word, count = line.strip().split(" ", maxsplit=1) 
        count = count.split("(")[1:]

        for i,c in enumerate(count):

            count[i] = list(map(int,c.strip("()").split(",")))
        
        file_content[word] = [[getURL(c[0]), c[1]] for c in sorted(count,reverse=True, key=lambda x: x[1])]

    #print(getURL(file_content[0]["count"][0][0])) 

with open("db.json", "w") as f:
    json.dump(file_content,f)
# word => [[doc,max]...[doc,min]]
