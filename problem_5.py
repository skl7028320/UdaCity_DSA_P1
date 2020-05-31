import hashlib
from datetime import datetime
import time


class Block:
    def __init__(self, timestamp, data, previous_hash=None):
        self.timestamp = timestamp
        self.data = data
        self.previous_hash = previous_hash
        self.hash = self.calc_hash()
        self.next = None

    def calc_hash(self):
        if self.previous_hash is None:
            hash_str = hash_str = (self.timestamp + self.data).encode('utf-8')
        else:
            hash_str = (self.timestamp + self.data + self.previous_hash).encode('utf-8')

        sha = hashlib.sha256()
        sha.update(hash_str)

        return sha.hexdigest()

    def __repr__(self):
        repr_str = f"""
Block: Timestamp: {self.timestamp}
       Data: {self.data}
       Previous hash: {self.previous_hash}
"""

        return repr_str


class BlockChain:
    def __init__(self):
        self.head = None
        self.num_blocks = 0

    def append(self, new_block):
        if self.head is None:
            self.head = new_block
            self.num_blocks = 1
        else:
            new_block.next = self.head
            self.head = new_block
            self.num_blocks += 1

    def to_list(self):
        output = []

        current_block = self.head
        while current_block:
            output.append(current_block)
            current_block = current_block.next

        output.reverse()

        return output


genesis_timestamp = str(datetime.utcnow().timestamp())
genesis_data = "genesis block"
genesis_block = Block(genesis_timestamp, genesis_data)

block_chain = BlockChain()
block_chain.append(genesis_block)

previous_block = genesis_block
new_block = None
for i in range(1, 6):
    timestamp = str(datetime.utcnow().timestamp())
    data = "transaction " + str(i)
    new_block = Block(timestamp, data, previous_block.hash)
    block_chain.append(new_block)
    previous_block = new_block
    time.sleep(1)

print(block_chain.to_list())

# Every created block chain is different because the timestamp differs for each run. Therefore testing the output is not
# possible.
