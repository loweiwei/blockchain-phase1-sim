
from models.transaction import UTXO, Transaction

def test_transaction_with_change(sender_utxo, send_amount, sender_address, recipient_address):
	tx2 = Transaction.create_with_change(sender_utxo, send_amount, sender_address, recipient_address)

	print("\n=== Test: Transaction with Change ===")
	print(f"Transaction ID: {tx2.txid}")
	for i, out in enumerate(tx2.outputs):
		print(f"Output #{i}: {out.amount} → {out.address}")

# Basic transaction (single input, single output)
input_utxo1 = UTXO(txid="abc123", index=0, amount=5.0, address="loweiwei")
output_utxo1 = UTXO(txid="", index=0, amount=4.0, address="Min_Fang")

tx1 = Transaction(inputs=[input_utxo1], outputs=[output_utxo1])

print("=== Basic Transaction ===")
print("Input UTXO:", input_utxo1.txid, input_utxo1.index, input_utxo1.amount, input_utxo1.address)
print("Output UTXO:", output_utxo1.amount, "->", output_utxo1.address)
print("Transaction ID (hash):", tx1.txid)

# Test: create transaction with change
test_transaction_with_change(input_utxo1, 1.0, "loweiwei", "Min_Fang")

