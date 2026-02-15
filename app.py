from flask import Flask
from your_blueprint_module import your_blueprint

def create_app():
    app = Flask(__name__)

    # Register blueprints
    app.register_blueprint(your_blueprint)

    return app

if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)