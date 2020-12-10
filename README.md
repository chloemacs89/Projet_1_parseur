# Description

Ce script permet de parser le site internet "http://books.toscrape.com" afin de pouvoir récupérer
les informations suivantes et de les stocker dans un fichier .csv :
product_page_url
- universal_ product_code (upc)
- title
- price_including_tax
- price_excluding_tax
- number_available
- product_description
- category
- review_rating
- image_url

Pour le moment, le script ne permet de récupérer les informations que d'un seul livre.

# Utilisation

Pour utiliser le script, vous devez posséder, au minimum, la version 3.8.0 de Python et avoir
installé les biblithèques contenues dans le fichier requirements.txt.

Pour l'activiter, il convient d'entrer python parseur_individuel.py <URL_du_livre> en ligne de
commande. Si le script s'éxécute correctement, ce dernier indiquera avoir dépôsé les informations
dans un fichier "name.csv" ainsi que le chemin pour y accéder (qui devrait être votre répertoire courant)


