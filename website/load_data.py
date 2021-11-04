
from database import Base, Users, Customers
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from werkzeug.security import generate_password_hash
from flask import Flask

app = Flask(__name__)
engine = create_engine('sqlite:///database.db', connect_args={'check_same_thread': False}, echo=True)
Base.metadata.bind = engine
db = scoped_session(sessionmaker(bind=engine))


def accounts():
    id = 1
    acc_no = '1234'
    name = 'akshay'
    acc_type = 'savings'
    balance = '5000$'
    passw = 'Akshay@1'
    cust_id = '0001'
    passw_hash = generate_password_hash(passw,method='sha256')
    db.execute("INSERT INTO customers (cust_id,acc_no) VALUES (:c,:a)",{"c":cust_id,"a":acc_no})
    db.execute("INSERT INTO users (acc_no,name,acc_type,balance,password) VALUES (:a,:n,:t,:b,:p)",
               {"a": acc_no, "n": name, "t": acc_type, "b": balance, "p": passw_hash})
    db.commit()
    print("accounts Completed ............................................ ")
    id = 2
    acc_no = '1235'
    name = 'monil'
    acc_type = 'checking'
    balance = '8000$'
    passw = 'Monil@2'
    cust_id = '0002'
    passw_hash = generate_password_hash(passw,method='sha256')
    db.execute("INSERT INTO customers (cust_id,acc_no) VALUES (:c,:a)", {"c": cust_id, "a": acc_no})
    db.execute("INSERT INTO users (acc_no,name,acc_type,balance,password) VALUES (:a,:n,:t,:b,:p)",
               {"a": acc_no, "n": name, "t": acc_type, "b": balance, "p": passw_hash})
    db.commit()
    print("accounts Completed ............................................ ")
    id = 3
    acc_no = '1236'
    name = 'abhishek'
    acc_type = 'savings'
    balance = '6000$'
    passw = 'Abhishek@3'
    cust_id = '0003'
    passw_hash = generate_password_hash(passw,method='sha256')
    db.execute("INSERT INTO customers (cust_id,acc_no) VALUES (:c,:a)", {"c": cust_id, "a": acc_no})
    db.execute("INSERT INTO users (acc_no,name,acc_type,balance,password) VALUES (:a,:n,:t,:b,:p)",
               {"a": acc_no, "n": name, "t": acc_type, "b": balance, "p": passw_hash})
    db.commit()
    print("accounts Completed ............................................ ")


if __name__ == "__main__":
    accounts()