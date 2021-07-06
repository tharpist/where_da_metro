from forms import InputForm
from flask import Flask, render_template, redirect, request, url_for
import os
from wamata import fetch_data, get_station, send_message  
app = Flask(__name__)


@app.route('/', methods=['POST', 'GET'])
def home():
    if request.method == 'POST':
        station = get_station(request.form['nm'])
        data = fetch_data(station)
        message = send_message(data)
        return redirect(url_for('station', a_data=message))
    if request.method == 'GET':
        print(request.method)
        return render_template('index.html')

@app.route('/<a_data>')
def station(a_data):
    return f"<h1>{a_data}<h1>"

#default port:
if __name__ == '__main__':
    app.run()

#station_name = 'a09'

#station = get_station(station_name)

#data = fetch_data(station)

#print(data)