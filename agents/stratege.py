class Stratege:
    def __init__(self):
        self.name = "Stratège"
    
    def run(self, input_data):
        domain = input_data.get('domain', '')
        return f"Stratégie proposée pour le domaine {domain}:\n" + \
               f"1. Analyse du marché\n" + \
               f"2. Identification des opportunités\n" + \
               f"3. Plan d'action recommandé\n" + \
               f"4. Objectifs à court et long terme" 