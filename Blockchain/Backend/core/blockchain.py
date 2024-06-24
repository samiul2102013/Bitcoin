import sys
import time
sys.path.append('C:/Users/acer/OneDrive/Desktop/Bitcoin')
from Blockchain.Backend.core.block import Block
from Blockchain.Backend.core.blockheader import BlockHeader
from Blockchain.Backend.util.util import hash256

zero_HASH = '0' * 64
VERSION = 1

class Blockchain:
    def __init__(self):
        self.chain = []
        self.GenesisBlock()

    def GenesisBlock(self):
        BlockHeight = 0
        prevBlockHash = zero_HASH
        self.addBlock(BlockHeight, prevBlockHash)

    def addBlock(self, BlockHeight, prevBlockHash):
        timestamp = int(time.time())
        Transaction = f"Codes Alert sent {BlockHeight} bitcoin to Joe"
        merkleRoot = hash256(Transaction.encode()).hex()
        bits = 'ffff001f'
        blockHeader = BlockHeader(VERSION, prevBlockHash, merkleRoot, timestamp, bits)
        blockHeader.mine()
        self.chain.append(Block(BlockHeight, 1, blockHeader, 1, Transaction))
        print(self.chain)

if __name__ == "__main__":
    blockchain = Blockchain()
