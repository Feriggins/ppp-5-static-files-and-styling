from flask import Flask, render_template

def create_app(): 
    app = Flask(__name__)

    @app.route('/')
    def index(): 
        return render_template("main.html")
    
    from . import pet
    from . import facts
    
    app.register_blueprint(pet.bp)
    app.register_blueprint(facts.bp_facts)
    
    return app