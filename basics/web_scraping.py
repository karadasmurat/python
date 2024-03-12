import requests
import cloudscraper
from lxml import etree
from bs4 import BeautifulSoup
import time
import urllib.parse

# url_hemen = "https://www.migros.com.tr/rest/hemen/search/screens/money-indirimli-market-urunleri-dt-5?reid=1710176183071000028"
url_hemen = "https://www.migros.com.tr/rest/hemen/products/search?discount-type=MCC&sayfa=1&sirala=cok-satanlar&reid=1710176183071000028"
url_hemen_part1 = "https://www.migros.com.tr/rest/hemen/products/search?discount-type=MCC&sayfa="
url_hemen_part2 = "&sirala=cok-satanlar"


class Product:
    def __init__(self, n: str, r: float, p: float, i: str):
        self.name = n
        self.discount_rate = r
        self.sale_price = p
        self.img = i

    def __eq__(self, other):
        return self.discount_rate == other.discount_rate

    def __lt__(self, other):
        return self.discount_rate < other.discount_rate

    # note that str has a calculated field!
    def __str__(self) -> str:
        return f"Product({self.name}, {self.discount_rate}, {self.sale_price}, \nhttps://www.migros.com.tr/hemen/arama?q={urllib.parse.quote(self.name)})"

    def html_component(self):
        # return f"<div><span class='badge text-bg-secondary'>{self.discount_rate}</span><span>{self.sale_price}</span><a href='https://www.migros.com.tr/hemen/arama?q={urllib.parse.quote(self.name)}'><img src='{self.img}'/></a></div>"

        return f'<div class="col><div class="card" style="width: 12rem;"><a href="https://www.migros.com.tr/hemen/arama?q={urllib.parse.quote(self.name)}"><img src="{self.img}" class="card-img-top" alt="..."></a><div class="card-body"><h5 class="card-title">{self.name}</h5><p class="card-text"> {self.sale_price}</p><span class="badge rounded-pill text-bg-warning">{self.discount_rate}</span></div></div>'


def html_out(fname, seq, mode="a"):
    with open(fname, mode) as file:
        file.write('<html><head><link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-T3c6CoIi6uLrA9TneNEoa7RxnatzjcDSCmG1MXxSR1GAsXEV/Dwwykc2MPK8M2HN" crossorigin="anonymous"></head><body><div class="container text-center"><div class="row mb-3">')

        for item in seq:
            file.write(item.html_component())

        file.write("</div></div></body></html>")


def http_basics():
    print("HTTP Basics")
    print("-----------")
    print("GET")

    res = requests.get('http://www.google.com')
    # 200 text/html; charset=ISO-8859-1
    print(res.status_code, res.headers['Content-Type'])
    print(res.text)  # <!doctype html><html ...


def json_get():
    print("JSON Decoding")
    print("-------------")

    res = requests.get('https://jsonplaceholder.typicode.com/todos/1')

    # 200 application/json; charset=utf-8
    print(res.status_code, res.headers['Content-Type'])
    # {'userId': 1, 'id': 1, 'title': 'delectus aut autem', 'completed': False}
    print(res.json())


def xml_get_unblocked(url):
    # cloudscraper
    scraper = cloudscraper.create_scraper(delay=10, browser="chrome")
    res = scraper.get(url)

    print(res.status_code, res.headers['Content-Type'])
    # print(res.content)

    return res.content


def getPageCount(content):
    soup = BeautifulSoup(content, 'lxml-xml')

    pageCount = int(soup.AppResponse.data.pageCount.string)
    return pageCount


def process_response(content, products):
    print("Processing content")

    soup = BeautifulSoup(content, 'lxml-xml')
    # print(soup.prettify())

    container = soup.storeProductInfos

    for product in container.children:
        name_tag = product.find('name')
        if name_tag:  # Check if the tag exists
            # print(name_tag.text)  # Access the text content of the name tag
            prod = Product(name_tag.text, float(product.discountRate.string), float(
                product.shownPrice.string)/100, product.images.images.urls.PRODUCT_LIST.string)

            # print(prod)
            products.append(prod)


def hemen():
    print("Hemen!")
    print("------")

    products = []

    # initial response is used to get pageCount
    content = xml_get_unblocked(url_hemen)
    process_response(content, products)

    pageCount = getPageCount(content)
    for i in range(pageCount-1):
        url_next_page = f"{url_hemen_part1}{i+2}{url_hemen_part2}"
        print("repeat for page: ", url_next_page)
        content = xml_get_unblocked(url_next_page)
        process_response(content, products)
        time.sleep(0.5)

    print("items: ", len(products))
    # sort descending, highest discount_rate first
    products.sort(key=lambda p: p.discount_rate, reverse=True)

    # for p in products:
    #    print(p.html_component())

    # save to file, write mode
    html_out("hemen.html", products, "w")


def webscraping_basics():
    print("Web Scraping Basics")
    print("--------------------")

    content = xml_get_unblocked(url_hemen)

    # using Python’s html.parser
    # soup = BeautifulSoup(content, 'html.parser')

    # using lxml parser
    soup = BeautifulSoup(content, 'lxml-xml')

    # print(soup.prettify())

    # Certain tags in HTML documents can be accessed by properties
    # print(soup.title) # <title>Example Domain</title>

    # Find Elements by ID
    # id attribute makes the element uniquely identifiable on the page
    # soup.find(id="link3")

    # find(): find a tag by name
    # For convenience, just saying the name of the tag you want is equivalent to find()
    print(soup.AppResponse.data.metaData.title)
    pageCount = int(soup.AppResponse.data.pageCount.string)
    print("Page count, no cookies: ", pageCount)
    print(soup.AppResponse.data.hitCount)

    # container = soup.find('storeProductInfos')
    container = soup.storeProductInfos
    # print(container)

    # .children: a tag’s direct children
    # .string
    for product in container.children:
        name_tag = product.find('name')
        if name_tag:  # Check if the tag exists
            # print(name_tag.text)  # Access the text content of the name tag
            prod = Product(name_tag.text, float(product.discountRate.string), float(
                product.salePrice.string)/100)

            print(prod)
            # print( f"discount: %{product.discountRate.string} salePrice: {float(product.salePrice.string)/100}")

    # image: {product.images.images.urls.PRODUCT_LIST.string}
    # find_all(): get all the tags
    # products = soup.find_all('storeProductInfos')
    # for p in products:
    #    print(p.name.text)
