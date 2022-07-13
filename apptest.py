from flask import Flask,request
from cryptage import Cryptage
import requests


app = Flask(__name__)
mdp = "passer123"


@app.route('/apiEncrypt',methods=['POST','GET'])
def toApi():
    data = request.get_json(force=True)
    cryptage = Cryptage(mdp, data)
    print("Cryptage en cours...")
    cryptedData = cryptage.crypter()
    print("termine !")
    url = request.url
    print(f"==>{url}")
    requests.post(url,json=cryptedData)
    return cryptedData

@app.route('/apiDecrypt',methods=['POST','GET'])
def fromApi():
    data = request.get_json(force=True)
    cryptage = Cryptage(mdp, data)
    print("Decrypatage en cours...")
    decryptedData = cryptage.decrypter()
    print("termine !")
    url = request.url
    print(f"==>{url}")
    requests.post(url,json=decryptedData)
    return decryptedData

    
app.run(host='127.0.0.1',port=4000)
