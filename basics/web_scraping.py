import requests
import cloudscraper
from lxml import etree
from bs4 import BeautifulSoup
import time
import urllib.parse
import pandas as pd
import math
from urllib.parse import urlencode

# url_hemen = "https://www.migros.com.tr/rest/hemen/search/screens/money-indirimli-market-urunleri-dt-5?reid=1710176183071000028"
url_hemen = "https://www.migros.com.tr/rest/hemen/products/search?discount-type=MCC&sayfa=1&sirala=cok-satanlar&reid=1710176183071000028"
url_hemen_part1 = "https://www.migros.com.tr/rest/hemen/products/search?discount-type=MCC&sayfa="
url_hemen_part2 = "&sirala=cok-satanlar"

COOKIE_SAHIBINDEN = "st=ae2dd4d990048486694e1a43f299e30eded4de64abad7cd37de07873629ed757016ed5936dd930b0e6bce35046457a5565dcd26049dc8c605; vid=846; cdid=G4ayfs4tzhY441MA65feb6d0; csss=fovznyyk7Xcfr899uS5y0bxFHbO_WfUjlmac3QpYInvogVs68uJqn7UIKd2dQAf0TFsUDBYnYJMY1ztWzpeurA; csls=tSiIWsc46GFEeZVBH1HGg-6fyK9mFGpHIbDFu8DuXraqjpVnzc_76WjC63v1w_zEvUJTWk1_kZJmzlyS4djjOw; csid=i168lz8RlGXZLt3ObQtN7ZDTef8OncUOnjii-kmAFkcThgjvAypKvy6xPeSHL-p1Nz3sUMvOChPbgu03t9LuPBsnsWvaNJmILkg0kEvckpAigaBqVeEU2_kn3belCUWp7xy3odJIRaWYrjn43KkZIIikmnw3udd3W4UJGTwy3DSHAXXAncu5JOrwlGjYPSuUuBMb_MF7kHBC2V9g3HxRwnoMkXkZQX7CXJo0ypxB29BfmVmahyH-SMQ2rPvhkW60LMSRTPAgKibMTEPS0_6Cy2FC1udfUaHgxILI0J8YItPGEp9dxcSFvZjjWo_gR4twCKV_2S-HHYs7kQUzoaWxy8RZDYGXIsnJly_RkU4sFjCEsZnyXEV8KCBDVV7HNF11; __cf_bm=q7Idr82sFHNI7tWQD9KxLVxbGF8nPAp72uTpluzYLdg-1711191760-1.0.1.1-qqgmZM5iMlZHM8hgyZ4K7DQSxzX7fkAZ8SZx2cJQYRyQa_p78mka3Vw1CodYVjZ3aDrZk8r4q36XnFKwkKsTtQ; __cflb=0H28vudCb12J6LVB9qNjWurRvgFyPgDAgwVd35Ma7J3; nwsh=std; MS1=; showPremiumBanner=false; _gcl_au=1.1.1627568293.1711191767; dp=1920*1080-landscape; geoipCity=istanbul; geoipIsp=turkcell_superonline; __ssid=02a16ca876219880136f2308f52bdfc; cf_clearance=pXfJ190T02nr1JP7oJtNsxAZQduGtpmdQWPwTazFXQs-1711191767-1.0.1.1-8gvDOw168TgfjJbKX4e6QJFhNHomrO.HbJlEonv1vM3nDP0qkFzGyRu2btRRxBmnSH4eFdy3pxWOzfpcCCYeBg; __gads=ID=f09185997e935248:T=1711191767:RT=1711191767:S=ALNI_MbEr2l4Y3TqXusoSSWhEHZt8mHkYQ; __gpi=UID=00000d8114ee0254:T=1711191767:RT=1711191767:S=ALNI_MYBnXg1r2gJHzOfxAn-nYHzG2pjTw; __eoi=ID=fd44d5bd90a3bfb3:T=1711191767:RT=1711191767:S=AA-AfjbsHBL6qgf5ZANBu9T8Parp; _gid=GA1.2.1277905064.1711191769; _dc_gtm_UA-235070-1=1; _ga_CVPS3GXE1Z=GS1.1.1711191735.3.1.1711191768.27.0.0; _ga=GA1.1.1430915538.1711191767; _tt_enable_cookie=1; _ttp=9lYx0P2DKd8ShPjUrN5inWAqhqj; _gali=div-gpt-ad-1343223117871-0; OptanonConsent=isGpcEnabled=0&datestamp=Sat+Mar+23+2024+14%3A02%3A57+GMT%2B0300+(GMT%2B03%3A00)&version=202310.2.0&browserGpcFlag=0&isIABGlobal=false&consentId=4b25e9e5-6191-4529-b5d7-bbd14628bba4&interactionCount=1&landingPath=https%3A%2F%2Fwww.sahibinden.com%2Farazi-suv-pickup-kia-sorento-2.5-crdi%3Fa277_max%3D2008%26pagingSize%3D50%26a277_min%3D2006&groups=C0004%3A0%2CC0001%3A1%2CC0003%3A0%2CC0002%3A0&hosts=H131%3A0%2CH108%3A0%2CH97%3A0%2CH110%3A0%2CH76%3A0%2CH77%3A0%2CH147%3A0%2CH78%3A0%2CH98%3A0%2CH79%3A0%2CH106%3A0%2CH58%3A0%2CH174%3A0%2CH8%3A0%2CH80%3A0%2CH67%3A0%2CH27%3A0%2CH14%3A0%2CH82%3A0%2CH83%3A0%2CH99%3A0%2CH10%3A0%2CH31%3A0%2CH114%3A0%2CH84%3A0%2CH175%3A0%2CH176%3A0%2CH115%3A0%2CH117%3A0%2CH100%3A0%2CH87%3A0%2CH88%3A0%2CH119%3A0%2CH89%3A0%2CH3%3A1%2CH4%3A0%2CH90%3A0%2CH91%3A0%2CH102%3A0%2CH5%3A0%2CH140%3A0%2CH93%3A0%2CH103%3A0%2CH94%3A0%2CH61%3A0%2CH36%3A0%2CH141%3A0%2CH122%3A0%2CH96%3A0%2CH104%3A0%2CH125%3A0%2CH105%3A1%2CH142%3A0&genVendors="
USER_AGENT = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36"
NUMBER_SEPERATOR = ""  # "_"


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
    scraper = cloudscraper.create_scraper(delay=10, browser={
        'browser': 'chrome',
        'platform': 'android',
        'desktop': False,
    })
    res = scraper.get(url)

    # DEBUG status code
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


