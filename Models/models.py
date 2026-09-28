from importlib import import_module

try:
    SQLAlchemy = import_module("flask_sqlalchemy").SQLAlchemy
except ModuleNotFoundError as error:
    raise ModuleNotFoundError(
        "Install Flask-SQLAlchemy with: python -m pip install Flask-SQLAlchemy"
    ) from error

db = SQLAlchemy()

# class Buku(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     judul = db.Column(db.String(100))
#     penulis = db.Column(db.String(50))

class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    task = db.Column(db.String(200))