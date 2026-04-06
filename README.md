# SenSante 🏥

Assistant de pré-diagnostic médical pour le Sénégal.

## Description

SenSante utilise le Machine Learning pour aider au pré-diagnostic des maladies courantes (paludisme, grippe, typhoïde) à partir des symptômes du patient.

## Structure du projet

- `data/` : Données patients (CSV)
- `models/` : Modèle ML (à venir)
- `api/` : API FastAPI (à venir)
- `frontend/` : Interface web (à venir)
- `notebooks/` : Scripts d’exploration (exploration.py)

## Installation

Créer un environnement virtuel :

python -m venv venv  
venv\Scripts\activate  

Installer les dépendances :

pip install -r requirements.txt

## Analyse des données

Le script `exploration.py` permet de :

- afficher les diagnostics  
- calculer la température moyenne par maladie  
- identifier la maladie la plus fréquente  

## Version

Version actuelle : v0

## Auteur

Yaye Mareme Diop - L2 GLSI - ESP / UCAD

## Cours

Intégration de Modèles IA - Dr. El Hadji Bassirou TOURE