def get_soup(url):
    # security issues - may get 403
    hdrs = {"Cookie": COOKIE_SAHIBINDEN, "User-Agent": USER_AGENT}
    res = requests.get(url, headers=hdrs)

    # DEBUG response
    print(res.status_code, res.headers['Content-Type'])
    # print(res.text)

    # content = xml_get_unblocked(url)
    # print(content)

    # using Python’s html.parser
    soup = BeautifulSoup(res.text, 'html.parser')

    # using lxml parser
    # soup = BeautifulSoup(res.text, 'lxml-xml')

    # DEBUG soup
    # print(soup.prettify())
    return soup


def process_sahibinden(soup, cars):
    # find with keyword arguments: id
    results_table = soup.find(id='searchResultsTable')
    # header_row = results_table.thead.tr
    # headers = header_row.find_all("td")
    # print(len(headers))

    # rows = results_table.tbody.tr
    # all rows (tr) under table.tbody
    rows = results_table.tbody.find_all("tr", class_="searchResultsItem")

    for tr in rows:
        # each row represents a result, which has cells (tds)
        # print("**** New record found.")
        # nativeAd
        if "nativeAd" in tr["class"]:
            print("AD FOUND.")
        else:
            # print(len(tr.contents))
            year = tr.contents[5].text.strip()

            # Python 3.6 now supports PEP515, and so you can use _ for float and integer literal readability improvement.
            km = tr.contents[7].text.strip().replace(".", NUMBER_SEPERATOR)
            price = tr.contents[11].text.strip().split()[0].replace(
                ".", NUMBER_SEPERATOR)  # "620.000 TL" -> 620_000
            pubdate = tr.contents[13].text.strip().replace("\n\n", " ")
            cars.append({"year": year, "km": km,
                        "price": price, "date": pubdate})

    # print(len(cars), cars)


