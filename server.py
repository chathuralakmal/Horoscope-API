from flask import Flask, jsonify
from horoscope import Horoscope

app = Flask (__name__)

############################################
# Index 
############################################

@app.route ('/', methods=['GET'])
def index_route () :
    return jsonify({
		'author' : 'Tapasweni Pathak',
		'author_url' : 'http://tapasweni-pathak.github.io/',
		'base_url' : 'horoscope-api.herokuapp.com',
	    	'project_name' : 'Horoscope API',
		'project_url' : 'http://tapasweni-pathak.github.io/Horoscope-API'
	})


############################################
# Horoscopes
###########################################

#Todays' Horoscope
@app.route ('/horoscope/today/<sunsign>', methods=['GET'])
def today_horoscope_route (sunsign) :
	result = dict (Horoscope.get_todays_horoscope (sunsign))
	return jsonify (date=result['date'],
			sunsign=result['sunsign'],
			horoscope=result['horoscope'])
					

#Current Week Horoscope
@app.route ('/horoscope/week/<sunsign>', methods=['GET'])
def weekly_horoscope_route (sunsign) :
	result = dict (Horoscope.get_weekly_horoscope (sunsign))
	return jsonify (week=result['week'],
			sunsign=result['sunsign'],
			horoscope=result['horoscope'])

#Current Month Horoscope
@app.route ('/horoscope/month/<sunsign>', methods=['GET'])
def monthly_horoscope_route (sunsign) :
	result = dict (Horoscope.get_monthly_horoscope (sunsign))
	return jsonify (month=result['month'],
			sunsign=result['sunsign'],
			horoscope=result['horoscope'])

#Current Year Horoscope
@app.route ('/horoscope/year/<sunsign>', methods=['GET'])
def yearly_horoscope_route (sunsign) :
	result = dict (Horoscope.get_yearly_horoscope (sunsign))
	return jsonify (year=result['year'],
			sunsign=result['sunsign'],
			horoscope=result['horoscope'])


###########################################
# More Information About A Sunsign
###########################################

@app.route ('/knowmore/<sunsign>', methods=['GET'])
def know_more_route (sunsign) :
	result = dict (Horoscope.know_all_about (sunsign))
	return jsonify (sanskrit_name=result['sanskrit_name'],
			meaning_of_name=result['meaning_of_name'],
			lord=result['lord'],
			lucky_color=result['lucky_color'],
			lucky_day=result['lucky_day'],
			lucky_number=result['lucky_number'])
					

###########################################
#Start Flask
###########################################

if __name__ == "__main__":
	app.run()