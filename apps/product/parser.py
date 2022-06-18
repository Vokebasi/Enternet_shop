
import decimal
import requests
from bs4 import BeautifulSoup as bs

url = "https://banks.kg/rates/usd"
headers = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
    "User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:101.0) Gecko/20100101 Firefox/101.0"
}

def parser():
    req = requests.get(url, headers=headers)
    soup = bs(req.text, 'lxml')
    dollar = soup.find('td', class_="bg-light").text.strip()
    return float(dollar)


if __name__ == "__main__":
    print(parser())


 