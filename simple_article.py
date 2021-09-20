class SimpleArticle:
    def __init__(self, article_id, title):
        self.article_id = article_id
        self.title = title
        self.original_language = None
        self.thumbnail = None
        self.category = None
        self.tags = None
        self.author = None
        self.pub_date = None
        self.mod_date = None
        self.sections = None

    def set_article_details(self, article_details):
        self.original_language = article_details['original_language']
        self.thumbnail = article_details['thumbnail']
        self.category = article_details['category']
        self.tags = article_details['tags']
        self.author = article_details['author']
        self.pub_date = article_details['pub_date']
        self.mod_date = article_details['mod_date']
        self.sections = article_details['sections']
