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
            data = Padding.pad(self.dict[e].encode(),16)
            #chiffrer les donnees
            encoded = base64.b64encode(cipher.encrypt(data))
            self.dict[e] = encoded.decode('ascii')
            print(self.dict[e])
        return self.dict
    
        

    def decrypter(self):
        hashword = hashlib.sha256(self.password.encode()).digest()
        cipher = AES.new(hashword,AES.MODE_CBC,self.iv)
        for e in self.dict:
            data = cipher.decrypt(base64.b64decode(self.dict[e]))
            self.dict[e] = Padding.unpad(data,16).decode()
            print(self.dict[e])
        return self.dict

# myDict = {
#     "email":"pmg@gmail.com",
#     "mot de passe":"passer"
# }
# testCrypt1 = Cryptage(password="passer",dict=myDict)
# testCrypt2 = Cryptage(password="passer",dict=myDict)
# print(testCrypt1.dict)
# print("*******************")
# print(testCrypt1.crypter())
# print("*******************")
# print(testCrypt2.decrypter())



