import requests
from bs4 import BeautifulSoup

# Définition du tag cible et de l'URL de la page à scraper
targetTag = "ResultsContainer"
URL = "https://realpython.github.io/fake-jobs/"

# Envoi d'une requête HTTP pour récupérer le contenu brut HTML de la page
page = requests.get(URL)

# Initialisation de BeautifulSoup pour analyser le contenu HTML
soup = BeautifulSoup(page.content, "html.parser")

# Recherche de l'élément HTML par son ID (ici, ResultsContainer)
results = soup.find(id=targetTag)

# Filtrage des offres d'emploi contenant le mot "python" dans un élément h2
python_jobs = results.find_all(
    "h2", string=lambda text: "python" in text.lower()
)

# Récupération des éléments complets de chaque offre d'emploi Python (remontée jusqu'au conteneur parent)
python_jobs_elements = [
    h2_element.parent.parent.parent for h2_element in python_jobs
]

# Parcours des offres d'emploi Python trouvées et extraction des informations pertinentes
for job_element in python_jobs_elements:
    # Extraction du titre de l'offre (h2), de l'entreprise (h3) et de la localisation (p)
    title_element = job_element.find("h2", class_="title")
    company_element = job_element.find("h3", class_="company")
    location_element = job_element.find("p", class_="location")

    # Affichage des informations extraites (titre, entreprise, localisation) en supprimant les espaces superflus
    print(title_element.text.strip())
    print(company_element.text.strip())
    print(location_element.text.strip())

    # Recherche du lien "Apply" et affichage du lien de candidature si disponible
    links = job_element.find_all("a")
    if len(links) > 1:
        link_url = links[1]["href"]
        print(f"Apply here: {link_url}\n")

    # Ajout d'une ligne vide pour séparer les différentes offres d'emploi affichées
    print()
