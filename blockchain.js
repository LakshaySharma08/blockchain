const SHA256 = require("crypto-js/sha256");

class Block {
  constructor(index, timestamp, data, previousHash = "") {
    this.index = index;
    this.timestamp = timestamp;
    this.data = data;
    this.previousHash = previousHash;
    this.hash = this.calculateHash();
  }

  calculateHash() {
    return SHA256(
      this.index +
        this.timestamp +
        JSON.stringify(this.data) +
        this.previousHash
    ).toString();
  }
}

class Blockchain {
  constructor() {
    this.chain = [this.createGenesis()];
  }

  createGenesis() {
    return new Block(0, "05-10-2021", "Genesis Block", "0");
  }

  getLastBlock() {
    return this.chain[this.chain.length - 1];
  }

  addBlock(newBlock) {
    newBlock.previousHash = this.getLastBlock().hash;
    newBlock.hash = newBlock.calculateHash();
    this.chain.push(newBlock);
  }
  verifyChain() {
    for (let i = 1; i < this.chain.length; ++i) {
      if (this.chain[i].hash !== this.chain[i].calculateHash()) return false; // Check if the calculate hash is equal to present.
      if (this.chain[i - 1].hash !== this.chain[i].previousHash) return false;
    }
    return true;
  }

  print() {
    console.log(JSON.stringify(this, null, 4));
  }
}

let tkCoin = new Blockchain();

tkCoin.addBlock(new Block(1, "06-10-2021", { name: "Tanmay  " }));
tkCoin.addBlock(new Block(1, "07-10-2021", { name: "Person 1" }));
tkCoin.addBlock(new Block(1, "08-10-2021", { name: "Person 2" }));

console.log(tkCoin.verifyChain());
tkCoin.chain[2].data = { name: "Hacker trying to change the chain data" };

console.log(tkCoin.verifyChain());
// tkCoin.print()