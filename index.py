import os
from flask import Flask
from flask import render_template
from flask import jsonify
from flask import request
import requests

app = Flask(__name__)

def forecast(city, state, country, days):
	url = "http://api.openweathermap.org/data/2.5/forecast/daily?mode=json&cnt={}&q={},{},{}".format(days, city, state, country)
	response = requests.get(url)
	forecast_list = response.json()["list"]
	return forecast_list

def today_temp(city, state, country):
	url = 'http://api.openweathermap.org/data/2.5/weather?q={},{},{}'.format(city, state, country)
	response = requests.get(url)
	temp = (response.json()["main"]["temp"] - 273.15)* 1.8000 + 32.00
	temp =  str(int(temp))
	return temp
    
def coarse_addr(ip):
	url = "http://api.db-ip.com/addrinfo?addr={}&api_key=5d9dd65d7e5387f647dfbec122537e3e35ddecae".format(ip)
	addr = requests.get(url).json()
	return addr

@app.route("/")
def index():
	ip = request.access_route[0]
	addr = coarse_addr(ip)
	temp = today_temp(addr["city"], addr["stateprov"], addr["country"])
	forecast_list = forecast(addr["city"], addr["stateprov"], addr["country"], 7)
	return render_template("index.html",city=addr["city"],temp=temp, forecast_list=forecast_list)

@app.route("/<city>")
def weather(city):
	url = 'http://api.openweathermap.org/data/2.5/weather?q={}'.format(city)
	response = requests.get(url)
	temp = (response.json()["main"]["temp"] - 273.15)* 1.8000 + 32.00
	temp =  str(temp)
	return render_template("temp.html", city=city, temp=temp)

if __name__ == "__main__":
    app.run(debug=True)
    
