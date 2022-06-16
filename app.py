import os 
# import smtplib
from flask import Flask,render_template,request
import csv
import time 


app = Flask(__name__)

def format_server_time():
    server_time =time.localtime()
    return time.strftime("%I:%M:%S %p", server_time)

@app.route("/")
def index():
    context = { 'server_time':format_server_time()}
    return render_template("index.html", context=context)




if __name__=="__main__":
    app.run(debug=True_)


