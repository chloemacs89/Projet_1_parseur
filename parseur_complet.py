from parseur_individuel import dumpIntoCSV
from bs4 import BeautifulSoup as bfs
import requests as rq
import sys


def makeCategoryList(response, url):
    """
    Renvoie un dictionnaire qui associe le nom des catégories à l'URL
    de la première page de chacune de ces catégories.
    """
    categoryDict = {}
    soup = bfs(response.text, features="html.parser")
    getCategory = soup.find("ul", class_="nav nav-list")
    for category in getCategory.findAll("li"):
        catLink = url + category.a.get("href")
        catName = category.a.text.strip()
        categoryDict[catName.capitalize()] = catLink.rstrip("index.html")

    return categoryDict


def getBookPageUrl(response, url, baseUrl):
    """
    Retourne la liste des URL de chacun des livres à scrapper. 
    Cette liste peut ensuite être parcouru pour extraire les informations
    demandées.
    """
    bookUrlList = []
    everyPageUrl = [url + "index.html"] + getCategoryPagesUrl(
        response, url, baseUrl)

    for page in everyPageUrl:
        response = rq.get(page)
        soup = bfs(response.text, features="html.parser")
        bookLink = soup.findAll("h3")
        for link in bookLink:
            bookUrlList.append("http://books.toscrape.com/catalogue/" +
                               link.a["href"].strip("../../../"))

    return bookUrlList


def getNextPageUrl(response, url, baseUrl):
    """
    Renvoie l'URL de la prochaine page à ajouter dans la liste
    des URL des pages de la catégorie demandée.
    """
    soup = bfs(response.text, features="html.parser")
    pager = soup.find("ul", class_="pager")
    if pager:
        nextUrl = pager.find("li", class_="next")
        if nextUrl:
            newUrl = nextUrl.a.get("href").lstrip("catalogue/")
            return baseUrl + newUrl
    else:
        return False


def getCategoryPagesUrl(response, url, baseUrl, urlList=[]):
    """
    Renvoie la liste de l'ensemble des URL des pages de la catégorie
    choisie. 
    """
    if getNextPageUrl(response, url, baseUrl):
        url = getNextPageUrl(response, url, baseUrl)
        urlList.append(url)
        response = rq.get(url)
        getCategoryPagesUrl(response, url, baseUrl, urlList)

    return urlList


def categoryChoice(response, url):
    soup = bfs(response.text, features="html.parser")
    catList = makeCategoryList(response, url)
    print("Vous pouvez choisir de scrapper une catégorie particulière.")
    print("Si vous répondez 'non' à la question ci-dessous, la totalité du site sera scrappé.")
    choice = input("Souhaitez-vous selectionner une catégorie (oui/non) : ").lower()
    if choice == "oui":
        print(50 * "-")
        print("Choisissez la catégorie à scrapper parmis les catégories suivantes :")
        print(50 * "-")
        for catNum, catName in enumerate(catList.keys()):
            print(catNum + 1, ":", catName)
        print(50 * "-")
        catChoice = input("Nom de la catégorie que vous souhaitez scrapper : ").capitalize()
        if catChoice in catList.keys():
            print(f"La catégorie {catChoice} va être scrappée !")
            return catList[catChoice]
        else:
            print("Catégorie inconnue !")
            return False
    elif choice == "non":
        print("L'ensemble du site va être scrappé !")
        return catList["Books"]
    else:
        print("Choix invalide")
        return False


def main():
    url = "https://books.toscrape.com/"
    response = rq.get(url)
    response.encoding = "utf-8"
    catUrl = categoryChoice(response, url)
    csvFileName = input("Choisissez le nom du fichier csv (inutile de préciser .csv) : ") + ".csv"
    if catUrl:
        for livre in getBookPageUrl(response, catUrl, catUrl):
            pageLivre = rq.get(livre)
            pageLivre.encoding = "utf-8"
            dumpIntoCSV(pageLivre, csvFileName)

    print(50*"-")
    print("Opération terminée")


main()
