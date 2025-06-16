from .redacteur import Redacteur
from .designer import Designer

class Coordinateur:
    def __init__(self):
        self.name = "Coordinateur"
        self.redacteur = Redacteur()
        self.designer = Designer()
    
    def run(self, input_data):
        domain = input_data.get('domain', '')
        
        # Obtenir les résultats des agents
        contenu = self.redacteur.run(input_data)
        design = self.designer.run(input_data)
        
        return f"Proposition coordonnée pour le domaine {domain}:\n\n" + \
               f"=== CONTENU ===\n{contenu}\n\n" + \
               f"=== DESIGN ===\n{design}\n\n" + \
               f"=== RECOMMANDATIONS DE COLLABORATION ===\n" + \
               f"1. Intégration du contenu dans le design\n" + \
               f"2. Harmonisation des messages clés\n" + \
               f"3. Optimisation de l'expérience utilisateur" 