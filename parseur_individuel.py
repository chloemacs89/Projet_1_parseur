import requests as rq
from bs4 import BeautifulSoup as bfs
import re
import sys
import csv

if len(sys.argv) != 2:
    print("Vous ne devez passer qu'un seul argument dans la commande.")
    print("Cet argument doit nécessairement être l'URL du livre concerné.")
    quit()

url = sys.argv[1]

response = rq.get(url)

response.encoding = "utf-8"


def productDescription(response):
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


def dumpIntoCSV(response):
    """
    Récupère tous les dictionnaires des différentes fonctions et les
    cumule dans un dictionnaire dont les keys servent à initialiser
    les champs du fichier csv, puis d'y écrire les values correspondates. 
    """
    bookInfo = {
        **productDescription(response),
        **productUrl(response),
        **productTitle(response),
        **productImg(response)
    }
    with open("name.csv", "w+", newline='') as csvfile:
        columnNames = bookInfo.keys()
        writer = csv.DictWriter(csvfile, fieldnames=columnNames)
        writer.writeheader()
        writer.writerow(bookInfo)
        print("dépôt des information dans le fichier : ./name.csv")


dumpIntoCSV(response)
