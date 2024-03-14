

class AccountModel():
    def __init__(self):
        self.accounts = []
        self.balances = {}
    
    def addAccount(self, pubblicKeyString):

        if not pubblicKeyString in self.accounts:
            self.accounts.append(pubblicKeyString)
            self.balances[pubblicKeyString] = 0

    def getBalance(self, publicKeyString):
        if publicKeyString not in self.accounts:
            self.addAccount(publicKeyString)
        return self.balances[publicKeyString]
    
    def updateBalance(self, publicKeyString, amount):

        if publicKeyString not in self.accounts:
            self.addAccount(publicKeyString)

        self.balances[publicKeyString] += amount
        