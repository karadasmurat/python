import requests
import cloudscraper
from lxml import etree
from bs4 import BeautifulSoup
import time
import urllib.parse
import pandas as pd
import math

# url_hemen = "https://www.migros.com.tr/rest/hemen/search/screens/money-indirimli-market-urunleri-dt-5?reid=1710176183071000028"
url_hemen = "https://www.migros.com.tr/rest/hemen/products/search?discount-type=MCC&sayfa=1&sirala=cok-satanlar&reid=1710176183071000028"
url_hemen_part1 = "https://www.migros.com.tr/rest/hemen/products/search?discount-type=MCC&sayfa="
url_hemen_part2 = "&sirala=cok-satanlar"

cookie_sahibinden = "st=ac8fe03a2726c481da9aa2f881e456a1bcb60af5dbdcc72bb1f030d1d3d01537380b954b02fda9696cd1013f979e499761e061afd785f49fd; vid=245; cdid=u85EKjH9iqeOwYDn65f7d417; csss=JIxey7FvSKONsAEJThVtc0GS7mzyfwvr3D6y1FhDQ2jAJklfk4g0PfkhbyF3vQro8gBLNJEhsKuAhudXwlZ_dA; csls=B0VA_8_jusZTL20-BXI_ua14Dr0tITKKVUMkwws87-i-A3cHFAYXH85TBpMkH-GnAGRjVtAySZ4JHd1QSt54pQ; csid=8u0zj7zFJNTytsG7QVsO4H69eXGOMLV43dxoKNrATzRXPIfbdYNMmx5jfaQ8WgyW_74lZ6GhIJchkqyZjvaRsDWO2TP9dK0OnW2dr-u7Y70C2CCwYdBOPwi03fGDuButpkFPXJ_ouD0Yx2q7ZRFBssW0s87yRxEWbIsEXjfUGqU5uqjhyaV_bEhy53X87qPKiGD1YqfH01tS9EEN4EYnz5y3NYyYjP0bgShflFQcw2GThj9pzAQfcwgp6YJ7_wd8_f73rhjwbeqHxxfPu34HkKNvxTQ_tLG343YA-pmf2cZfngUg_1EbUC98wxW1LYc5xQ6G_dvJHAZpIxVh3og0X9i4hSEvrPhgPg1fE-NuRi8sSSCc5aRbNMZKeW4LKPLo; __cf_bm=fcvYndCW4pxiNpK.E6IQtn8yxjMdkbsGGI5NT.dVHRs-1710740503-1.0.1.1-qBAaL1GlaS0PuooVdLN5bSUBPluRYzfveVo6.GFcUZfibpGA9tDcn8KNE_I_seGwaS59J5ONv3pZQ2OqDZwusA; __cflb=0H28vudCb12J6LVB9qNjWurRvgFyPgDAXSkiei82kK5; nwsh=std; showPremiumBanner=false; dp=1920*1080-landscape; MS1=; geoipCity=istanbul; geoipIsp=turkcell_superonline; __ssid=147f3c2928c3c271d6c9d176e622341; cf_clearance=g4HVbFBSJiWQT0GJSFrMCz6b3YIkEybutnYrvr1BtL0-1710740511-1.0.1.1-wgZ9CrNDDELBsBuQM8gKHnrwMvPLGYp6KXMqOeZH9BGJ1uYps9AZTBtR_CCKQUvd4sFp7o7SXsnYRj_GsPhOig; _gcl_au=1.1.2071832485.1710740511; __gads=ID=ba5825e8e2ef16a8:T=1710740511:RT=1710740511:S=ALNI_MZxZbbgvOTtZJm4ldM7wZDHPl-Alw; __gpi=UID=00000d74f66a2f6a:T=1710740511:RT=1710740511:S=ALNI_MZ6W_qAvv9HzWUtC1sX2k3CdGDrSw; __eoi=ID=bdf30dfb8cc254db:T=1710740511:RT=1710740511:S=AA-Afjaw7zixnKwHc2F4iCPx_3Mn; _ga_CVPS3GXE1Z=GS1.1.1710740503.4.1.1710740514.49.0.0; _ga=GA1.2.2010616745.1710740512; _gid=GA1.2.1334290083.1710740514; _tt_enable_cookie=1; _ttp=3TdjYJtFkEAMUidSyX2TacRKrnY; _dc_gtm_UA-235070-1=1; OptanonConsent=isGpcEnabled=0&datestamp=Mon+Mar+18+2024+08%3A42%3A06+GMT%2B0300+(GMT%2B03%3A00)&version=202310.2.0&browserGpcFlag=0&isIABGlobal=false&consentId=1ccdb54a-761f-4cc9-8c2b-1e0ab65c4f2f&interactionCount=1&landingPath=https%3A%2F%2Fwww.sahibinden.com%2Farazi-suv-pickup-kia-sorento-2.5-crdi%3Fa277_max%3D2007%26pagingSize%3D50%26a277_min%3D2007&groups=C0004%3A0%2CC0001%3A1%2CC0003%3A0%2CC0002%3A0&hosts=H131%3A0%2CH108%3A0%2CH97%3A0%2CH110%3A0%2CH76%3A0%2CH77%3A0%2CH147%3A0%2CH78%3A0%2CH98%3A0%2CH79%3A0%2CH106%3A0%2CH58%3A0%2CH174%3A0%2CH8%3A0%2CH80%3A0%2CH67%3A0%2CH27%3A0%2CH14%3A0%2CH82%3A0%2CH83%3A0%2CH99%3A0%2CH10%3A0%2CH31%3A0%2CH114%3A0%2CH84%3A0%2CH175%3A0%2CH176%3A0%2CH115%3A0%2CH117%3A0%2CH100%3A0%2CH87%3A0%2CH88%3A0%2CH119%3A0%2CH89%3A0%2CH3%3A1%2CH4%3A0%2CH90%3A0%2CH91%3A0%2CH102%3A0%2CH5%3A0%2CH140%3A0%2CH93%3A0%2CH103%3A0%2CH94%3A0%2CH61%3A0%2CH36%3A0%2CH141%3A0%2CH122%3A0%2CH96%3A0%2CH104%3A0%2CH125%3A0%2CH105%3A1%2CH142%3A0&genVendors="


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
    hdrs = {
        "Cookie": cookie_sahibinden,
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36"
    }
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
            km = tr.contents[7].text.strip().replace(".", "_")
            price = tr.contents[11].text.strip().split()[0].replace(
                ".", "_")  # "620.000 TL" -> 620_000
            cars.append({"year": year, "km": km, "price": price})

    # print(len(cars), cars)


def get_url(offset, size=50):
    return f"https://www.sahibinden.com/arazi-suv-pickup-kia-sorento-2.5-crdi?a277_max=2007&&pagingOffset={offset}&pagingSize={size}&a277_min=2007"


def sahibinden():
    paging_size = 50
    url = get_url(offset=0, size=paging_size)
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

    pageCount = math.ceil(cnt / paging_size)
    # print(f"DEBUG: results: {cnt} pageSize: {paging_size} pageCount: {pageCount}")

    # get all pages one by one for the resultset
    for i in range(pageCount-1):
        url = url = get_url(offset=(i+1)*paging_size, size=paging_size)
        # print("DEBUG: Visiting next page: ", url)
        soup = get_soup(url)
        process_sahibinden(soup, cars)
        time.sleep(0.5)

    # pandas DataFrame from a list of dictionaries
    df = pd.DataFrame.from_dict(cars)
    print(df)


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
