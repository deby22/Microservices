import os

from flask import request

from services import AuthorService, ReporterService, NotificationService
from init import app, redis, db


# ----- CRUD -----
@app.route("/")
def hello():
    redis.incr("notification_hits")
    return f"NOTIFICATION has been viewed {redis.get('notification_hits')} times"


@app.route("/authors", methods=["POST"])
def create_author():
    service = AuthorService()
    return service.create(request.json)


@app.route("/authors", methods=["GET"])
def get_author():
    service = AuthorService()
    return service.get_list()


@app.route("/authors/<int:id>", methods=["GET"])
def get_authors(id):
    service = AuthorService()
    return service.get(id)


@app.route("/reporters", methods=["POST"])
def create_reporter():
    service = ReporterService()
    return service.create(request.json)


@app.route("/reporters", methods=["GET"])
def get_reporters():
    service = ReporterService()
    return service.get_list()


@app.route("/reporters/<int:id>", methods=["GET"])
def get_reporter(id):
    service = ReporterService()
    return service.get(id)


# ----- CRUD -----


# ----- Action -----
@app.route("/eloqua_register", methods=["POST"])
def eloqua_register():
    service = NotificationService()
    return service.eloqua_register(request.json)


@app.route("/sm_register", methods=["POST"])
def sm_register():
    service = NotificationService()
    return service.sm_register(request.json)


@app.route("/notify_reporters", methods=["GET"])
def notify_reporters():
    service = NotificationService()
    return service.notify_reporters()


# ----- Action -----


if __name__ == "__main__":
    db.create_all()
    app.run(host="0.0.0.0", port=os.getenv("PORT"))
