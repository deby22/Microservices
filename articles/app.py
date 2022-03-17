import os

from flask import request, abort

from services import ArticleService
from init import app, redis, db


def sla_simulator():
    redis.incr("article_hits")
    if int(redis.get("article_hits") or "1") % 10 == 0:
        abort(500)


@app.route("/")
def hello():
    sla_simulator()
    return f"ARTICLES has been viewed {redis.get('article_hits')} times"


@app.route("/articles", methods=["POST"])
def create_article():
    sla_simulator()
    service = ArticleService()
    return service.create(request.get_json(force=True))


@app.route("/articles", methods=["GET"])
def get_articles():
    sla_simulator()
    service = ArticleService()
    return service.get_list()


@app.route("/articles/<int:id>", methods=["GET"])
def get_article(id):
    sla_simulator()
    service = ArticleService()
    return service.get(id)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=os.getenv("PORT"))
