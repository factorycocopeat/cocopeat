from flask import Blueprint, render_template, request

bp = Blueprint("infrastructure", __name__)

@bp.route("/infrastructure")
def infrastructure():
    return render_template(
        "production/infrastructure.html"
    )