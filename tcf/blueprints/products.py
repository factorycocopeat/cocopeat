from flask import Blueprint, render_template, request

bp = Blueprint("products", __name__, url_prefix="/products")

@bp.route("/cocopeat/coco-peat-5kg-blocks/")
def cocopeat5kgblocks():
    return render_template(
        "product/coco-peat-5kg-blocks.html"
    )
@bp.route("/cocopeat/cocopeat-growbags/")
def cocopeatgrowbags():
    return render_template(
        "product/cocopeat-growbags.html"
    )
@bp.route("/cocopeat/coco-chips/")
def cocochips():
    return render_template(
        "product/coco-chips.html"
    )