class Article:
  def __init__(self, id, title, authors, abstract, keywords, text):
    self.id       = id
    self.title    = title
    self.authors  = authors
    self.abstract = abstract  
    self.keywords = keywords
    self.text     = text

  def __str__(self):
    return f"Article(id = { self.id }, title = '{ self.title }')"