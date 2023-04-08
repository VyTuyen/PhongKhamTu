from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from urllib.parse import quote
from flask_login import LoginManager

app = Flask(__name__)
app.secret_key='#%^&(*$%^&(78678675$%&^&$^%*&^%&*^'
app.config["SQLALCHEMY_DATABASE_URI"] ="mysql+pymysql://root:%s@localhost/phongkhamtu?charset=utf8mb4" % quote('Y1012Jqkhkp')
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = True

db = SQLAlchemy(app)
<<<<<<< HEAD
login_manager = LoginManager(app=app)
=======
login_manager = LoginManager(app=app)

>>>>>>> c742fa719d8ffa1e1e5c999c866f59d3bb8270b7
