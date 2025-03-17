from abc import ABC, abstractmethod
import os
import google.generativeai as genai

class ArticleAnalysisStrategy(ABC):
  @abstractmethod
  def analyze(self, article):
    pass

class KeywordAnalysisStrategy(ArticleAnalysisStrategy):
  def analyze(self, article):
    print(f"Analisando palavras-chave: { article.keywords}")
    return {
      "strategy": "keyword_analysis",
      "keyword": article.keywords,
      "analysis": f"Análise baseada nas palavras-chave: { article.keywords }"
    }

class PromptVerificationStrategy(ArticleAnalysisStrategy):
  def __init__(self, prompt):
    self.prompt = prompt

  def analyze(self, article):
    matches = any(term.lower() in article.abstract.lower() for term in self.prompt.split())
    reason = "O resumo contém termos do prompt" if  matches else "O resumo não contém termos do prompt"

    return {
      "strategy": "prompt_verification",
      "matches_prompt": matches,
      "reason": reason,
    }

class CitationExtractionStrategy(ArticleAnalysisStrategy):
  def  __init__(self, api_key=None):
    self.api_key = api_key or os.environ.get("GEMINI_API_KEY")
    genai.configure(api_key = self.api_key)

  def analyze(self, article):
    model = genai.GenerativeModel("gemini-2.0-flash")

    prompt = f"""
    Extraia as 3 citações mais importantes do texto:

    Título: { article.title }
    Resumo: { article.abstract }
    Texto:  { article.text[:1000]}...

    Retorne apenas as citações em formato ACM, sem comentarios adicionais.
    """

    response = model.generate_content(prompt)

    return {
      "strategy": "citation_extraction",
      "citation": response.text,
    }
