from http import client
from flask import Flask, redirect, render_template, request, jsonify, url_for
import uuid
import pymongo
from flask_mail import Mail, Message
from random import randint
app = Flask(__name__)
app.config["MAIL_SERVER"] = 'smtp.gmail.com'
app.config["MAIL_PORT"] = 587
app.config["MAIL_USERNAME"] = 'tanisha0714@gmail.com'
# you have to give your password of gmail account
app.config['MAIL_PASSWORD'] = 'mayGodblessme'
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USE_SSL'] = False
mail = Mail(app)
otp = randint(000000, 999999)
# Database
client = pymongo.MongoClient(
    "mongodb+srv://a:a@cluster0.ilagt0y.mongodb.net/?retryWrites=true&w=majority")
db = client.get_database("users")
print(db.students.find_one({"email": "dipanshuhappy@gmail.com"}))
print(db.students)
# from user import routes


@app.route('/')
def home():
    return redirect(url_for('login'))


@app.route('/user/login', methods=['POST'])
def verify_login():
    message = ""
    user = {
        "email": request.form.get('email'),
        "password": request.form.get('password')
    }
    print("dljf;sd")
    if db.students.find_one({"email": user['email']}) != None:

        student = db.students.find_one({"email": user['email']})

        print("student", student['password'])
        print("student -user", user['password'])
        if(str(student['password']).strip() == user['password'].strip()):
            message = "valid"
            app.config['userid'] = student["_id"]
            return jsonify({"respond": message}), 200

        else:
            message = "invalid"
            return jsonify({"respond": message}), 400
    return jsonify({"respond": message}), 400


@app.route('/user/sendotp', methods=["POST"])
def sendOtp():
    message = "sent"
    email = request.form['email']
    msg = Message(subject='OTP', sender='tanisha0714@gmailcom',
                  recipients=[email])
    msg.body = str(otp)
    mail.send(msg)
    return jsonify({"respond": otp}), 200


@app.route('/user/validate', methods=['POST'])
def validate():
    message = ""
    user_otp = request.form['otp']
    if otp == int(user_otp):
        message = "valid"
        return jsonify({"respond": message}), 200
    message = "invalid"
    return jsonify({"respond": message}), 400


@app.route('/login')
def login():
    return render_template("login.html")


@app.route('/user/signup', methods=['POST'])
def get_user():
    user = {
        "_id": uuid.uuid4().hex,
        "full_name": request.form.get('full_name'),
        "email": request.form.get('email'),
        "password": request.form.get('password')
    }
    if db.students.find_one({"email": user['email']}):
        return jsonify({"error": "email already exist"}), 400
    db.students.insert_one(user)
    return jsonify(user), 200


@app.route('/signup')
def signup():
    return render_template("signup.html")
# @app.route('/dashboard')
# def dashboard():
#     user=db.students.find_one({'_id':app.config['userid']})
#     name=user['full_name']
#     collegeId=str(user['email']).split("@")[0].upper()
#     return render_template("dashboard.html",name=name,rollID=collegeId)


@app.route('/dashboard')
def dashboard():
    # user=db.students.find_one({'_id':app.config['userid']})
    # name=user['full_name']
    # collegeId=str(user['email']).split("@")[0].upper()
    return render_template("dashboard.html")


if __name__ == '__main__':
    app.run()
