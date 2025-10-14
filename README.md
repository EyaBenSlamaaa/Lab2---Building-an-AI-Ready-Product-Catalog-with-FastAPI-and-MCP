# Product Catalog API + MCP Server

## Description
Ce projet fournit une **API de catalogue de produits** avec FastAPI et l’expose comme outils AI via FastMCP.  
Il peut être utilisé avec des agents AI comme **Claude Desktop**.

- **FastAPI** : endpoints pour lister tous les produits et récupérer un produit par ID.  
- **FastMCP** : expose ces endpoints comme outils appelables par AI.

---

## Structure du projet

product-catalog-lab/
│
├─ main.py # FastAPI application
├─ mcp_server.py # MCP server exposant les outils
├─ venv/ # environnement virtuel Python
└─ README.md

yaml
Copier le code

---

## Installation et setup

1️⃣ Cloner le dépôt et entrer dans le projet
git clone <votre-repo-url>
cd product-catalog-lab

2️⃣ Créer et activer un environnement virtuel
python -m venv venv
# Windows
venv\Scripts\activate
# Linux / macOS
source venv/bin/activate

3️⃣ Installer les dépendances
pip install fastapi[all] uvicorn fastmcp

4️⃣ Part 1: FastAPI Product Catalog
Démarrer le serveur
uvicorn main:app --host localhost --port 8000 --reload

Tester les endpoints

Lister tous les produits

curl http://localhost:8000/products


Récupérer un produit par ID

curl http://localhost:8000/products/1


Swagger UI

http://localhost:8000/docs

OpenAPI schema

curl http://localhost:8000/openapi.json > openapi.json

5️⃣ Part 2: MCP Server (FastMCP)
Démarrer le serveur MCP

Dans un nouveau terminal :

venv\Scripts\activate
python mcp_server.py


Outils exposés : list_products et get_product.

Configurer Claude Desktop

Ouvrir Claude Desktop → Paramètres → Développeur → Éditer config

Ajouter la configuration MCP :

{
  "mcpServers": {
    "product-catalog": {
      "command": "C:\\Users\\eyabe\\product-catalog-lab\\venv\\Scripts\\python.exe",
      "args": ["C:\\Users\\eyabe\\product-catalog-lab\\mcp_server.py"]
    }
  }
}


Redémarrer Claude Desktop.

Activer les outils dans un chat
Recherche et outils → Sélectionnez "product-catalog-mcp"

Tester les requêtes

Lister tous les produits

Récupérer un produit par ID (ex. 2)





