from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from redis import Redis

# Init app
app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:////tmp/notification.db"

# Init db
db = SQLAlchemy(app)

# Init marshmallow
ma = Marshmallow(app)

# Init redis
redis = Redis(host="redis", port=6379)
