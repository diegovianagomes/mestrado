class ArticleProcessor:
    def __init__(self, strategy=None):
        self.strategy = strategy

    def set_strategy(self, strategy):
        self.strategy = strategy

    def process_article(self, article):
        if not self.strategy:
            raise ValueError("Nenhuma estratégia definida")

        return self.strategy.analyze(article)