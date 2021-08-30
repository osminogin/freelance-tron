const TronWeb = require('tronweb');
const HttpProvider = TronWeb.providers.HttpProvider;
const dotenv = require('dotenv');

dotenv.config()

const fullNode = new HttpProvider(process.env.FULLNODE_URL);
const solidityNode = new HttpProvider(process.env.SOLIDITY_URL);
const eventServer = new HttpProvider(process.env.EVENT_SERVER);

console.log(`Connecting to ${fullNode} and ${solidityNode}`);

const tronWeb = new TronWeb(fullNode,solidityNode,eventServer);

console.log(tronWeb.trx);
console.log(tronWeb.transactionBuilder)
console.log(tronWeb.utils)

let newAccount = tronWeb.createAccount();
console.log(newAccount)