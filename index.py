import os
from flask import Flask
from flask import render_template
from flask import jsonify
from flask import request
import requests
import json

app = Flask(__name__)

def kelvin_to_far(kelvin):
	return (kelvin - 273.15)* 1.8000 + 32.00

def day_forecast(city, state, country, days):
	url = "http://api.openweathermap.org/data/2.5/forecast/daily?mode=json&cnt={}&q={},{},{}".format(days, city, state, country)
	response = requests.get(url)
	forecast_list = response.json()["list"]
	return forecast_list
	
def hour_forecast(city, state, country):
	url = "http://api.openweathermap.org/data/2.5/forecast?mode=json&q={},{},{}".format(city, state, country)
	response = requests.get(url)
	forecast_list = response.json()["list"]
	return forecast_list

def today_temp(city, state, country):
	url = 'http://api.openweathermap.org/data/2.5/weather?q={},{},{}'.format(city, state, country)
	response = requests.get(url)
	temp = kelvin_to_far(response.json()["main"]["temp"])
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
	
	week_forecast_list = day_forecast(addr["city"], addr["stateprov"], addr["country"], 7)
	week_fahrenheits = list(week_forecast_list)
	#creates a list of fahrenheits
	for i in range(len(week_forecast_list)):
		week_fahrenheits[i] = int(kelvin_to_far(week_forecast_list[i]["temp"]["day"]))
	
	hour_forecast_list = hour_forecast(addr["city"], addr["stateprov"], addr["country"])
	hour_forecast_temps = [0]*8
	hour_forecast_labels = [""]*8
	#plucks daily temp, and date-time for the next 24 hours
	for i in range(8):
		hour_forecast_temps[i] = int(kelvin_to_far(hour_forecast_list[i]["main"]["temp"]))
		hour_forecast_labels[i] = hour_forecast_list[i]["dt_txt"]
	
	temp = int(week_fahrenheits[0])
	print hour_forecast_labels
	return render_template("index.html",
		city=addr["city"],
		temp=temp, 
		week_forecast_list=week_fahrenheits,
		hour_forecast_temps=hour_forecast_temps,
		hour_forecast_labels=json.dumps(hour_forecast_labels))

@app.route("/<city>")
def weather(city):
	url = 'http://api.openweathermap.org/data/2.5/weather?q={}'.format(city)
	response = requests.get(url)
	temp = (response.json()["main"]["temp"] - 273.15)* 1.8000 + 32.00
	temp =  str(temp)
	return render_template("temp.html", city=city, temp=temp)

if __name__ == "__main__":
    app.run(debug=True)
    
