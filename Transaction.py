import uuid 
import time
import copy

class Transaction():
    def __init__ (self, senderPublicKey, recieverPublicKey, amount, type):
        self.senderPublicKey = senderPublicKey
        self.recieverPublicKey = recieverPublicKey
        self.amount = amount
        self.type = type
        self.id = uuid.uuid1().hex
        self.timestamp = time.time()
        self.signature = ''

    def toJson(self):
        return self.__dict__
    
    def sign(self, signature):
        self.signature = signature

    def payload(self):
        jsonRepresentation = copy.deepcopy(self.toJson())
        jsonRepresentation['signature'] = ''
        return jsonRepresentation