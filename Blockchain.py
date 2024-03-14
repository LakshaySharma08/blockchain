from Block import Block
from BlockchainUtils import BlockhainUtils
from AccountModel import AccountModel


class Blockchain():

    def __init__ (self):
        self.blocks = [Block.genesis()]
        self.accountModel = AccountModel()



    def addBlock(self, block):
        self.executeTransactions(block.transactions)
        self.blocks.append(block)

    def toJson(self):
        data = {}
        jsonBlocks = []
        for block in self.blocks:
            jsonBlocks.append(block.toJson())
        data['blocks'] = jsonBlocks
        return data
    
    def blockCountValid(self, block):
        if self.blocks[-1].blockCount == block.blockCount - 1:
            return True
        else:
            return False
        
    def lastBlockHashValid(self, block):
        latestBlockchainBlockHash = BlockhainUtils.hash(self.blocks[-1].payload()).hexdigest()

        if latestBlockchainBlockHash == block.lastHash:
            return True
        else:
            return False
        
    def getCoveredTransaction(self, transactions):
        coveredTransactions = []
        for transaction in transactions:
            if self.transactionCovered(transaction):
                coveredTransactions.append(transaction)
            else:
                print('Transaction is not covered by sender')

        return coveredTransactions

    def transactionCovered(self, transaction):

        if transaction.type == 'EXCHANGE':
            return True

        senderBalance = self.accountModel.getBalance(transaction.senderPublicKey)

        if senderBalance >= transaction.amount:
            return True
        else:
            return False
        
    def excecuteTransaction(self, transaction):
        sender = transaction.senderPublicKey
        reciever = transaction.recieverPublicKey
        amount = transaction.amount
        self.accountModel.updateBalance(sender, -amount)
        self.accountModel.updateBalance(reciever, amount)

    def executeTransactions(self, transactions):
        for transaction in transactions:
            self.excecuteTransaction(transaction)
