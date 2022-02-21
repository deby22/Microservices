import time
import random

from flask import jsonify

from init import db
from models import Author, Reporter
from schemas import person_schema, persons_schema


class AuthorService:
    def create(self, data):
        author = Author(**data)
        db.session.add(author)
        db.session.commit()
        return person_schema.jsonify(author)

    def get_list(self):
        articles = Author.query.all()
        return jsonify(persons_schema.dump(articles))

    def get(self, id):
        author = Author.query.get_or_404(id)
        return person_schema.jsonify(author)


class ReporterService:
    def create(self, data):
        reporter = Reporter(**data)
        db.session.add(reporter)
        db.session.commit()
        return person_schema.jsonify(reporter)

    def get_list(self):
        reporters = Reporter.query.all()
        return jsonify(persons_schema.dump(reporters))

    def get(self, id):
        reporter = Reporter.query.get_or_404(id)
        return person_schema.jsonify(reporter)


class NotificationService:
    def eloqua_register(self, content):
        rand = round(random.uniform(0, 1), 2)
        time.sleep(rand)
        author_service = AuthorService()
        author = author_service.get(content["author"])
        content["author"] = author
        print(f"Eloqua register with data: {content}")
        return f"sm_register after: {rand} sec"

    def sm_register(self, content):
        rand = round(random.uniform(0, 1), 2)
        time.sleep(rand)
        author_service = AuthorService()
        author = author_service.get(content["author"])
        content["author"] = author
        print(f"Sales Manago register with data: {content}")
        return f"sm_register after {rand} sec"

    def notify_reporters(self):
        rand = round(random.uniform(0, 1), 2)
        time.sleep(rand)
        reporter_service = ReporterService()
        reporters = reporter_service.get_list()
        print(f"Send email to reporters: {reporters}")
        return f"notify_reporters after {rand} sec"
