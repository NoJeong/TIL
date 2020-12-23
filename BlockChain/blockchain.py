import hashlib
import time
import json

class Block():
    def __init__(self, index, timestamp, data):
        self.index = index
        self.timestamp = timestamp
        self.data = data
        self.previousHash = 0
        self.nonce = 0
        self.hash = self.calHash()

    def calHash(self):
        return hashlib.sha256(str(self.index).encode() + str(self.data).encode() +
                            str(self.nonce).encode() + str(self.timestamp).encode() + str(self.previousHash).encode()).hexdigest()

    def mine(self, difficulty):
        ans = ["0"]*difficulty
        answer = "".join(ans)
        while(str(self.hash)[:difficulty] != answer):
            self.nonce += 1
            self.hash = self.calHash()

        print('nonce: ', self.nonce)
        print('data: ', self.data)
        print('prevhash: ', self.previousHash)
        print('hash: ', self.hash)

        return self.hash


class BlockChain:
    def __init__(self, ):
        self.chain = []
        self.difficulty = 5
        self.createGenesis()

    def createGenesis(self):
        self.chain.append(Block(0, time.time(), 'Genesis'))

    def addBlock(self, nBlock):
        nBlock.previousHash = self.chain[len(self.chain)-1].hash
        nBlock.hash = nBlock.mine(self.difficulty)
        nBlock.data = len(self.chain) + 1
        self.chain.append(nBlock)

    def getLatestBlock(self):
        return self.chain[len(self.chain)-1]

    def isValid(self):
        i = 1
        while(i<len(self.chain)):
            if(self.chain[i].hash != self.chain[i].calHash()):

                return False
            if(self.chain[i].previousHash != self.chain[i-1].hash):

                return False
            i += 1
        return True


base = BlockChain()

start_time = time.time();
for i in range(1,4):
    base.addBlock(Block(len(base.chain),time.time(), base.chain[-1].data))


########
#https://steemit.com/kr/@pangol/python-2-mining
# 이곳의 코드를 거의 따라쓴것이나 다름없다.
# 과제를 위해서 몇가지 변형만 줬을뿐이다. 
