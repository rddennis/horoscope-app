from flask import Flask, render_template, request, redirect
from livereload import Server
from horoscope import Horoscope

import urllib2
import json
import pprint

app = Flask(__name__)
app.debug = True

@app.route('/')
def home():
	return render_template('home.html')

@app.route('/search', methods=["GET", "POST"])
def search():
	print request.method
	if request.method == "POST":
		sign = request.form['sign']
		return redirect('/horoscopes/%s' %sign)

@app.route('/findSign')
def find_by_birthday():
	return render_template('findSign.html')

@app.route('/findSignBday', methods=["GET", "POST"])
def findSign():
	if request.method == "POST":
		month = request.form['month']
		day = int(request.form['day'])

	if month == "January":
		if day >= 21:
			sign = "Aquarius"
		else:
			sign = "Capricorn"
	elif month == "February":
		if day >= 18:
			sign = "Pisces"
		else:
			sign = "Aquarius"
	elif month == "March":
		if day >= 20:
			sign = "Aries"
		else:
			sign = "Pisces"
	elif month == "April":
		if day >= 20:
			sign = "Taurus"
		else:
			sign = "Aries"
	elif month == "May":
		if day >= 21:
			sign = "Gemini"
		else:
			sign = "Taurus"
	elif month == "June":
		if day >= 21:
			sign = "Cancer"
		else:
			sign = "Gemini"
	elif month == "July":
		if day >= 23:
			sign = "Leo"
		else:
			sign = "Cancer"
	elif month == "August":
		if day >= 23:
			sign = "Virgo"
		else:
			sign = "Leo"
	elif month == "September":
		if day >= 23:
			sign = "Libra"
		else:
			sign = "Virgo"
	elif month == "October":
		if day >= 23:
			sign = "Scorpio"
		else: 
			sign = "Libra"
	elif month == "November":
		if day >= 22:
			sign = "Sagittarius"
		else:
			sign = "Scorpio"
	elif month == "December":
		if day >= 22:
			sign = "Capricorn"
		else:
			sign = "Sagittarius"

	return redirect('/horoscopes/%s' %sign)


@app.route('/horoscopes/<sun_sign>')
def horoscopes(sun_sign):
	sun_sign = sun_sign
	daily = Horoscope.get_todays_horoscope(sun_sign)
	weekly = Horoscope.get_weekly_horoscope(sun_sign)
	yearly = Horoscope.get_yearly_horoscope(sun_sign)
	image_link = '/static/images/%s.jpg' %sun_sign
	return render_template('horoscopes.html', sun_sign = sun_sign, daily_horoscope = daily, weekly_horoscope = weekly, yearly_horoscope = yearly, image = image_link)

Server(app.wsgi_app).serve()

