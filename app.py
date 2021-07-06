from forms import InputForm
from flask import Flask, render_template, redirect, request, url_for
import os
from wamata import fetch_data, get_station, send_message  
app = Flask(__name__)


@app.route('/', methods=['POST', 'GET'])
def home():
    if request.method == 'POST':
        station_name = request.form['nm']
        return  redirect(url_for('station',
         station_name=station_name))
    if request.method == 'GET':
        print(request.method)
        return render_template('index.html')

@app.route('/<station_name>')
def station(station_name):
    station_url = get_station(station_name)
    train_data = fetch_data(station_url)
    message = send_message(train_data)
    #return render_template('input.html')
    return f"<h1>{message}<h1>"

#default port:
if __name__ == '__main__':
    app.run()

#station_name = 'a09'

#station = get_station(station_name)

#data = fetch_data(station)

#print(data)