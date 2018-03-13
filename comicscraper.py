import requests, json, re
from requests import get
def main():
    n = 1
    check = True
    while check == True:
        check = scrape(n)
        n = n+1
def scrape(n):
    if n > 403:
        n = n+1
    url = 'https://xkcd.com/%d/info.0.json' %n
    r = requests.get(url)
    if r.status_code == 200:
        file = open("content.txt","a")
        content = r.json()["transcript"]
        content = re.sub(r"\[\[\s*(.*?)\s*\]\]","",content)
        content = re.sub(r"\{\{\s*(.*?)\s*\}\}","",content)
        content = re.sub(r"\"","'",content)
        file.write(r.json()["title"])
        file.write("\n")
        file.write(content)
        file.write(r.json()["alt"])
        file.write("\n")
        file.write("\n")
        filename = "images/%d.png" %n
        #download(r.json()["img"],filename)
        print(n)
        return True
    else:
        print("Error!")
        print(n)
        print(r.status_code)
        return False

def download(url,filename):
    with open(filename, "wb") as file:
        response = get(url)
        file.write(response.content)

if __name__ == "__main__":
    main()
