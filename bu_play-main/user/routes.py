
from user.models import User
from App import app
@app.route('/user/signup',methods=['POST'])
def get_user():
    print("kdsfjkldsfj")
    print("dfljdljkfldsjf")
    return User().signup()