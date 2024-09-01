from flask import Blueprint, render_template
import json

bp = Blueprint('pet', __name__, url_prefix="/pets")

@bp.route("/")
def index():
    with open('pets.json') as f:
        pets = json.load(f)
    return render_template("index.html", pets=pets)

@bp.route('/<int:pet_id>')
def pet_details(pet_id):

    with open("pets.json") as f:
        pets = json.load(f)

    for pet in pets:
        if pet["pet_id"] == pet_id:
            return render_template('pet_facts.html', pet=pet)

    return "Can't find that pet", 404
