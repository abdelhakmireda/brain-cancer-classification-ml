import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import kagglehub
import io

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.decomposition import PCA
from sklearn.metrics import classification_report, confusion_matrix, accuracy_score
from sklearn.linear_model import LogisticRegression
from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.svm import SVC
from sklearn.impute import SimpleImputer

st.set_page_config(page_title="Classification Cancer du Cerveau", layout="wide")
st.title("🧠 Classification des données du cancer du cerveau")
st.markdown("Prédiction du diagnostic avec différents modèles de Machine Learning")

# 🎯 Sidebar : Génération de dataset simulé
st.sidebar.header("🎲 Générer un dataset simulé")

num_samples = st.sidebar.number_input("Nombre d'échantillons", min_value=10, max_value=5000, value=100)
num_features = st.sidebar.number_input("Nombre de caractéristiques", min_value=5, max_value=500, value=50)
generate_data = st.sidebar.button("🔄 Générer le dataset")

if generate_data:
    np.random.seed(42)
    data = np.random.rand(num_samples, num_features)
    columns = [f"Feature_{i}" for i in range(1, num_features + 1)]
    df_generated = pd.DataFrame(data, columns=columns)
    df_generated["Target"] = np.random.choice([0, 1], size=num_samples)

    generated_csv_path = "dataset_simulé.csv"
    df_generated.to_csv(generated_csv_path, index=False)

    st.sidebar.success("✅ Dataset simulé généré avec succès !")
    st.sidebar.download_button(
        label="📥 Télécharger le dataset CSV",
        data=open(generated_csv_path, "rb").read(),
        file_name=generated_csv_path,
        mime="text/csv"
    )

# 🧬 Sidebar : Importer le dataset Kaggle
st.sidebar.header("🧬 Kaggle BrainCancer Dataset")
import_kaggle_data = st.sidebar.button("📥 Télécharger et importer les données Kaggle")

if import_kaggle_data:
    try:
        path = kagglehub.dataset_download("brunogrisci/brain-cancer-gene-expression-cumida")
        kaggle_csv_path = f"{path}/Brain_GSE50161.csv"
        df_kaggle = pd.read_csv(kaggle_csv_path)

        st.sidebar.success("✅ Données Kaggle importées avec succès !")
        st.write("Aperçu du dataset Kaggle :")
        st.dataframe(df_kaggle.head())

        df_kaggle.dropna(how='all', axis=1, inplace=True)
        for col in df_kaggle.columns:
            df_kaggle[col] = pd.to_numeric(df_kaggle[col], errors='coerce')

        imputer = SimpleImputer(strategy="mean")
        X_kaggle = imputer.fit_transform(df_kaggle.iloc[:, :-1])
        y_kaggle = df_kaggle.iloc[:, -1]

        # 🧠 Encodage du label pour éviter l'erreur "Unknown label type"
        if y_kaggle.dtype == float or y_kaggle.dtype == int:
            y_kaggle = pd.qcut(y_kaggle, q=2, labels=[0, 1])  # Discrétisation binaire
        else:
            le = LabelEncoder()
            y_kaggle = le.fit_transform(y_kaggle)

        scaler = StandardScaler()
        X_kaggle_scaled = scaler.fit_transform(X_kaggle)

        pca = PCA(n_components=min(50, X_kaggle_scaled.shape[1]))
        X_kaggle_pca = pca.fit_transform(X_kaggle_scaled)

        X_train_kaggle, X_test_kaggle, y_train_kaggle, y_test_kaggle = train_test_split(
            X_kaggle_pca, y_kaggle, test_size=0.2, random_state=42
        )

        models = {
            "Régression Logistique": LogisticRegression(max_iter=1000),
            "KNN": KNeighborsClassifier(),
            "Arbre de Décision": DecisionTreeClassifier(),
            "Naïve Bayes": GaussianNB(),
            "SVM": SVC()
        }

        results_kaggle = []

        for name, model in models.items():
            try:
                model.fit(X_train_kaggle, y_train_kaggle)
                y_pred_kaggle = model.predict(X_test_kaggle)

                acc = accuracy_score(y_test_kaggle, y_pred_kaggle)
                cm = confusion_matrix(y_test_kaggle, y_pred_kaggle)

                results_kaggle.append({"Modèle": name, "Accuracy": acc})

                st.markdown(f"#### 🔍 {name} (Kaggle)")
                fig, ax = plt.subplots()
                sns.heatmap(cm, annot=True, fmt='d', cmap='Greens', ax=ax)
                ax.set_xlabel("Prédit")
                ax.set_ylabel("Réel")
                ax.set_title(f"Matrice de confusion - {name} (Kaggle)")
                st.pyplot(fig)

            except Exception as e:
                st.error(f"❌ Erreur sur {name} avec les données Kaggle : {str(e)}")

        df_results_kaggle = pd.DataFrame(results_kaggle).set_index("Modèle")
        st.subheader("📈 Résultats sur les données Kaggle")
        st.dataframe(df_results_kaggle.style.highlight_max(axis=0))

        xlsx_kaggle_path = "kaggle_classification_results.xlsx"
        output = io.BytesIO()
        with pd.ExcelWriter(output, engine='xlsxwriter') as writer:
            df_results_kaggle.to_excel(writer, sheet_name="Résultats_Kaggle")
        st.download_button(
            label="📥 Télécharger les résultats Kaggle (.xlsx)",
            data=output.getvalue(),
            file_name=xlsx_kaggle_path,
            mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
        )

    except Exception as e:
        st.error(f"❌ Erreur lors de l'importation du dataset Kaggle : {str(e)}")
        st.stop()

