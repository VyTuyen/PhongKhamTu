from flask import render_template, request, redirect, session
from flask_login import login_user, logout_user
from PhongKhamTu import dao, app
from PhongKhamTu.decorators import annonynous_user

def login_my_user():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        user = dao.auth_user(username=username, password=password)
        if user:
            login_user(user=user)
            n = request.args.get('next')
            return redirect(n if n else '/')

    return render_template('login.html')


def logout_my_user():
    logout_user()
    return redirect('/login')
def register():
    err_msg = ''
    if request.method == 'POST':
        password = request.form['registerPassword']
        confirm = request.form['registerConfirmPassword']
        if password.__eq__(confirm):
            try:
                dao.register(hoten=request.form['registerName'],
                             email=request.form['registerEmail'],
                             password=password,
                             username=request.form['registerName'])

                return redirect('/login')
            except:
                err_msg = 'Đã có lỗi xảy ra! Vui lòng quay lại sau!'
        else:
            err_msg = 'Mật khẩu KHÔNG khớp!'

    return render_template('register.html', err_msg=err_msg)


