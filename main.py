from Transaction import Transaction
from Wallet import Wallet

if __name__ == '__main__':
    amount = 1
    type = 'TRANSFER'
    sender = 'sender'
    reciever = 'reciever'
    
    wallet = Wallet()

    transaction = wallet.createTransaction(reciever, amount, type)

    print(transaction.payload())