# 📂 Téléversement de fichier CSV ou Excel
st.subheader("📂 Téléversement des données")
uploaded_file = st.file_uploader("📤 Importez votre fichier CSV ou Excel", type=["csv", "xlsx"])

if uploaded_file is not None:
    try:
        if uploaded_file.name.endswith('.csv'):
            df = pd.read_csv(uploaded_file)
        elif uploaded_file.name.endswith('.xlsx'):
            df = pd.read_excel(uploaded_file)
        else:
            st.error("❌ Format de fichier non supporté.")
            st.stop()
    except Exception as e:
        st.error(f"❌ Erreur lors du chargement du fichier : {str(e)}")
        st.stop()
else:
    st.warning("⚠️ Veuillez téléverser un fichier CSV ou Excel pour continuer.")
    st.stop()

st.success("✅ Données chargées avec succès !")
st.write("Aperçu du dataset :")
st.dataframe(df.head())

# Prétraitement
df.dropna(how='all', axis=1, inplace=True)
for col in df.columns:
    df[col] = pd.to_numeric(df[col], errors='coerce')

imputer = SimpleImputer(strategy="mean")
X = imputer.fit_transform(df.iloc[:, :-1])
y = df.iloc[:, -1]

# Encodage du label si besoin
if y.dtype == float or y.dtype == int:
    y_cut, bins = pd.qcut(y, q=2, retbins=True, duplicates='drop')
    n_intervals = len(bins) - 1
    labels = list(range(n_intervals))
    y = pd.qcut(y, q=2, labels=labels, duplicates='drop')
else:
    y = LabelEncoder().fit_transform(y)


scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

pca = PCA(n_components=min(50, X_scaled.shape[1]))
X_pca = pca.fit_transform(X_scaled)

X_train, X_test, y_train, y_test = train_test_split(
    X_pca, y, test_size=0.2, random_state=42, stratify=y
)


models = {
    "Régression Logistique": LogisticRegression(max_iter=1000),
    "KNN": KNeighborsClassifier(),
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
        sns.heatmap(cm, annot=True, fmt='d', cmap='Blues', ax=ax)
        ax.set_xlabel("Prédit")
        ax.set_ylabel("Réel")
        ax.set_title(f"Matrice de confusion - {name}")
        st.pyplot(fig)

    except Exception as e:
        st.error(f"❌ Erreur sur {name}: {str(e)}")

df_results = pd.DataFrame(results).set_index("Modèle")
st.subheader("📈 Comparaison des modèles")
st.dataframe(df_results.style.highlight_max(axis=0))

csv_path = "classification_results.csv"
try:
    df_results.to_csv(csv_path)
    st.success(f"✅ Résultats exportés vers {csv_path}")
    st.download_button(
        label="📥 Télécharger les résultats CSV",
        data=open(csv_path, "rb").read(),
        file_name=csv_path,
        mime="text/csv"
    )
except Exception as e:
    st.error(f"❌ Erreur lors de l'exportation : {str(e)}")
