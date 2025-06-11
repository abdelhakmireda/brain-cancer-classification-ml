import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.decomposition import PCA
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix, classification_report, accuracy_score
from sklearn.linear_model import LogisticRegression
from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.svm import SVC
from sklearn.impute import SimpleImputer

# Configurer l'interface Streamlit
st.set_page_config(page_title="Classification Cancer du Cerveau", layout="wide")
st.title("🧠 Classification des données du cancer du cerveau")
st.markdown("Prédiction du diagnostic avec différents modèles de Machine Learning")

# 📥 **Téléversement d'un fichier CSV**
uploaded_file = st.file_uploader("📤 Importez votre fichier CSV", type=["csv"])

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)

    st.success("✅ Données chargées avec succès !")
    st.write("### Aperçu du dataset :")
    st.dataframe(df.head())

    # 📌 **Prétraitement des données**
    df.dropna(how='all', axis=1, inplace=True)

    if 'samples' in df.columns and 'type' in df.columns:
        X = df.drop(columns=['samples', 'type'])
        y = df['type']
    else:
        st.error("❌ Colonnes 'samples' et 'type' absentes, vérifiez votre dataset.")
        st.stop()

    # Encoder les noms des classes
    encoder = LabelEncoder()
    y_encoded = encoder.fit_transform(y)
    class_names = encoder.classes_  # Récupérer les noms des classes

    # Normalisation des données
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)

    # Réduction de dimension avec PCA
    pca = PCA(n_components=2)
    X_pca = pca.fit_transform(X_scaled)

    # Séparation des données
    X_train, X_test, y_train, y_test = train_test_split(X_pca, y_encoded, test_size=0.2, random_state=42, stratify=y_encoded)

    # 📊 **Définition des modèles**
    models = {
        "Régression Logistique": LogisticRegression(),
        "KNN": KNeighborsClassifier(n_neighbors=5),
        "Arbre de Décision": DecisionTreeClassifier(),
        "Naïve Bayes": GaussianNB(),
        "SVM": SVC()
    }

    st.subheader("📊 Évaluation des modèles")
    results = []

    for name, model in models.items():
        try:
            model.fit(X_train, y_train)
            y_pred = model.predict(X_test)

            acc = accuracy_score(y_test, y_pred)
            cm = confusion_matrix(y_test, y_pred)

            results.append({"Modèle": name, "Accuracy": acc})

            st.markdown(f"#### 🔍 {name}")
            fig, ax = plt.subplots()
            sns.heatmap(cm, annot=True, fmt='d', cmap='Blues', ax=ax, xticklabels=class_names, yticklabels=class_names)
            ax.set_xlabel("Prédit")
            ax.set_ylabel("Réel")
            ax.set_title(f"Matrice de confusion - {name}")
            st.pyplot(fig)

            # 📊 Génération du rapport de classification détaillé
            classification_rep = classification_report(y_test, y_pred, target_names=class_names, output_dict=True)
            df_classification = pd.DataFrame(classification_rep).T

            st.subheader(f"📊 Rapport de classification - {name}")
            st.dataframe(df_classification.style.highlight_max(axis=0))

            # 📥 Export du rapport en fichier Excel
            classification_excel_path = f"classification_details_{name}.xlsx"
            df_classification.to_excel(classification_excel_path)

            st.download_button(label=f"📥 Télécharger le rapport détaillé de {name} (Excel)",
                               data=open(classification_excel_path, "rb").read(),
                               file_name=classification_excel_path,
                               mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet")

        except Exception as e:
            st.error(f"❌ Erreur sur {name}: {str(e)}")

    # 📈 **Comparaison des performances**
    df_results = pd.DataFrame(results).set_index("Modèle")
    st.subheader("📈 Comparaison des modèles")
    st.dataframe(df_results.style.highlight_max(axis=0))

    # 📥 **Export des résultats en fichier Excel**
    excel_path = "classification_results.xlsx"
    df_results.to_excel(excel_path)

    st.success("✅ Résultats exportés en fichier Excel !")
    st.download_button(label="📥 Télécharger les résultats comparatifs (Excel)", data=open(excel_path, "rb").read(),
                       file_name=excel_path, mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet")