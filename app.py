from flask import Flask,request,jsonify
from cryptage import Cryptage
import requests


app = Flask(__name__)
mdp = "passer123"
dburl = "http://127.0.0.1:8080/signup/"

@app.route('/apiEncrypt',methods=['POST','GET'])
def toApi():
    data = request.get_json(force=True)
    print(data)
    cryptage = Cryptage(mdp, data)
    print("Cryptage en cours...")
    cryptedData = cryptage.crypter()
    print("termine !")
    # url = request.environ['REMOTE_ADDR']+":"+str(request.environ['REMOTE_PORT'])
    # print(f"==>{url}")
    url = dburl
    try:
        requests.post(url,json=cryptedData)
    except requests.RequestException as e:
        print(f"Erreur connection au serveur ==>{e}")
    return jsonify(cryptedData)

@app.route('/apiDecrypt',methods=['POST','GET'])
def fromApi():
    data = request.get_json(force=True)
    cryptage = Cryptage(mdp, data)
    print("Decrypatage en cours...")
    decryptedData = cryptage.decrypter()
    print("termine !")
    # url = request.environ['REMOTE_ADDR']+":"+str(request.environ['REMOTE_PORT'])
    # print(f"==>{url}")
    # try:
    #     requests.post(url,json=decryptedData)
    # except requests.RequestException as e:
    #     print(f"Erreur connection au serveur ==>{e}")
    return decryptedData

    
app.run(host='127.0.0.1',port=5000)
