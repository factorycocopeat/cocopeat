from flask import Blueprint, render_template, request

bp = Blueprint("products", __name__, url_prefix="/products")

@bp.route("/cocopeat/coco-peat-5kg-blocks/")
def infrastructure():
    return render_template(
        "product/coco-peat-5kg-blocks.html"
    )