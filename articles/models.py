from init import db


class Article(db.Model):
    author = db.Column(db.Integer, nullable=False)
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80), unique=True, nullable=False)
    content = db.Column(db.String, nullable=False)
