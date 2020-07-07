import os
from flask import Flask, render_template, redirect, request, url_for
from flask_pymongo import PyMongo
from bson.objectid import ObjectId 

app = Flask(__name__)
app.config["MONGO_DBNAME"] = 'drones2020'
app.config["MONGO_URI"] = 'mongodb+srv://onadj:Signacare2020@myfirstcluster-hbcie.mongodb.net/drones2020?retryWrites=true&w=majority'

mongo = PyMongo(app)


@app.route('/')
@app.route('/get_drones')
def get_drones():
    return render_template("adddrones.html", drones=mongo.db.drones.find())


if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)