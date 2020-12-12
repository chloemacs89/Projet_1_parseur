from parseur_individuel import dumpIntoCSV
from bs4 import BeautifulSoup as bfs
import requests as rq
import sys

url = "https://books.toscrape.com/catalogue/category/books/travel_2/index.html"

response = rq.get(url)

response.encoding = "utf-8"


def makeCategoryList(response):
    pass


def getBookPageUrl(response, url):
    bookUrlList = []
    everyPageUrl = [url] + getCategoryPagesUrl(response, url)
    print(everyPageUrl)

    for page in everyPageUrl:
        response = rq.get(page)
        soup = bfs(response.text)
        bookLink = soup.findAll("h3")
        for link in bookLink:
            bookUrlList.append("http://books.toscrape.com/catalogue/" +
                               link.a["href"].strip("../../../"))

    return bookUrlList


def getNextPageUrl(response, url):
    soup = bfs(response.text)
    pager = soup.find("ul", class_="pager")
    if pager:
        nextUrl = pager.find("li", class_="next")
        if nextUrl:
            newUrl = nextUrl.a.get("href")
            return "https://books.toscrape.com/catalogue/category/books/travel_2/" + newUrl
    else:
        return False


def getCategoryPagesUrl(response, url, urlList=[]):
    if getNextPageUrl(response, url):
        url = getNextPageUrl(response, url)
        urlList.append(url)
        response = rq.get(url)
        getCategoryPagesUrl(response, url, urlList)

    return urlList


for livre in getBookPageUrl(response, url):
    pagelivre = rq.get(livre)
    pagelivre.encoding = "utf-8"
    dumpIntoCSV(pagelivre, "site_complet.csv")
