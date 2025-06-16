from typing import Dict, Any, List
from langchain_community.llms import OpenAI
from langchain.prompts import PromptTemplate
import os
from dotenv import load_dotenv

load_dotenv()

class RealCoverageAgent:
    """
    Agent qui analyse la couverture d'assurance actuelle.
    """
    
    def __init__(self):
        self.llm = OpenAI(openai_api_key=os.getenv('OPENAI_API_KEY'))
        self.prompt_template = PromptTemplate(
            input_variables=["content"],
            template="""
            Liste les assurances mentionnées dans ce texte :
            {content}
            
            Format de réponse (JSON) :
            {{
                "assurances": [
                    {{
                        "type": str,
                        "montant": str
                    }}
                ]
            }}
            """
        )
    
    def run(self, content: str) -> List[Dict[str, Any]]:
        """
        Analyse le texte et extrait les assurances.
        """
        try:
            prompt = self.prompt_template.format(content=content)
            response = self.llm.invoke(prompt)
            result = eval(response)  # Simple parsing pour la beta
            return result.get("assurances", [])
            
        except Exception as e:
            print(f"Erreur RealCoverageAgent: {str(e)}")
            return [] 