from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def index():
    categories=({
        "id":1,
        "name": "Đăng kí khám bệnh"
    },{
        "id": 2,
        "name": "Đăng nhập"
    })
    informations=({
        "id": 1,
    "name": "iPhone 7 Plus",
        "description": "Apple, 32GB, RAM: 3GB, iOS13",
        "image":"https://res.cloudinary.com/dxxwcby8l/image/upload/v1647056401/ipmsmnxjydrhpo21xrd8.jpg",
        "category_id": 1
    },)

    return render_template("index.html",categories=categories,informations=informations)
if __name__ == '__main__':
    app.run(debug=True)
