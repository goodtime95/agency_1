class Redacteur:
    def __init__(self):
        self.name = "Rédacteur"
    
    def run(self, input_data):
        domain = input_data.get('domain', '')
        return f"Contenu proposé pour le domaine {domain}:\n" + \
               f"1. Titre accrocheur\n" + \
               f"2. Introduction captivante\n" + \
               f"3. Points clés développés\n" + \
               f"4. Conclusion engageante" 