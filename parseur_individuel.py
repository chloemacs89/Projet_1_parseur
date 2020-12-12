import requests as rq
from bs4 import BeautifulSoup as bfs
import sys
import os
import csv

def productInformation(response):
    """
    La fonction récupère les informations contenues dans
    la partie 'Production Description' du site. Elles sont
    stockées dans un dictionnaire
    """
    tdList = []
    thList = []
    soup = bfs(response.text, features="html.parser")
    tdTag = soup.findAll("td")
    thTag = soup.findAll("th")
    for td in tdTag:
        tdList.append(td.text)
    for th in thTag:
        thList.append(th.text)
    return dict(zip(thList, tdList))


def productionDescription(response):
    soup = bfs(response.text, features="html.parser")
    descriptionText = soup.find("article", class_="product_page")
    return {"Production_Description": descriptionText.findAll("p")[3].text}


def productUrl(response):
    return {"url": response.url}


def productTitle(response):
    soup = bfs(response.text, features="html.parser")
    return {"Title": soup.find("h1").text}


def productImg(response):
    soup = bfs(response.text, features="html.parser")
    return {
        "imgUrl":
        "http://books.toscrape.com/" + soup.find("img")["src"].strip("../../")
    }


def productRating(response):
    rateValues = {"One": 1, "Two": 2, "Three": 3, "Four": 4, "Five": 5}
    soup = bfs(response.text, features="html.parser")
    rating = soup.find("p", class_="star-rating")
    starRating = rating.attrs["class"][1]
    return {"review_rating": rateValues[starRating]}


def productCategory(response):
    soup = bfs(response.text, features="html.parser")
    category = soup.find("ul", class_="breadcrumb")
    return {"category": category.findAll("a")[2].text}


def dumpIntoCSV(response, csvFileName):
    """
    Récupère tous les dictionnaires des différentes fonctions et les
    cumule dans un dictionnaire dont les keys servent à initialiser
    les champs du fichier csv, puis d'y écrire les values correspondates. 
    """
    bookInfo = {
        **productTitle(response),
        **productInformation(response),
        **productUrl(response),
        **productionDescription(response),
        **productCategory(response),
        **productRating(response),
        **productImg(response)
    }

    # Si le fichier n'existe pas, il est créé et les noms des champs
    # sont renseignés au passage. Sinon, les informations sont ajoutées
    # à la suite des valeurs déjà présentes
    if not os.path.exists(csvFileName):
        with open(csvFileName, "w+", newline='') as csvfile:
            columnNames = bookInfo.keys()
            writer = csv.DictWriter(csvfile, fieldnames=columnNames)
            writer.writeheader()

    with open(csvFileName, "a+", newline='') as csvfile:
        columnNames = bookInfo.keys()
        writer = csv.DictWriter(csvfile, fieldnames=columnNames)
        # writer.writeheader()
        writer.writerow(bookInfo)
        print(f"dépôt des information dans le fichier : {csvFileName}")


if __name__ == '__main__':
    if sys.argv != 2:
        print("Erreur : argument manquant ou argument en excès.")
        print("Fonctionnement : python parseur_livre.py <URL>")
        quit()

    url = sys.argv[1]
    response = rq.get(url)
    response.encoding = "utf-8"
    
    csvFileName = input("Nom du fichier csv (inutile de précise .csv) : ")

    dumpIntoCSV(response, csvFileName)