def get_url(url, qparams):

    # f"https://www.sahibinden.com/arazi-suv-pickup-kia-sorento-2.5-crdi?a277_min={YEAR_MIN}&a277_max={YEAR_MAX}&pagingOffset={offset}&pagingSize={size}"

    encoded_url = f"{url}?{urlencode(qparams)}"
    print("DEBUG: ", encoded_url)
    return encoded_url


def get_next_page(url, qparams):
    qparams["pagingOffset"] = int(
        qparams["pagingOffset"])+50 if qparams["pagingOffset"] else 50
    return get_url(url, qparams)


def sahibinden():
    PAGING_SIZE = 50
    params = {'a277_min': 2006, "a277_max": 2008,
              "pagingOffset": 0, "pagingSize": PAGING_SIZE}

    url = get_url(
        url=f"https://www.sahibinden.com/arazi-suv-pickup-kia-sorento-2.5-crdi", qparams=params)
    cars = []

    soup = get_soup(url)

    # json list under <script type="application/ld+json">
    # cars = soup.find("script", attrs={"type": "application/ld+json"})
    # print(cars.string)

    # searchResults
    result_text = soup.find("div", class_="result-text-sub-group")
    # 160 ilan
    cnt = int(result_text.contents[2].contents[0].text.strip().split()[0])

    process_sahibinden(soup, cars)

    pageCount = math.ceil(cnt / PAGING_SIZE)
    # print(f"DEBUG: results: {cnt} pageSize: {paging_size} pageCount: {pageCount}")

    # get all pages one by one for the resultset
    for i in range(pageCount-1):
        # url = get_url(offset=(i+1)*PAGING_SIZE, size=PAGING_SIZE)
        url = get_next_page(url, params)
        print("DEBUG: Visiting next page: ", url)
        soup = get_soup(url)
        process_sahibinden(soup, cars)
        time.sleep(0.5)

    # pandas DataFrame from a list of dictionaries
    df = pd.DataFrame.from_dict(cars)
    print(df)
    df.to_csv("sahibinden_kia_2006-2008_202403.csv",
              encoding='utf-8', index=False)


def coin_stats():

    soup = get_soup('https://coinstats.app/coins/fetch-ai/')

    # print(soup.prettify())

    # print(soup.title)
    # <title>Fetch.ai Token Price, Charts  Market Insights | Your Crypto Hub</title>

    # print(soup.title.name)  # title

    # Convenience property to get the single string within this PageElement.
    # print(soup.title.string)
    # Fetch.ai Token Price, Charts  Market Insights | Your Crypto Hub

    # A tag’s children are available in a list called .contents
    # print(soup.head.contents[0])  # <meta charSet="utf-8"/>

    # Instead of getting them as a list, you can iterate over a tag’s children using the .children generator:
    # for head_child in soup.head.children:
    #    print(head_child)

    # As of Beautiful Soup 4.1.2, you can search by CSS class using the keyword argument class_:
    # stats = soup.find_all("div", class_= "jsx-916978830 market-stats-item ")
    # print(len(stats))
    # for stat in stats:
    #    pass
    #    print(stat)

    ath_title_tags = soup.find_all(
        "span", class_="jsx-916978830 market-stats-item_title_text")
    print("Found:", len(ath_title_tags))
    for t in ath_title_tags:
        if t.string == "All Time High":
            print(t.parent.next_sibling.find(
                "div", class_="jsx-2488791722 price-change-badge  price-down").contents[1].text)


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
