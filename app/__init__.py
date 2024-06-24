import os
import re

from peewee import *
from playhouse.shortcuts import model_to_dict
import datetime

from flask import Flask, render_template, request, jsonify
from dotenv import load_dotenv
from app.text import about_text, work_text, about_text_maya, work_text_maya, education_text, education_text_maya

load_dotenv('./environment.env')
app = Flask(__name__)

if os.getenv("TESTING") == "true":
    print("Running in test mode")
    mydb = SqliteDatabase('file:memory?mode=memory&cache=shared', uri=True)
else:
    mydb = MySQLDatabase(os.getenv("MYSQL_DATABASE"),
        user=os.getenv("MYSQL_USER"), 
        password=os.getenv("MYSQL_PASSWORD"), 
        host=os.getenv("MYSQL_HOST"), 
        port=3306)

print(mydb)

class TimelinePost(Model):
    name = CharField()
    email = CharField()
    content = TextField()
    created_at = DateTimeField(default=datetime.datetime.now)

    class Meta:
        database = mydb

mydb.connect()
mydb.create_tables([TimelinePost])

def mapping(coords):
    markers = ""

    for id, (lat, lon) in enumerate(coords):
        # Create the marker and its pop-up for each shop
        idd = f"a{id}"
        markers += "var {idd} = L.marker([{latitude}, {longitude}]);\
                            {idd}.addTo(map);".format(
            idd=idd,
            latitude=lat,
            longitude=lon,
        )
    return coords, markers  


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

@app.route('/api/timeline_post', methods=['POST'])
def post_time_line_post():
    try:
        name = request.form["name"]
    except:
        return jsonify({"error": "Invalid name"}), 400

    emailPattern = r"[^@]+@[^@]+\.[^@]+"
    try:
        email = request.form["email"]
        if not re.match(emailPattern, email):
            return jsonify({"error": "Invalid email format"}), 400
    except:
        return jsonify({"error": "Invalid email"}), 400

    try:
        content = request.form["content"]
        if not content:
            return jsonify({"error": "Invalid content"}), 400
    except:
        return jsonify({"error": "Invalid content"}), 400

    timeline_post = TimelinePost.create(name=name, email=email, content=content)

    if timeline_post:
        return model_to_dict(timeline_post)
    else:
        return jsonify({'error': 'Failed to create timeline post'}), 400

@app.route('/api/timeline_post', methods=['GET'])
def get_time_line_post():
    return {
        'timeline_post': [
            model_to_dict(p)
            for p in TimelinePost.select().order_by(TimelinePost.created_at.desc())
        ]
    }

@app.route('/timeline')
def timeline():
    timeline_post = get_time_line_post()
    return render_template('timeline.html', title="Timeline", timeline_post=timeline_post)

if __name__ == "__main__":
    app.run()