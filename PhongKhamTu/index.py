from flask import render_template

from PhongKhamTu import app


@app.route("/")
def index():
    categories=({
        "id":1,
        "name": "Đăng kí khám bệnh"
    },{
        "id": 2,
        "name": "Đăng nhập"
    })

    return render_template("index.html",categories=categories)
if __name__ == '__main__':
    app.run(debug=True)
