from init import ma


class ArticleSchema(ma.Schema):
    class Meta:
        fields = ("id", "author", "title", "content")


article_schema = ArticleSchema()
articles_schema = ArticleSchema(many=True)
