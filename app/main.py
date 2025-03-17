import os
import random
from dotenv import load_dotenv
import glob
import PyPDF2
from io import StringIO
from pdfminer.high_level import extract_text_to_fp
from pdfminer.layout import LAParams
from models.article import Article
from strategies.analysis_strategies import (
    KeywordAnalysisStrategy,
    PromptVerificationStrategy,
    CitationExtractionStrategy
)
from processors.article_processor import ArticleProcessor

load_dotenv()

def extract_text_from_pdf(file_path):
    """Extrai texto de um PDF usando pdfminer."""
    output = StringIO()
    with open(file_path, 'rb') as file:
        extract_text_to_fp(file, output, laparams=LAParams())
    return output.getvalue()

def extract_keywords_from_text(text, num_keywords=5):
    """Extrai palavras-chave de um texto."""
    from collections import Counter
    import re

    stop_words = {'the', 'a', 'an', 'and', 'or', 'but', 'is', 'are', 'was', 'were',
                 'in', 'on', 'at', 'to', 'for', 'with', 'by', 'about', 'of', 'this',
                 'that', 'these', 'those', 'from', 'as', 'be', 'been', 'being', 'have',
                 'has', 'had', 'do', 'does', 'did', 'will', 'would', 'shall', 'should',
                 'can', 'could', 'may', 'might', 'must', 'which', 'who', 'whom', 'whose',
                 'what', 'where', 'when', 'why', 'how'}

    words = re.findall(r'\b\w+\b', text.lower())
    words = [w for w in words if w not in stop_words and len(w) > 3]

    word_counts = Counter(words)
    return [word for word, _ in word_counts.most_common(num_keywords)]

def find_abstract(text):
    """Tenta encontrar o resumo em um texto acadêmico."""
    abstract_markers = ["abstract", "resumo", "summary"]

    paragraphs = text.split('\n\n')

    for i, para in enumerate(paragraphs):
        if any(marker in para.lower() for marker in abstract_markers):
            if i + 1 < len(paragraphs):
                return paragraphs[i + 1]
            else:
                return para

    if len(paragraphs) > 1:
        return paragraphs[1]  
    elif paragraphs:
        return paragraphs[0]
    else:
        return "Resumo não disponível"

def load_article_from_file(file_path):
    """Carrega um artigo de um arquivo."""
    file_id = os.path.basename(file_path).split('.')[0]
    file_ext = os.path.splitext(file_path)[1].lower()

    if file_ext == '.pdf':
        try:
            text = extract_text_from_pdf(file_path)

            with open(file_path, 'rb') as file:
                reader = PyPDF2.PdfReader(file)
                info = reader.metadata

                title = info.title if info and info.title else "Título não disponível"
                authors = [info.author] if info and info.author else ["Autor não disponível"]

                if title == "Título não disponível" and text:
                    lines = text.split('\n')
                    if lines:
                        title = lines[0].strip()

                abstract = find_abstract(text)

                keywords = extract_keywords_from_text(text)

                lower_text = text.lower()
                kw_indices = [lower_text.find(marker) for marker in ["keywords", "key words", "palavras-chave", "palavras chave"] if marker in lower_text]

                if kw_indices:
                    kw_index = min([idx for idx in kw_indices if idx >= 0])
                    kw_text = text[kw_index:].split('\n\n')[0]
                    kw_text = kw_text.replace(';', ',').lower()
                    for marker in ["keywords", "key words", "palavras-chave", "palavras chave"]:
                        kw_text = kw_text.replace(marker, '')
                    kw_text = kw_text.replace(':', '')
                    extracted_keywords = [k.strip() for k in kw_text.split(',') if k.strip()]
                    if extracted_keywords:
                        keywords = extracted_keywords

        except Exception as e:
            print(f"Erro ao processar PDF: {e}")
            title = file_id
            authors = ["Autor não disponível"]
            abstract = "Resumo não disponível"
            text = "Texto não disponível"
            keywords = ["PDF", "Artigo", file_id]

    elif file_ext in ['.txt', '.md']:
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read()

            lines = content.split('\n')
            title = lines[0] if lines else "Título não disponível"
            authors = [lines[1]] if len(lines) > 1 else ["Autor não disponível"]

            paragraphs = content.split('\n\n')
            abstract = paragraphs[1] if len(paragraphs) > 1 else "Resumo não disponível"

            text = content

            keywords = extract_keywords_from_text(content)

    else:
        raise ValueError(f"Formato de arquivo não suportado: {file_ext}")

    return Article(
        id=file_id,
        title=title,
        authors=authors,
        abstract=abstract,
        keywords=keywords,
        text=text
    )

def main():
    articles_folder = r"C:\DEV\mestrado\articles"

    article_files = glob.glob(os.path.join(articles_folder, "*.pdf"))
    article_files.extend(glob.glob(os.path.join(articles_folder, "*.txt")))

    if not article_files:
        print("Nenhum artigo encontrado na pasta. Usando artigo de exemplo.")
        article = Article(
            id="001",
            title="Implementação do Padrão Strategy em Python",
            authors=["João Silva", "Maria Oliveira"],
            abstract="Este artigo discute a implementação do padrão de design Strategy em Python para análise de artigos acadêmicos.",
            keywords=["Design Patterns", "Strategy", "Python", "Análise de Texto"],
            text="Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed do eiusmod tempor incididunt ut labore et dolore magna aliqua."
        )
    else:
        selected_file = random.choice(article_files)
        print(f"Processando arquivo: {selected_file}")

        try:
            article = load_article_from_file(selected_file)
            print(f"Título: {article.title}")
            print(f"Autores: {article.authors}")
            print(f"Palavras-chave: {article.keywords}")
            print(f"Tamanho do resumo: {len(article.abstract)} caracteres")
            print(f"Tamanho do texto: {len(article.text)} caracteres")
        except Exception as e:
            print(f"Erro ao carregar o artigo: {e}")
            return

    processor = ArticleProcessor()

    print("\n=== Análise de Palavras-chave ===")
    processor.set_strategy(KeywordAnalysisStrategy())
    result = processor.process_article(article)
    print(result)

    print("\n=== Verificação de Prompt ===")
    processor.set_strategy(PromptVerificationStrategy("Strategy Python"))
    result = processor.process_article(article)
    print(result)

    print("\n=== Extração de Citações ===")
    processor.set_strategy(CitationExtractionStrategy())
    result = processor.process_article(article)
    print(result)

if __name__ == "__main__":
    main()