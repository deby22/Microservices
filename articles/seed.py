from services import ArticleService
from init import db, app

db.drop_all()
db.create_all()


with app.app_context():
    service = ArticleService()
    service.create(
        {"title": "First article", "content": "First articles content", "author": 1}
    )
    service.create(
        {"title": "Second article", "content": "Second article content", "author": 1}
    )
    service.create(
        {"title": "Third article", "content": "Third article content", "author": 2}
    )
