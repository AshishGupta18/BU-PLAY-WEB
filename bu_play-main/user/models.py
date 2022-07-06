import json
from flask import Flask,jsonify,request
import uuid
from App import db
class User:
    def signup(self):
        user={
            "_id":uuid.uuid4(),
            "full_name":request.form.get('full_name'),
            "email":request.form.get('email'),
            "password":request.form.get('password')
        }
        db.users.insert_one(user)
        
        return jsonify(user),200
   