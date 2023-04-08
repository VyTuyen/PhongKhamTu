from flask import render_template, redirect,request
from PhongKhamTu import app, admin,dao, controllers,utils
from flask_login import login_user, logout_user
from PhongKhamTu.model import UserRole

@app.route("/")
def index():
    return render_template("index.html")
@app.route("/register")
def my_register():
    return render_template('register.html')
# @app.route("/admin-login",methods=['post'])
# def signin_admin():
#     username = request.form['username']
#     password = request.form['password']
#
#     user = dao.check_login(username=username, password=password, role=UserRole.ADMIN)
#     if user:
#         login_user(user=user)
#     return redirect('/admin')
if __name__ == '__main__':
    app.run(debug=True)
