from flask import Blueprint, render_template

views = Blueprint('views', __name__)

metrics = {"sales_total":100, "inventory_total":200}

@views.route('/')
def home():
    return render_template("home.html", metrics=metrics)


@views.route('/sale')
def sale():
    return "<h1>Sale</h1>"

@views.route('/purchace')
def purchace():
    return "<h1>Purchace</h1>"

@views.route('/inventory')
def inventory():
    return "<h1>Inventory</h1>"

@views.route('/customer')
def customer():
    return "<h1>Customer</h1>"
