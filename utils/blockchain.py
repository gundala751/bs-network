class Transaction:
    def __init__(self, sender, recipient, amount):
        self.sender = sender
        self.recipient = recipient
        self.amount = amount

class Block:
    def __init__(self, index, previous_hash, transactions, timestamp):
        self.index = index
        self.previous_hash = previous_hash
        self.transactions = transactions
        self.timestamp = timestamp

class Blockchain:
    def __init__(self):
        self.chain = []
        self.current_transactions = []
        self.create_block(previous_hash='1')  # create the genesis block

    def create_block(self, previous_hash, timestamp=None):
        block = Block(
            index=len(self.chain) + 1,
            previous_hash=previous_hash,
            transactions=self.current_transactions,
            timestamp=timestamp or time.time(),
        )
        self.current_transactions = []  # reset the list of current transactions
        self.chain.append(block)
        return block

    def new_transaction(self, sender, recipient, amount):
        transaction = Transaction(sender, recipient, amount)
        self.current_transactions.append(transaction)
        return self.last_block.index + 1  # return the index of the block that will hold this transaction

    @property
    def last_block(self):
        return self.chain[-1]