
import time
import flask 
import os
import random
import requests
import urllib.request
import urllib
import wget



app = flask.Flask(__name__)
 
@app.route('/')
 
def index():

    hello = "Hello World"
    
    
    
    

    
    return flask.render_template(
        
        "index.html",
        hello=hello
        
        
        
        )
    
app.run(
    
    port=int(os.getenv('PORT',8080)),
    host = os.getenv('IP','0.0.0.0')
    
    )
    
    