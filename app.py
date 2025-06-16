from dotenv import load_dotenv
import os
import streamlit as st
from agents import Stratege

# Chargement des variables d'environnement
load_dotenv()

# Configuration de la page
st.set_page_config(
    page_title="Agence d'Agents IA",
    page_icon="🤖",
    layout="wide"
)

# Titre de l'application
st.title("🤖 Agence d'Agents IA")
st.markdown("---")

# Vérification de la clé API
if not os.getenv("OPENAI_API_KEY"):
    st.error("⚠️ La clé API OpenAI n'est pas configurée. Veuillez créer un fichier .env avec votre clé API.")
    st.stop()

# Initialisation des agents
stratege = Stratege()

# Sélection du domaine
domain = st.text_input("Entrez le domaine de travail (ex: coaching, marketing, etc.)", "coaching")

# Exécution de l'agent Stratège
if st.button("Lancer le Stratège"):
    with st.spinner("Le Stratège analyse le domaine..."):
        result = stratege.run(domain)
        st.markdown("### 🎯 Stratégie proposée")
        st.write(result)

# Ajout d'informations sur l'application
st.markdown("---")
st.markdown("""
### À propos
Cette application utilise des agents IA spécialisés pour analyser et proposer des stratégies.
Le Stratège utilise GPT-4 et des recherches web pour proposer des stratégies pertinentes.
""")
