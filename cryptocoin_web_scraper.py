import urllib2
from bs4 import BeautifulSoup


def get_quote_price(url):
    page = urllib2.urlopen(url)
    soup = BeautifulSoup(page, 'html.parser')
    price_box = soup.find(attrs={'id': 'quote_price'})
    price = price_box.text.strip()
    print(price)


marketPageList = ['https://coinmarketcap.com/currencies/ripple',
                  'https://coinmarketcap.com/currencies/iota',
                  'https://coinmarketcap.com/currencies/tron',
                  'https://coinmarketcap.com/currencies/bitcoin',
                  'https://coinmarketcap.com/currencies/ethereum',
                  'https://coinmarketcap.com/currencies/litecoin']

for url in marketPageList:
    get_quote_price(url)
