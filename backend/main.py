
from flask import Flask, render_template, redirect, url_for, request, jsonify
from flask_sqlalchemy import SQLAlchemy
import requests

app = Flask(__name__)
app.config["SECRET_KEY"] = "8BYkEfBA6O6donzWlSihBXox7C0sKR6b"
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///ingredients.db"

db = SQLAlchemy(app)

class Ingredient(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(32), unique=True, nullable=False)
    ingredient_name = db.Column(db.String(250), unique=False, nullable=False)
    expiration = db.Column(db.String(8),unique=False,nullable=False)
    img_url = db.Column(db.String(500))
    def __repr__(self) -> str:
        return f"<Ingredients: { self.title }"
    def to_dict(self):
        return {column.name: getattr(self, column.name) for column in self.__table__.columns}



@app.route("/")
def home():
    db.create_all()
    return "Nothing Here"


@app.route("/ingredient/add", methods=["POST"])
def add():
    if request.method == "POST":
        username = request.args.get("username")
        ingredient_name = request.args.get("ingredient_name")
        expiration = request.args.get("expiration_date")
        img_url = request.args.get("img_url")
        ingredient_entry = Ingredient(
            username=username,
            ingredient_name=ingredient_name,
            expiration=expiration,
            img_url=img_url
        )
        db.session.add(ingredient_entry)
        db.session.commit()
        return "success",200

@app.route("/ingredient/get", methods=["GET"])
def get():
    if request.method == "GET":
        username = request.args.get("username")
        # ingredients = db.session.execute(db.select(Ingredient).filter_by(username=username))
        ingredients = db.session.query(Ingredient).filter_by(username=username).all()
        if(ingredients==None):
            return 404
        ingredient_list = [row.to_dict() for row in ingredients]
        return jsonify(ingredient_list),200

@app.route("/ingredient/delete",methods=["DELETE"])
def delete():
    if request.method == "DELETE":
        ingredient_id = request.args.get("id")
        username = request.args.get("username")
        entry_to_delete = Ingredient.query.get(ingredient_id)
        if entry_to_delete.username==username:
            db.session.delete(entry_to_delete)
            return "deleted",200
    return "failed"
