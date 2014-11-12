import os
from flask import Flask
from flask import render_template
from flask import jsonify
from flask import request
import requests

app = Flask(__name__)

@app.route("/")
def index():
    url = "http://api.db-ip.com/addrinfo?addr={}&api_key=5d9dd65d7e5387f647dfbec122537e3e35ddecae".format(request.remote_addr)
    addr = requests.get(url)
    return str(addr)

@app.route("/<city>")
def weather(city):
    url = 'http://api.openweathermap.org/data/2.5/weather?q={}'.format(city)
    response = requests.get(url)
    temp = (response.json()["main"]["temp"] - 273.15)* 1.8000 + 32.00
    temp =  str(temp)
    return render_template("temp.html", city=city, temp=temp)

if __name__ == "__main__":
    app.run(debug=True)