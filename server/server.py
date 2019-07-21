# Authors:
# Nikhil Kumar & Pravat Bhusal

# server imports
from flask import Flask, request
from flask_cors import CORS
server = Flask(__name__)
CORS(server)

# scraper import
from scraper import parse_meals, parse_locations, parse_menu

# import file io packages
import json

# read the scraper config file
scraper_json = json.load(open("../config/scraper.json", "r+"))
dining_url = scraper_json["url"]

# meal selection route
@server.route("/meal", methods=['GET'])
def meal():
    return parse_meals(dining_url)

# locations route
@server.route("/meal/location", methods=['POST'])
def location():
    # receive the meal
    data = json.loads(request.data)
    meal = data["meal"]

    # format the locations URL
    locations_url = dining_url + "location?meal=" + meal
    return parse_locations(locations_url)

# menu route
@server.route("/meal/location/menu", methods=['POST'])
def menu():
    # receive the meal and location
    data = json.loads(request.data)
    meal = data["meal"]
    location = data["location"]

    # format the menu URL
    menu_url = dining_url + "select?meal=" + meal + "&loc=" + location
    return parse_menu(menu_url)

# code to be executed when the server is run
if __name__ == "__main__":
    # read the server config file
    server_json = json.load(open("../config/server.json", "r+"))

    # parse the server config file
    host = server_json["host"]
    port = server_json["port"]

    # run the flask server
    server.run(host, port)
