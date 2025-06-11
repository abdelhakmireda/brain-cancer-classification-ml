# Utiliser une image Python officielle
FROM python:3.10

# Définir le répertoire de travail dans le conteneur
WORKDIR /app

# Copier les fichiers nécessaires
COPY requirements.txt ./
COPY hassna.py ./  

# Installer les dépendances
RUN pip install --no-cache-dir -r requirements.txt

# Exposer le port utilisé par Streamlit
EXPOSE 8501

# Commande pour exécuter l'application
CMD ["streamlit", "run", "hassna.py", "--server.port=8501", "--server.address=0.0.0.0"]