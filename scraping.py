import requests
from bs4 import BeautifulSoup

# Récupération du tags ciblé et de l'url de la page
targetTag = "ResultsContainer"
URL = "https://realpython.github.io/fake-jobs/"
# Récupération des données brutes de la page en HTML
page = requests.get(URL)

# Affectation du contenu dans l'instance Beautiful soup
soup = BeautifulSoup(page.content, "html.parser")
# Récupération du contenu selon l'ID d'un TAG
results = soup.find(id=targetTag)
# Récupération des jobs selon la class ".card" en type ResultSet
job_elements = results.find_all("div", class_="card-content")
#print(type(job_elements))
# Affichage du résultats
for job_element in job_elements:
    # Récupération de chaques éléments HTML pertinent h2, h3, p
    title_element = job_element.find("h2", class_="title")
    company_element = job_element.find("h3", class_="company")
    location_element = job_element.find("p", class_="location")

    # Affichage du contenu de chaque éléments HTML + suppression de l'espace avant et après
    print(title_element.text.strip())
    print(company_element.text.strip())
    print(location_element.text.strip())
    print()