from flask import Flask, render_template, request, redirect, url_for, session, flash
from werkzeug.security import check_password_hash

from config import Config
from database import init_db, get_connection

app = Flask(__name__)
app.config.from_object(Config)

init_db()


@app.route("/", methods=["GET", "POST"])
def login():

    if request.method == "POST":

        username = request.form["username"]
        password = request.form["password"]

        conn = get_connection()

        admin = conn.execute(
            "SELECT * FROM admin WHERE username=?",
            (username,)
        ).fetchone()

        conn.close()

        if admin and check_password_hash(admin["password"], password):

            session["admin"] = admin["username"]

            return redirect(url_for("dashboard"))

        flash("Username atau Password salah!", "danger")

    return render_template("login.html")


@app.route("/dashboard")
def dashboard():

    if "admin" not in session:
        return redirect(url_for("login"))

    return render_template(
        "dashboard.html",
        username=session["admin"]
    )


@app.route("/logout")
def logout():

    session.clear()

    return redirect(url_for("login"))


if __name__ == "__main__":
    app.run(debug=True)