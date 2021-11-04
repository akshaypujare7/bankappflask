from flask import Blueprint, render_template, request, flash
from flask_login import login_required, current_user
from .database import Base, Users, Customers
from . import db


views = Blueprint('views', __name__)


@views.route('/', methods=['GET', 'POST'])
@login_required
def home():
    if request.method == 'POST':
        acc_no = request.form.get('acc_no')
        cust_id = request.form.get('cust_id')
        data = db.execute("Select * from users inner join customers on users.:acc_no = customers.:acc_no where cust_id = :cust_id",
                          {"acc_no":acc_no,"cust_id":cust_id}).fetchall()
        if data:
            return render_template('home.html', viewaccount=True, data=data)
        flash("Account not found! Please,Check you input.", 'danger')
    return render_template('home.html', viewaccount=True)



