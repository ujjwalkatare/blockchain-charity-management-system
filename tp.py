# importing the required libraries  
import hashlib  
import json  
from time import time  
  
# creating the Block_chain class  
class Block_chain(object):  
    def __init__(self):  
        self.chain = []  
        self.pendingTransactions = []  
  
        self.newBlock(previousHash = "Transaction History Blocks", the_proof = 'Username')  

    def newBlock(self, the_proof, previousHash = None):  
        the_block = {  
            'index': len(self.chain) + 1,  
            'timestamp': time(),  
            'transactions': self.pendingTransactions,  
            'proof': the_proof,  
            'previous_hash': previousHash or self.hash(self.chain[-1]),  
        }  
        self.pendingTransactions = []  
        self.chain.append(the_block)  
        self.saveChainToJson()  # Save the updated chain to JSON file
        return the_block  
  
    #Searching the blockchain for the most recent block.  
    @property  
    def lastBlock(self):  
        return self.chain[-1]  
  
    # Adding a transaction with relevant info to the 'blockpool' - list of pending tx's.   
    def newTransaction(self, the_sender, the_recipient, the_amount):  
        the_transaction = {  
            'sender': the_sender,  
            'recipient': the_recipient,  
            'amount': the_amount  
        }  
        self.pendingTransactions.append(the_transaction)  
        return self.lastBlock['index'] + 1  
  
    # receiving one block. Turning it into a string, turning that into  
    # Unicode (for hashing). Hashing with SHA256 encryption,  
    # then translating the Unicode into a hexadecimal string.  
    def hash(self, the_block):  
        stringObject = json.dumps(the_block, sort_keys = True)  
        blockString = stringObject.encode()  
  
        rawHash = hashlib.sha256(blockString)  
        hexHash = rawHash.hexdigest()  
  
        return hexHash
    
    # Save the blockchain to a JSON file
    def saveChainToJson(self):
        with open('chain.json', 'w') as file:
            json.dump(self.chain, file)

# Load blockchain from JSON file if exists, otherwise create a new blockchain
try:
    with open('chain.json', 'r') as file:
        blockchain_data = json.load(file)
        block_chain = Block_chain()
        block_chain.chain = blockchain_data
except FileNotFoundError:
    block_chain = Block_chain()


transaction6 = block_chain.newTransaction("Justin", "Alex", '1 BTC')  
block_chain.newBlock(10384)  