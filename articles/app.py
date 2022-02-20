import os

from flask import request

from services import ArticleService
from init import app, redis, db


@app.route("/")
def hello():
    redis.incr("article_hits")
    return f"ARTICLES has been viewed {redis.get('article_hits')} times"


@app.route("/articles", methods=["POST"])
def create_article():
    service = ArticleService()
    return service.create(request.json)


@app.route("/articles", methods=["GET"])
def get_articles():
    service = ArticleService()
    return service.get_list()


@app.route("/articles/<int:id>", methods=["GET"])
def get_article(id):
    service = ArticleService()
    return service.get(id)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=os.getenv("PORT"))
