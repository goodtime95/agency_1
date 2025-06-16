from typing import Dict, Any
from langchain_community.llms import OpenAI
from langchain.prompts import PromptTemplate
import os
from dotenv import load_dotenv

load_dotenv()

class ProfileAgent:
    """
    Agent qui extrait les informations de profil d'un utilisateur.
    """
    
    def __init__(self):
        self.llm = OpenAI(openai_api_key=os.getenv('OPENAI_API_KEY'))
        self.prompt_template = PromptTemplate(
            input_variables=["user_text"],
            template="""
            Extrait les informations de profil de ce texte :
            {user_text}
            
            Format de réponse (JSON) :
            {{
                "age": int,
                "profession": str,
                "revenus": str,
                "situation_familiale": str
            }}
            """
        )
    
    def run(self, user_text: str) -> Dict[str, Any]:
        """
        Analyse le texte et extrait le profil.
        """
        try:
            prompt = self.prompt_template.format(user_text=user_text)
            response = self.llm.invoke(prompt)
            return eval(response)  # Simple parsing pour la beta
            
        except Exception as e:
            print(f"Erreur ProfileAgent: {str(e)}")
            return {} 