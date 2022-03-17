import os

from flask import request, abort

from services import AuthorService, ReporterService, NotificationService
from init import app, redis, db


def sla_simulator():
    redis.incr("notification_hits")
    if int(redis.get("notification_hits") or "1") % 10 == 0:
        abort(500)


# ----- CRUD -----
@app.route("/")
def hello():
    sla_simulator()
    return f"NOTIFICATION has been viewed {redis.get('notification_hits')} times"


@app.route("/authors", methods=["POST"])
def create_author():
    sla_simulator()
    service = AuthorService()
    return service.create(request.json)


@app.route("/authors", methods=["GET"])
def get_author():
    sla_simulator()
    service = AuthorService()
    return service.get_list()


@app.route("/authors/<int:id>", methods=["GET"])
def get_authors(id):
    sla_simulator()
    service = AuthorService()
    return service.get(id)


@app.route("/reporters", methods=["POST"])
def create_reporter():
    sla_simulator()
    service = ReporterService()
    return service.create(request.json)


@app.route("/reporters", methods=["GET"])
def get_reporters():
    sla_simulator()
    service = ReporterService()
    return service.get_list()


@app.route("/reporters/<int:id>", methods=["GET"])
def get_reporter(id):
    sla_simulator()
    service = ReporterService()
    return service.get(id)


# ----- CRUD -----


# ----- Action -----
@app.route("/eloqua_register", methods=["POST"])
def eloqua_register():
    sla_simulator()
    service = NotificationService()
    return service.eloqua_register(request.json)


@app.route("/sm_register", methods=["POST"])
def sm_register():
    sla_simulator()
    service = NotificationService()
    return service.sm_register(request.json)


@app.route("/notify_reporters", methods=["GET"])
def notify_reporters():
    sla_simulator()
    service = NotificationService()
    return service.notify_reporters()


# ----- Action -----


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=os.getenv("PORT"))
