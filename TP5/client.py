from flask import Flask, render_template, request
import requests

app = Flask(__name__)

# Configuration de l'API FastAPI
API_URL = "http://44.202.201.45:5000"  # Remplacez par l'URL de votre API FastAPI

@app.route("/")
def index():
    """Page d'index affichant la liste des noms d'animaux."""
    try:
        response = requests.get(f"{API_URL}/animaux/noms")
        response2 = requests.get(f"{API_URL}/animaux/ids")
        response.raise_for_status()
        response2.raise_for_status()
        noms = response.json()
        ids = response2.json()
    except requests.exceptions.RequestException as e:
        noms = []
        ids = []
        print(f"Erreur lors de la récupération des noms ou ids d'animaux : {e}")
    return render_template("index.html", noms=noms, ids=ids)

@app.route("/fiche/<int:animal_id>")
def fiche(animal_id):
    """Page descriptive d'un animal."""
    try:
        response = requests.get(f"{API_URL}/animaux/{animal_id}")
        response.raise_for_status()
        animal = response.json()
    except requests.exceptions.RequestException as e:
        animal = None
        print(f"Erreur lors de la récupération de l'animal : {e}")
    return render_template("fiche.html", animal=animal)

@app.route("/mentions-legales")
def mentions_legales():
    """Page des mentions légales."""
    return render_template("mentions_legales.html")

@app.route("/admin")
def admin():
    """Page des mentions légales."""
    return render_template("admin.html")

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=8080)
