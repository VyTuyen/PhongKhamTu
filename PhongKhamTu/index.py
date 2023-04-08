from flask import render_template, redirect,request
from PhongKhamTu import app, admin,dao, controllers,utils
from flask_login import login_user, logout_user

# app.add_url_rule('/', 'index', controllers.index, methods=['get', 'post'])
@app.route("/")
def index():
    return render_template("index.html")
@app.route("/medical_registration")
def my_registration():
    return render_template("medical_registration.html")
@app.route("/login")
def my_login():
    return render_template("login.html")
@app.route("/login", methods=['post'])
def my_login_process():
    Username = request.form['username']
    Password = request.form['password']
    u = dao.auth_user(Username, Password)
    if u:
        login_user(user=u)
        next_page = request.args.get('next')
        return redirect(next_page if next_page else '/')
    return render_template('login.html')
@app.route("/logout")
def my_logout():
    logout_user()
    return redirect("/login")
if __name__ == '__main__':
    app.run(debug=True)
