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

Pour l'activiter, il convient d'entrer **python parseur_complet.py** en ligne de
commande. Aucune argument n'est à donner dans la ligne de commande. 

Si le script s'éxécute correctement, ce dernier demandera à l'utilisateur de préciser la catégorie
qu'il souhaite scrapper ainsi que le nom du fichier dans lequel il souhaite déposer les informations
recherchées. Si aucune catégorie spécifique n'est demandée, l'ensemble du site est alors scrapper. 

Si le fichier n'existe pas, il est créé dans le répertoire où est exécuter le script. Si le fichier existe déjà, iln'est pas écrasé, et les informations demandées seront ajouter à la suite de celles déjà présentes dans le fichier.

Le script fait appel au module parseur_individuel.py qui se charge de collecter les informations de
chaque livre présent dans la catégorie demandée. Vous avez la possibilité de l'utiliser
individuellement en entrant **python parseur_individuel.py <URL du livre>**. 


