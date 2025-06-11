# 🧠 Brain Cancer Classification ML

## 📌 Introduction

Bienvenue dans ce projet de classification du cancer du cerveau utilisant des techniques modernes de **Machine Learning** intégrées dans une interface **Streamlit** interactive.  
Ce système permet d’analyser des données génétiques et cliniques afin d’assister les chercheurs et professionnels de santé dans le **diagnostic prédictif** de différentes formes de tumeurs cérébrales.

---

## 🚀 Présentation du projet

Cette application met en œuvre plusieurs modèles de Machine Learning pour classifier les types de cancers du cerveau à partir de données génomiques, notamment :

- 🔹 Régression Logistique  
- 🔹 K-Nearest Neighbors (KNN)  
- 🔹 Arbre de Décision  
- 🔹 Naïve Bayes  
- 🔹 Support Vector Machine (SVM)  

Le projet propose une interface conviviale et pédagogique, prenant en charge :

- ✅ la génération de datasets simulés  
- ✅ l'import automatisé de données Kaggle  
- ✅ le téléversement de fichiers utilisateurs (CSV / Excel)  
- ✅ un pipeline de prétraitement complet : *nettoyage, imputation, standardisation, réduction de dimension (PCA)*  
- ✅ des visualisations détaillées et exportables des résultats

---

## 🎯 Fonctionnalités principales

- 🧬 **Import de données génomiques (CSV, Excel, Kaggle)**  
- 🔄 **Création dynamique de jeux de données simulés**  
- 🧠 **Classification multi-modèles avec matrices de confusion**  
- 📈 **Comparaison visuelle des performances des modèles**  
- 💾 **Export des résultats en formats Excel**  
- ⚙️ **Pipeline automatique de préparation des données**

---

## ⚙️ Installation manuelle (via `pip`)

1️⃣ Clonez ce dépôt :  
```bash
git clone https://github.com/ton-utilisateur/brain-cancer-classification-ml.git
cd brain-cancer-classification-ml
```
2️⃣ Installez les dépendances Python :  
```bash
pip install -r requirements.txt
```
3️⃣ Lancez l’application Streamlit :  
```bash
streamlit run hassna.py
```
---

## 🐳 Exécution avec Docker Compose (facultatif)

Si vous préférez un déploiement conteneurisé, utilisez simplement Docker Compose :

```bash
docker compose up --build
```
🔗 Une fois lancé, accédez à l'application sur :  
http://localhost:8501

---

## 📁 Structure du projet
## 📁 Organisation du projet

Ce projet est structuré de manière simple et lisible pour faciliter son utilisation, sa maintenance et son déploiement :

| Dossier/Fichier              | Description                                                                          |
|-----------------------------|--------------------------------------------------------------------------------------|
| `hassna.py`                 | Fichier principal contenant l'application Streamlit                                 |
| `requirements.txt`          | Liste des dépendances Python nécessaires au bon fonctionnement de l'application    |
| `Dockerfile`                | Fichier permettant de construire une image Docker de l'application                  |
| `docker-compose.yaml`       | Fichier de configuration pour lancer le projet via Docker Compose                   |
| `/data/`                    | (Optionnel) Dossiers contenant les jeux de données d'entrée                         |
| `/output/`                  | Dossier dans lequel les résultats sont exportés sous forme de fichiers Excel        |
| `/notebooks/`               | (Facultatif) Contient des explorations Jupyter ou des essais de modélisation        |
| `README.md`                 | Documentation complète du projet (le fichier que vous lisez actuellement)          |

Cette structure vous permet de retrouver rapidement ce que vous cherchez, que ce soit pour :  
✅ modifier l'interface,  
✅ mettre à jour les modèles,  
✅ ajouter des datasets,  
✅ ou exporter les résultats.

---


---

## 🤝 Contribution

Les contributions sont les bienvenues !  
Que vous souhaitiez proposer une nouvelle fonctionnalité, corriger un bug ou améliorer la documentation, n'hésitez pas à :

- Créer une **issue** pour signaler un problème  
- Soumettre une **pull request** pour proposer une amélioration

✨ Votre aide est précieuse et grandement appréciée.

---

## 📬 Contact

📧 Pour toute question, remarque ou proposition de collaboration :  
**reda.abdelhak.mi@gmail.com**

---

## 🎉 Conclusion

Ce projet vous offre un outil accessible, performant et interactif pour explorer la classification de données médicales complexes avec des techniques d'apprentissage automatique modernes.  
Grâce à l'interface Streamlit, vous pouvez tester plusieurs modèles, visualiser leurs performances et exporter vos résultats… sans écrire une seule ligne de code supplémentaire.

Merci pour votre intérêt 🙏  
⭐ Si vous trouvez ce projet utile, pensez à lui attribuer une étoile sur GitHub et à le partager avec vos collègues ou amis curieux !

---
