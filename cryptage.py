from Crypto.Cipher import AES
from Crypto.Util import Padding
import hashlib
import base64
class Cryptage():

    def __init__(self,password,dict):
        self.password = password
        self.iv = "unvecteurinitial".encode()
        self.dict = dict
    

    def crypter(self):
        #hasher le mot de passe
        hashword = hashlib.sha256(self.password.encode()).digest()
        cipher = AES.new(hashword,AES.MODE_CBC,self.iv)
        for e in self.dict:
            #ajouter du padding pour faire des blocs egaux
            try:
                data = Padding.pad(self.dict[e].encode(),16)
                encoded = base64.b64encode(cipher.encrypt(data))
                self.dict[e] = encoded.decode('ascii')
            except AttributeError:
                self.dict[e] = self.dict[e]*30 + 100
                #print(type(data))
                print("Attention: les entiers seront convertis en string")
            #chiffrer les donnees
           
        return self.dict
    
        

    def decrypter(self):
        hashword = hashlib.sha256(self.password.encode()).digest()
        cipher = AES.new(hashword,AES.MODE_CBC,self.iv)
        for e in self.dict:
            try:
                data = cipher.decrypt(base64.b64decode(self.dict[e]))
                try:
                    self.dict[e] = Padding.unpad(data,16).decode()
                except ValueError as e:
                    print(f"Le decryptage a echoue :( \nErreur=>{e}")
                    break
                try:
                    self.dict[e] = Padding.unpad(data,16).decode()
                except ValueError as e:
                    print(f"Le decryptage a echoue :( \nErreur=>{e}")
                    break
            except TypeError:
                self.dict[e] = (self.dict[e]-100)//30

        return self.dict

# dict = {
#     "nom" : "diouf",
#     "prenom":"ibrahima",
#     "age": 35,
#     "salaire" : 850000,
#     "nb Enfants":22,
#     "email":"mignane@esp.sn"
# }
# print(dict)

# monCrypt = Cryptage("passer123",dict)
# print(monCrypt.crypter())
# print(monCrypt.decrypter())
