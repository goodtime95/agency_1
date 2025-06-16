import streamlit as st
from agents import Stratege, Redacteur, Designer, Developpeur, Coordinateur

# Configuration de la page
st.set_page_config(
    page_title="Agence d'Agents IA",
    page_icon="🤖",
    layout="wide"
)

# Titre de l'application
st.title("🤖 Agence d'Agents IA")
st.markdown("---")

# Initialisation des agents
agents = {
    "Stratège": Stratege(),
    "Rédacteur": Redacteur(),
    "Designer": Designer(),
    "Développeur": Developpeur(),
    "Coordinateur": Coordinateur()
}

# Sélection du domaine
domain = st.text_input("Entrez le domaine de travail (ex: coaching, marketing, etc.)", "coaching")

# Création des colonnes pour les boutons
col1, col2 = st.columns([3, 1])

with col1:
    # Boutons pour exécuter les agents individuellement
    st.subheader("Exécuter un agent")
    selected_agent = st.selectbox(
        "Choisissez un agent",
        list(agents.keys())
    )
    
    if st.button(f"Exécuter {selected_agent}"):
        result = agents[selected_agent].run({"domain": domain})
        st.text_area("Résultat", result, height=200)

with col2:
    # Bouton pour exécuter tous les agents
    st.subheader("Exécuter tous les agents")
    if st.button("Exécuter tous les agents"):
        for agent_name, agent in agents.items():
            st.markdown(f"### {agent_name}")
            result = agent.run({"domain": domain})
            st.text_area("Résultat", result, height=200)
            st.markdown("---")

# Ajout d'informations sur l'application
st.markdown("---")
st.markdown("""
### À propos
Cette application simule une agence avec 5 agents IA spécialisés :
- **Stratège** : Propose des stratégies globales
- **Rédacteur** : Crée du contenu adapté
- **Designer** : Suggère des designs
- **Développeur** : Propose des solutions techniques
- **Coordinateur** : Fait collaborer le Rédacteur et le Designer
""") 