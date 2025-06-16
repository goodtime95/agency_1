from typing import Dict, Any, List
from langchain_community.llms import OpenAI
from langchain.prompts import PromptTemplate
import os
from dotenv import load_dotenv

load_dotenv()

class CoverageAdvisorAgent:
    """
    Agent qui fournit des recommandations d'assurance.
    """
    
    def __init__(self):
        self.llm = OpenAI(openai_api_key=os.getenv('OPENAI_API_KEY'))
        self.prompt_template = PromptTemplate(
            input_variables=["profile", "real_coverage"],
            template="""
            Donne des recommandations d'assurance basées sur :
            
            Profil :
            {profile}
            
            Assurances actuelles :
            {real_coverage}
            
            Format de réponse (JSON) :
            {{
                "recommandations": [
                    {{
                        "type": str,
                        "description": str
                    }}
                ],
                "score": int  # 0-100
            }}
            """
        )
    
    def run(
        self,
        profile: Dict[str, Any],
        real_coverage: List[Dict[str, Any]]
    ) -> Dict[str, Any]:
        """
        Génère des recommandations d'assurance.
        """
        try:
            prompt = self.prompt_template.format(
                profile=str(profile),
                real_coverage=str(real_coverage)
            )
            response = self.llm.invoke(prompt)
            return eval(response)  # Simple parsing pour la beta
            
        except Exception as e:
            print(f"Erreur CoverageAdvisorAgent: {str(e)}")
            return {"recommandations": [], "score": 0} 