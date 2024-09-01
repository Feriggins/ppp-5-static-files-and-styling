from flask import Blueprint, render_template, request, redirect, url_for
import json

bp_facts = Blueprint('facts', __name__, url_prefix="/facts")

@bp_facts.route('/')
def index(): 
    return render_template('facts.html')

@bp_facts.route("/new")
def new_fact():
    # Load pets from the JSON file
    with open('pets.json') as f:
        pets = json.load(f)
    # Render the form template with pets data
    return render_template('new_facts.html', pets=pets)

@bp_facts.route("/add", methods=['POST'])
def add_fact():
    # Extract pet ID and new fact from form data
    pet_id = request.form.get('pet_id')
    pet_fact = request.form.get('pet_fact')

    # Load pets from the JSON file
    with open('pets.json', 'r') as f:
        pets = json.load(f)

    # Find the pet and add the new fact
    for pet in pets:
        if pet['pet_id'] == int(pet_id):
            pet['pet_fact'] = pet_fact  # Update or add the new fact
            break

    # Save updated pets data back to JSON file
    with open('pets.json', 'w') as f:
        json.dump(pets, f, indent=4)

    # Redirect to the index page or back to the form with a success message
    return redirect(url_for('facts.index'))
