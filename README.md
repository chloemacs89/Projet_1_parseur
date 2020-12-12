# Description

Ce script permet de parser le site internet "http://books.toscrape.com" afin de pouvoir récupérer
les informations suivantes et de les stocker dans un fichier .csv :

- product_page_url
- universal_ product_code (upc)
- title
- price_including_tax
- price_excluding_tax
- number_available
- product_description
- category
- review_rating
- image_url

# Utilisation

Pour utiliser le script, vous devez posséder, au minimum, la version 3.8.0 de Python et avoir
installé les bibliothèques contenues dans le fichier requirements.txt.

Pour l'activiter, il convient d'entrer **python parseur_individuel.py <URL_du_livre>** en ligne de
commande.

Si le script s'éxécute correctement, ce dernier demandera à l'utilisateur de préciser le
nom du fichier dans lequel il souhaite déposer les informations recherchées. Si le fichier n'existe
pas, il est créé dans le répertoire où est exécuter le script. Si le fichier existe déjà, il n'est
pas écrasé, et les informations demandées seront ajouter à la suite de celles déjà présentes dans le
fichier. 


