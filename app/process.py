# importing the required libraries  
import hashlib  
import json  
from time import time  

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
        with open('chain/chain.json', 'w') as file:
            json.dump(self.chain, file)
