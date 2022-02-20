from flask import jsonify

from init import db
from models import Author, Reporter
from schemas import person_schema, persons_schema


class AuthorService:
    def create(self, data):
        author = Author(data)
        db.session.add(author)
        db.session.commit()
        return person_schema.jsonify(author)

    def get_list(self):
        articles = Author.query.all()
        return jsonify(persons_schema.dump(articles))

    def get(self, id):
        authors = Author.query.get_or_404(id)
        return person_schema.jsonify(authors)


class ReporterService:
    def create(self, data):
        reporter = Reporter(data)
        db.session.add(reporter)
        db.session.commit()
        return person_schema.jsonify(reporter)

    def get_list(self):
        reporters = Reporter.query.all()
        return jsonify(persons_schema.dump(reporters))

    def get(self, id):
        reporter = Reporter.query.get_or_404(id)
        return person_schema.jsonify(reporter)
