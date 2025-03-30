from models.transaction import UTXO, Transaction

input_utxo = UTXO(txid="abc123", index=0, amount=5.0, address="loweiwei")
output_utxo = UTXO(txid="", index=0, amount=5.0, address="Min_Fang")

tx = Transaction(inputs=[input_utxo], outputs=[output_utxo])

print("=== transaction  ===")
print("input UTXO：", input_utxo.txid, input_utxo.index, input_utxo.amount, input_utxo.address)
print("output UTXO：", output_utxo.amount, "->", output_utxo.address)
print("transaction ID（hash）：", tx.txid)


