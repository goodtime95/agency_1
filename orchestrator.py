from typing import Dict, Any
from agents.profile_agent import ProfileAgent
from agents.real_coverage_agent import RealCoverageAgent
from agents.coverage_advisor_agent import CoverageAdvisorAgent

class InsuranceAnalysisOrchestrator:
    """
    Orchestrateur simple pour l'analyse d'assurance.
    """
    
    def __init__(self):
        self.profile_agent = ProfileAgent()
        self.real_coverage_agent = RealCoverageAgent()
        self.coverage_advisor_agent = CoverageAdvisorAgent()
    
    def analyze(self, user_text: str, coverage_text: str) -> Dict[str, Any]:
        """
        Analyse simple du profil et des assurances.
        """
        try:
            # 1. Analyse du profil
            profile = self.profile_agent.run(user_text)
            
            # 2. Analyse des assurances actuelles
            real_coverage = self.real_coverage_agent.run(coverage_text)
            
            # 3. Génération des recommandations
            recommendations = self.coverage_advisor_agent.run(profile, real_coverage)
            
            return {
                "profile": profile,
                "real_coverage": real_coverage,
                "recommendations": recommendations
            }
            
        except Exception as e:
            print(f"Erreur Orchestrator: {str(e)}")
            return {
                "profile": {},
                "real_coverage": [],
                "recommendations": {"recommandations": [], "score": 0}
            }

if __name__ == "__main__":
    # Exemple d'utilisation
    orchestrator = InsuranceAnalysisOrchestrator()
    
    # Profil utilisateur
    user_text = """
    Je suis un développeur de 35 ans, marié avec 2 enfants.
    Je gagne 80k€ par an et possède une maison de 300k€.
    J'habite en région parisienne et pratique le vélo en ville.
    """
    
    # Couverture actuelle
    coverage_text = """
    J'ai une assurance habitation avec une garantie de 200k€.
    J'ai aussi une assurance vie de 100k€ et une prévoyance invalidité.
    Ma voiture est assurée tous risques.
    """
    
    # Lancement de l'analyse
    result = orchestrator.analyze(user_text, coverage_text)
    
    # Affichage des résultats
    import json
    print(json.dumps(result, indent=2, ensure_ascii=False)) 