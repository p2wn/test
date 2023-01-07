import requests, sys

l = []
def scrape(url):
    try:
        text = requests.get(url).text
        for x in text.split("\n"):
            if len(x) > 5 and ":" in x:
                l.append(x.replace("\n", ""))
    except:
        print("Error: invalid url")
if len(sys.argv) > 1:
    scrape(str(sys.argv[1]))
    file = open("scraped.txt", "w")
    file.write("\n".join(l))
    file.close()
else:
    print("Error: provide an url")
