from Cryptodome.Hash import SHA256
import json

class BlockhainUtils():

    @staticmethod
    def hash(data):
        dataString = json.dumps(data)
        dataBytes = dataString.encode('utf-8')
        datahash = SHA256.new(dataBytes)
        return datahash