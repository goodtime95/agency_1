from langchain_community.chat_models import ChatOpenAI
from langchain.prompts import ChatPromptTemplate
from langchain_community.tools import DuckDuckGoSearchRun
import os

class Stratege:
    def __init__(self):
        self.name = "Stratège"
        self.llm = ChatOpenAI(
            model="gpt-4",
            temperature=0.7,
            api_key=os.getenv("OPENAI_API_KEY")
        )
        self.search = DuckDuckGoSearchRun()
        
        self.prompt = ChatPromptTemplate.from_messages([
            ("system", """Tu es un stratège expert en {domain}. 
            Analyse le domaine et propose une stratégie complète.
            Utilise les informations de recherche pour enrichir ta réponse.
            
            Format de réponse attendu :
            1. Analyse du marché
            2. Opportunités identifiées
            3. Plan d'action
            4. Objectifs et KPIs"""),
            ("human", "Domaine : {domain}\nInformations de recherche : {search_results}")
        ])
    
    def run(self, domain):
        # Recherche d'informations sur le domaine
        search_results = self.search.run(f"latest trends and strategies in {domain}")
        
        # Génération de la stratégie
        chain = self.prompt | self.llm
        response = chain.invoke({
            "domain": domain,
            "search_results": search_results
        })
        
        return response.content 