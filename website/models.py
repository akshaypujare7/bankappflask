from . import db
from flask_login import UserMixin


class AccountSummary(db.Model, UserMixin):
    __tablename__ = 'customers'
    id = db.Column(db.Integer)
    cust_id = db.Column(db.String, primary_key=True)
    acc_no = db.Column(db.String(250), db.ForeignKey('users.acc_no'))


class User(db.Model, UserMixin):
    __tablename__ = 'users'
    id = db.Column(db.Integer)
    acc_no = db.Column(db.String(250), primary_key=True)
    name = db.Column(db.String(250), nullable=False)
    acc_type = db.Column(db.String(250), nullable=False)
    password = db.Column(db.String(250))
    balance = db.Column(db.String)
    account = db.relationship('AccountSummary')