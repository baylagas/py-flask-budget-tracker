from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "mysql://root:root@localhost:3306/budget_tracker_db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["SECRET_KEY"] = "horrible_secret_key"


""" with app.app_context():
    db.create_all() """


@app.route("/")
def home():
    return "hello world"


if __name__ == "__main__":
    app.run(debug=True)
