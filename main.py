from flask import Flask, request, render_template

import pickledb

db = pickledb.load("stream2.db", True)

app = Flask(__name__)

@app.route("/")
def allowee():
  return render_template("index.html")

@app.route("/register", methods=["POST"])
def bros_d_bros():
  first_name = request.form["first_name"]
  last_name = request.form["last_name"]

  db.set("first_name", first_name)
  db.set("last_name", last_name)
  db.dump()

  return "Welcome, {} {}!".format(first_name, last_name)


if __name__ == "__main__":
  app.run("0.0.0.0", 5000)