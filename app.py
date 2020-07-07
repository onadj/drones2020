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
    return render_template("drones.html", drones=mongo.db.drones.find())

@app.route('/add_drone')
def add_drone():
    return render_template('add_drone.html',categories=mongo.db.categories.find())

@app.route('/insert_drone', methods=['POST'])
def insert_drone():
    drones = mongo.db.drones
    drones.insert_one(request.form.to_dict())
    return redirect(url_for('get_drones'))

@app.route('/edit_drone/<drone_id>')
def edit_drone(drone_id):
    the_drone =  mongo.db.drones.find_one({"_id": ObjectId(drone_id)})
    all_categories =  mongo.db.categories.find()
    return render_template('edit_drone.html', drone=the_drone,
                           categories=all_categories)


if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)

