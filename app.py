from flask import Flask, render_template


app = Flask(__name__)


@app.route("/")  # function decorator
def hello_world():
    return "<p>aaaa Hello, World!</p>"


import random


@app.route("/lottery")
def get_lottery():

    numbers = list(range(1, 50))

    lottery_numbers = random.sample(numbers, 6)  # 帶 n 個 給 他

    lottery_numbers.sort()

    return render_template(
        "pages/lottery.html", numbers=lottery_numbers
    )  # 設定一個變數擺在lottery.html


@app.route("/about")  # function decorator
def about():
    return render_template("pages/about.html")  # 網域改成


if __name__ == "__main__":
    app.run(port=9999, debug=True)  # 正式的機器不要開debug
