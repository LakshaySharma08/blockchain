from Cryptodome.Hash import SHA256
import json
import jsonpickle

class BlockhainUtils():

    @staticmethod
    def hash(data):
        dataString = json.dumps(data)
        dataBytes = dataString.encode('utf-8')
        datahash = SHA256.new(dataBytes)
        return datahash
    
    @staticmethod
    def encode(objectToEncode):
        return jsonpickle.encode(objectToEncode, unpicklable = True)
    
    @staticmethod
    def decode(encodedObject):
        return jsonpickle.decode(encodedObject)