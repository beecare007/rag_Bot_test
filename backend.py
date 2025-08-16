import ollama
from typing import Optional
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class OllamaHelper:
    def __init__(self):
        self.client = ollama.Client(host='http://localhost:11434')
        self.models = self._check_models()
    
    def _check_models(self):
        try:
            return [m['name'] for m in self.client.list()['models']]
        except Exception as e:
            logger.error(f"Ollama connection failed: {e}")
            return []
    
    def get_answer(self, question: str) -> Optional[str]:
        if not self.models:
            return "System error: No Ollama models available"
        
        try:
            response = self.client.generate(
                model='mistral',
                prompt=question,
                stream=False
            )
            return response['response']
        except Exception as e:
            logger.error(f"Generation failed: {e}")
            return f"Error: {str(e)}"

# Singleton instance
helper = OllamaHelper()

def get_answer(question):
    return helper.get_answer(question)
