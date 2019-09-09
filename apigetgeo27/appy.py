from flask import Flask, redirect, request
from geoip import geolite2

app = Flask(__name__)

@app.route("/getgeo/<ip>")
def getgeo_(ip):
    
    match = geolite2.lookup(ip)
    matched = '{"COUNTRY": "'+str(match.country) +'", "SUBDIV": "'+ str(match.subdivisions)[str(match.subdivisions).find("(["):][3:-3]+'"}'
    return matched
    

if __name__ == "__main__":

    app.run(debug=True, threaded=True)    