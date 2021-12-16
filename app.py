from flask import *
import json

with open("static/what.json") as file:
    database = json.load(file)

app = Flask(__name__)

@app.route("/")
async def slash():
    return render_template("index.html", database=database.keys())

@app.route("/getkey", methods=["GET", "POST"])
async def getkeyalso():
    try:
        key = request.form['key']
    except KeyError:
        abort(400)
    try:
        verif = request.form['verificationkey']
    except KeyError: verif = "invalid"
    if request.method == "GET" or verif != "f":
        return redirect(301, "/")
    return await getkey(key)

@app.route("/<key>")
async def getkey(key):
    try:
        database[key]
    except KeyError:
        abort(404)
    return render_template("viewer.html", key=database[key])
