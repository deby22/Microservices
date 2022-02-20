from services import ReporterService, AuthorService
from init import db, app

db.drop_all()
db.create_all()


with app.app_context():
    author_service = AuthorService()
    author_service.create({"email": "dawid.deby@gmail.com"})
    author_service.create({"email": "ddeby@firstam.com"})

    reporter_service = ReporterService()
    reporter_service.create({"email": "dawid.deby@gmail.com"})
    reporter_service.create({"email": "ddeby@firstam.com"})
