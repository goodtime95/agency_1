import streamlit as st
from orchestrator import InsuranceAnalysisOrchestrator

st.set_page_config(
    page_title="Analyseur d'Assurance",
    page_icon="🛡️",
    layout="wide"
)

st.title("Analyseur d'Assurance 🛡️")

# Initialisation
orchestrator = InsuranceAnalysisOrchestrator()

# Interface
with st.form("analysis_form"):
    # Profil
    user_text = st.text_area(
        "Décrivez votre profil",
        placeholder="Ex: Je suis un développeur de 35 ans, marié avec 2 enfants..."
    )
    
    # Assurances
    coverage_text = st.text_area(
        "Décrivez vos assurances actuelles",
        placeholder="Ex: J'ai une assurance habitation avec une garantie de 200k€..."
    )
    
    submitted = st.form_submit_button("Analyser")
    
    if submitted and user_text and coverage_text:
        with st.spinner("Analyse en cours..."):
            try:
                # Analyse
                result = orchestrator.analyze(user_text, coverage_text)
                
                # Affichage
                st.success("Analyse terminée !")
                
                # Profil
                st.subheader("Profil")
                st.json(result["profile"])
                
                # Assurances actuelles
                st.subheader("Assurances actuelles")
                st.json(result["real_coverage"])
                
                # Recommandations
                st.subheader("Recommandations")
                recommendations = result["recommendations"]
                
                # Score
                st.metric("Score de couverture", f"{recommendations['score']}/100")
                
                # Liste des recommandations
                for rec in recommendations["recommandations"]:
                    st.write(f"**{rec['type']}**")
                    st.write(rec["description"])
                    st.write("---")
                
            except Exception as e:
                st.error(f"Erreur : {str(e)}")
    elif submitted:
        st.warning("Veuillez remplir tous les champs.") 