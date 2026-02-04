from flask import Flask, render_template, request, redirect
from tcf.blueprints.main import bp as main_bp
from tcf.blueprints.products import bp as products_bp
def create_app():
    app = Flask(__name__, static_folder="tcf/static", template_folder="tcf/templates")
    # Register blueprints
    app.register_blueprint(main_bp)
    app.register_blueprint(products_bp)
    return app
app = create_app()