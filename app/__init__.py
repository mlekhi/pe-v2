import os
import re

import datetime

from flask import Flask, render_template, request, jsonify
from app.text import about_text_maya, work_text_maya, education_text_maya
from dotenv import load_dotenv

app = Flask(__name__)

@app.route("/")
def index():
    coords = [(19.43260, -99.133209), (39.9526, -75.1652), (6.3690, 34.8888), (52.3676,4.9041)]

    # Render the page with the map
    return render_template(
        "index.html",
        markers=mapping(coords)[1],
        lat=(mapping(coords))[0][0][0],
        lon=(mapping(coords))[0][0][1],
        title="Maya Lekhi",
        url=os.getenv("URL"),
        photo="profile",
        about_text=about_text_maya,
        work_text=work_text_maya,
        education_text=education_text_maya
    )

@app.route("/hobbies")
def hobbies():
    title = "Our Team's Hobbies"
    hobbies_list = [
        {"title": "Reading", "image": "static/img/reading.jpg"},
        {"title": "Gardening", "image": "static/img/gardening.jpg"},
        {"title": "Painting", "image": "static/img/painting.jpg"},
        {"title": "Cooking", "image": "static/img/cooking.jpg"},
    ]

    return render_template("hobbies.html", title=title, hobbies_list=hobbies_list)

if __name__ == "__main__":
    app.run()