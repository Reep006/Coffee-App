from flask import Flask, jsonify
from flask import send_from_directory
from flask_cors import CORS
from pymongo import MongoClient
from bson.objectid import ObjectId

app = Flask(
    __name__,
    static_folder="static",
    static_url_path=""
)

CORS(app)

# MongoDB Connection
client = MongoClient("mongodb://localhost:27017/")
db = client["coffeeDB"]
collection = db["coffees"]

# Home Page
@app.route("/")
def home():
    return send_from_directory(app.static_folder, "index.html")

# Get Coffees
@app.route("/get_coffees")
def get_coffees():
    coffees = []
    for coffee in collection.find():
        coffees.append({
            "_id": str(coffee["_id"]),
            "name": coffee["name"],
            "votes": coffee["votes"],
            "image": coffee["image"]
        })
    return jsonify(coffees)

# Vote API
@app.route("/vote/<id>", methods=["POST"])
def vote(id):
    collection.update_one(
        {"_id": ObjectId(id)},
        {"$inc": {"votes": 1}}
    )
    return jsonify({
        "message": "Vote Updated"
    })
if __name__ == "__main__":
    app.run(debug=True)