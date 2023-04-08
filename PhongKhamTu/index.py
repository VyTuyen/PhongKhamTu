from flask import render_template

from PhongKhamTu import app, dao, admin, login_manager, controllers


@app.route("/")
def index():
    return render_template("index.html")


@login_manager.user_loader
def load_user(user_id):
    return dao.get_user_by_id(user_id)


app.add_url_rule("/login", "login_my_user", controllers.login_my_user, methods=['get', 'post'])
app.add_url_rule('/logout', "logout_my_user", controllers.logout_my_user)
app.add_url_rule("/register", "register", controllers.register, methods=['get', 'post'])
# app.add_url_rule("/admin-login", "signin_admin", controllers.signin_admin, methods=['post'])
# app.add_url_rule("/doctor-login", "doctor_login", controllers.doctor_login, methods=['get', 'post'])
# app.add_url_rule("/doctor-logout", "doctor_logout", controllers.doctor_logout)
# app.add_url_rule("/staff_login", " staff_login", controllers.staff_login, methods=['get', 'post'])
# app.add_url_rule("/staff_logout", "staff_logout", controllers.staff_logout)

if __name__ == "__main__":
    app.run(debug=True)
