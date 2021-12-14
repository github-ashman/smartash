signed_txn = W3.eth.account.sign_transaction(tx_dict, private_key=privateKey)
#diagnostics
#print(signed_txn)
print("Deploying the Smart Contract")
result = W3.eth.sendRawTransaction(signed_txn.rawTransaction)
#diagnostics
#print(result)
#print('-----------------------------------')
tx_receipt = None#W3.eth.getTransactionReceipt(result)

count = 0
while tx_receipt is None and (count < 300):
  time.sleep(1)
  try:
    tx_receipt = W3.eth.getTransactionReceipt(result)
  except:
    print('.',end='')

if tx_receipt is None:
  print (" {'status': 'failed', 'error': 'timeout'} ")
#diagnostics
#print (tx_receipt)
print("\nContract address is:",tx_receipt.contractAddress)

greeter = W3.eth.contract(
  address=tx_receipt.contractAddress,
  abi=abi
)
print("Output from greet()")
print(greeter.functions.greet().call())
nonce = W3.eth.getTransactionCount(address1)
tx_dict = greeter.functions.setGreeting('Hello from 10584204').buildTransaction({
  'chainId': 3,
  'gas': 1400000,
  'gasPrice': w3.toWei('40', 'gwei'),
  'nonce': nonce,
  'from':address1
})

signed_txn = W3.eth.account.sign_transaction(tx_dict, private_key=privateKey)
result = W3.eth.sendRawTransaction(signed_txn.rawTransaction)
tx_receipt = None#W3.eth.getTransactionReceipt(result)

count = 0
while tx_receipt is None and (count < 300):
  time.sleep(1)
  try:
    tx_receipt = W3.eth.getTransactionReceipt(result)
  except:
    print('.',end='')

if tx_receipt is None:
  print (" {'status': 'failed', 'error': 'timeout'} ")

#tx_hash = greeter.functions.setGreeting('Hello from 10584204').transact({"from":account1.address})
#tx_receipt = w3.eth.waitForTransactionReceipt(tx_hash)
print("\nOutput from greet()")
print(greeter.functions.greet().call({"from":account1.address}))
#'Hello from 10584204'
