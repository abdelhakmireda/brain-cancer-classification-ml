# 🧠 Brain Cancer Classification ML

## 🚀 Présentation

Ce projet Streamlit propose une **classification du cancer du cerveau** à partir de données génomiques et cliniques.  
Il permet de prédire le diagnostic grâce à plusieurs modèles de Machine Learning populaires :

- Régression Logistique  
- K-Nearest Neighbors (KNN)  
- Arbre de Décision  
- Naïve Bayes  
- Support Vector Machine (SVM)  

Le projet supporte la génération de datasets simulés, l'import de données Kaggle, et le téléversement de fichiers CSV ou Excel utilisateur.  
Un pipeline complet de prétraitement est inclus, avec imputation, encodage, standardisation, et réduction de dimension par PCA.  

---

## 🎯 Fonctionnalités

- 🔄 Génération de datasets simulés personnalisés  
- 📥 Import automatique du dataset Kaggle "Brain Cancer Gene Expression"  
- 📂 Téléversement de vos propres fichiers CSV / Excel  
- 🔍 Évaluation et comparaison des modèles ML avec affichage des matrices de confusion  
- 📊 Visualisation interactive via Streamlit  
- 📥 Export des résultats au format CSV et Excel  

---

## ⚙️ Installation

1. Clonez le dépôt  
```bash
git clone https://github.com/ton-utilisateur/brain-cancer-classification-ml.git
cd brain-cancer-classification-ml
```
2. Installez les dépendances  
```bash
pip install -r requirements.txt
```
3. Lancez l’application Streamlit
```bash
streamlit run app.py
```
---

## 📂 Structure du projet

- `app.py` : Script principal de l’application Streamlit  
- `requirements.txt` : Liste des dépendances Python nécessaires  
- `dataset_simulé.csv` : Exemple de dataset généré automatiquement  
- `classification_results.csv` et `kaggle_classification_results.xlsx` : Fichiers exportés contenant les résultats des classifications  

---

## 🤝 Contribution

Les contributions sont les bienvenues !  
N’hésitez pas à ouvrir une issue ou une pull request pour proposer des améliorations, corriger des bugs, ou ajouter de nouvelles fonctionnalités.  

---

## 📞 Contact

Pour toute question ou suggestion, vous pouvez me contacter à : ton.email@example.com  

---

## 🎉 Remerciements

Merci d’avoir consulté ce projet !  
Si vous le trouvez utile, n’hésitez pas à lui donner une étoile ⭐ sur GitHub.
