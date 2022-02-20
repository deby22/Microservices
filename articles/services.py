from flask import jsonify

from init import db
from models import Article
from schemas import article_schema, articles_schema


class ArticleService:
    def create(self, data):
        article = Article(**data)
        db.session.add(article)
        db.session.commit()
        return article_schema.jsonify(article)

    def get_list(self):
        articles = Article.query.all()
        return jsonify(articles_schema.dump(articles))

    def get(self, id):
        article = Article.query.get_or_404(id)
        return article_schema.jsonify(article)
