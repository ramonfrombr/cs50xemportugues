from flask import Flask, render_template
from cs50x import cs50x


app = Flask(__name__)

app.register_blueprint(cs50x, url_prefix='/2022')


if __name__ == '__main__':
    app.run()