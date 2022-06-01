from flask import Flask,jsonify, redirect,request
from cryptage import Cryptage
import requests


app = Flask(__name__)
mdp = "passer123"


@app.route('/apptoapi',methods=['POST','GET'])
def appToApi():
    data = request.get_json(force=True)
    cryptage = Cryptage(mdp, data)
    cryptedData = cryptage.crypter()
    url = "http://127.0.0.1:8080/signup"
    response = requests.post(url,json=cryptedData)
    return cryptedData

@app.route('/apitoapp',methods=['POST','GET'])
def apiToApp():
    pass

    
app.run(host='127.0.0.1',port=5000)
