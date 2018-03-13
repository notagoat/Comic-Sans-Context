import requests, json, re
def main():
    n = 1
    check = True
    while check == True:
        scrape(n)
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
        content = re.sub(r"(\r\n|\r|\n)"," ",content)
        file.write(r.json()["title"])
        file.write("\n")
        file.write(content)
        file.write("\n")
        file.write(r.json()["alt"])
        file.write("\n")
        file.write("\n")
        print(n)
        return True
    else:
        print("Error!")
        print(n)
        print(r.status_code)
        return False

if __name__ == "__main__":
    main()
