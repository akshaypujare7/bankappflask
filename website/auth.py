
from flask import Blueprint, render_template, request, flash, redirect, url_for
from .models import User, AccountSummary
from .database import Customers
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import check_password_hash
from . import db
from flask_login import login_user, login_required, logout_user, current_user

auth = Blueprint('auth', __name__)

@auth.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        name = request.form.get('name')
        password = request.form.get('password')

        user = User.query.filter_by(name=name).first()
        if user:
            if check_password_hash(user.password, password):
                flash('Logged in successfully!', category='success')
                login_user(user, remember=True)
                return redirect(url_for('auth.customer_login'))
            else:
                flash('Incorrect password, try again.', category='error')
        else:
            flash('Name does not exist.', category='error')

    return render_template("login.html", user=current_user)


@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('auth.login'))


@auth.route('/customer_login', methods=['GET', 'POST'])
def customer_login():
    if request.method == 'POST':
        customer_id = request.form.get('cust_id')
        account_number = request.form.get('acc_no')
        customer = AccountSummary.query.filter_by(cust_id=customer_id).first()
        account = AccountSummary.query.filter_by(acc_no=account_number).first()
        if customer and account:
            login_user(customer, remember=True)
            return redirect(url_for('views.home'))
        else:
            flash('Invalid customer id or account number',category='error')
    return render_template("customer_login.html", user=current_user)
