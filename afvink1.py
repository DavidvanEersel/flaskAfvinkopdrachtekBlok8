from flask import Flask, render_template, request
import zoek_in_database

app = Flask(__name__)


@app.route('/', methods=["POST", "GET"])
def home():
    zoekwoord = request.form.get("zoekwoord", '')
    if zoekwoord != '':
        return render_template("afvink1.html", resultaten=zoek_in_database.query(zoekwoord), zoekwoord=zoekwoord)
    else:
        return render_template("afvink1.html")


if __name__ == '__main__':
    app.run()
