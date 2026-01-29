import hashlib
import json
import time
import os


class Block_chain:
    def __init__(self):
        self.chain = []
        self.transactions = []

        # Create genesis block if chain is empty
        if not self.chain:
            self.new_block(previous_hash="0")

    # ----------------------------------------
    # Create a new block
    # ----------------------------------------
    def new_block(self, miner):
        block = {
            "index": len(self.chain) + 1,
            "timestamp": time.time(),
            "transactions": self.transactions,
            "miner": miner,
            "previous_hash": self.hash(self.chain[-1]) if self.chain else "0",
        }

        self.transactions = []
        self.chain.append(block)
        self.save_chain()
        return block

    # ----------------------------------------
    # Add a new transaction
    # ----------------------------------------
    def newTransaction(self, sender, receiver, amount):
        transaction = {
            "sender": sender,
            "receiver": receiver,
            "amount": amount,
            "timestamp": time.time(),
            "hash": self.transaction_hash(sender, receiver, amount),
        }

        self.transactions.append(transaction)
        return self.last_block["index"] + 1 if self.chain else 1

    # ----------------------------------------
    # Hash a block
    # ----------------------------------------
    @staticmethod
    def hash(block):
        block_string = json.dumps(block, sort_keys=True).encode()
        return hashlib.sha256(block_string).hexdigest()

    # ----------------------------------------
    # Hash a transaction
    # ----------------------------------------
    @staticmethod
    def transaction_hash(sender, receiver, amount):
        data = f"{sender}{receiver}{amount}{time.time()}"
        return hashlib.sha256(data.encode()).hexdigest()

    # ----------------------------------------
    # Get last block
    # ----------------------------------------
    @property
    def last_block(self):
        return self.chain[-1]

    # ----------------------------------------
    # Save blockchain to JSON file
    # ----------------------------------------
    def save_chain(self):
        os.makedirs("chain", exist_ok=True)
        with open("chain/chain.json", "w") as file:
            json.dump(self.chain, file, indent=4)

    # ----------------------------------------
    # Load blockchain from JSON file
    # ----------------------------------------
    def load_chain(self):
        try:
            with open("chain/chain.json", "r") as file:
                self.chain = json.load(file)
        except FileNotFoundError:
            self.chain = []
