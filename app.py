import datetime
import database
from flask import Flask, render_template, request


app = Flask("__name__")

database.create_tables()


@app.route("/home", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        entry_content = request.form.get("content")
        database.create_entries(
            entry_content, datetime.datetime.today().strftime("%b %d")
        )

    return render_template("home.html", entries=database.retrieve_entries())
