
#Email Varification Using OTP in Flask

from flask import Flask,render_template,request, redirect
from flask_mail import Mail,Message
from random import randint

app=Flask(__name__)
mail=Mail(app)

app.config["MAIL_SERVER"]='smtp.gmail.com'
app.config["MAIL_PORT"]=587
app.config["MAIL_USERNAME"]='tanisha0714@gmail.com'
app.config['MAIL_PASSWORD']='mayGodblessme'                    #you have to give your password of gmail account
app.config['MAIL_USE_TLS']=True
app.config['MAIL_USE_SSL']=False
mail=Mail(app)
otp=randint(000000,999999)
@app.route('/verify',methods=["POST"])
def verify():
    email=request.form['email']
    msg=Message(subject='OTP',sender='tanisha0714@gmailcom',recipients=[email])
    msg.body=str(otp)
    mail.send(msg)
    return render_template('veri.html')
@app.route('/validate',methods=['POST'])
def validate():
    user_otp=request.form['otp']
    if otp==int(user_otp):
        return "<h3>Email varification succesful</h3>"
    return "<h3>Please Try Again</h3>"
if __name__ == '__main__':
    app.run(debug=True)


