# -*- coding:utf-8 -*-
import base64
import hashlib
from Crypto import Random
from Crypto.Cipher import AES

class AESCipher(object):

    def __init__(self, key): 
        self.bs = 32
        #self.key = hashlib.sha256(key.encode()).digest()
        self.key = key
        self.iv = "insert iv"

    def encrypt(self, raw):
        raw = self._pad(raw)
        #iv = Random.new().read(AES.block_size)
        #print base64.b64encode(iv)
        print self.key
        cipher = AES.new(self.key, AES.MODE_CBC, base64.b64decode(self.iv))
        return base64.b64encode(cipher.encrypt(raw))
#        string =cipher.encrypt(raw)
 #       return string.encode("hex")

    def decrypt(self, enc):
        enc = base64.b64decode(enc)
        #iv = enc[:AES.block_size]
        cipher = AES.new(self.key, AES.MODE_CBC, base64.b64decode(self.iv))
        #return self._unpad(cipher.decrypt(enc[AES.block_size:])).decode('utf-8')
        return self._unpad(cipher.decrypt(enc)).decode('utf-8')

    def _pad(self, s):
        return s + (self.bs - len(s) % self.bs) * chr(self.bs - len(s) % self.bs)

    @staticmethod
    def _unpad(s):
        return s[:-ord(s[len(s)-1:])]
        
         
if __name__ == "__main__":

    aes = AESCipher("motdepasse123456")
    print aes.encrypt("oh oui chiffre moi ça")


 
