from flask import Flask, render_template, abort
from typing import Literal 

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/<unit_str>")
def constituet_unit(unit_str: Literal["lpr", "dpr", "zo", "ho"]):
    unit = unit_str.lower().strip()
    if unit not in ("lpr", "dpr", "zo", "ho"):
        raise abort(404)
    return render_template(f'unit_{unit}.html')
    
@app.errorhandler(404)
def not_found_handler(_):
    return render_template('error_404.html')

if __name__ == "__main__":
    app.run()
