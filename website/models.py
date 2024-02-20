from . import db 

class inventory(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    item_name = db.Column(db.String(200))
    variant = db.Column(db.String(200))
    stock = db.Column(db.Integer)
    price = db.Column(db.Integer)
    cost_price = db.Column(db.Integer)
    sku = db.Column(db.String(150), unique=True)

class sale(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    sale_date = db.Column(db.Date)
    cust_name = db.Column(db.String(200))
    payment_mode = db.Column(db.String(20))
    total_bill = db.Column(db.Integer)
    items = db.relationship('sale_details')

class sale_details(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    sale_id = db.Column(db.Integer, db.ForeignKey('sale.id'))
    item_id = db.Column(db.Integer, db.ForeignKey('inventory.id'))
    quantity = db.Column(db.Integer)

class expense(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    bill_date = db.Column(db.Date)
    item_name = db.Column(db.String(200))
    bill_amount = db.Column(db.Integer)
    due = db.Column(db.Integer)
    gst = db.Column(db.String(3))
    type = db.Column(db.String(200))


