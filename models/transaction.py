import hashlib
from typing import List

class UTXO:
    def __init__(self, txid: str, index: int, amount: float, address: str):
        self.txid = txid        #source id
        self.index = index      # the index of this trans
        self.amount = amount    # $$
        self.address = address  #ower address

class Transaction:
    def __init__(self, inputs: List[UTXO], outputs: List[UTXO]):
        self.inputs = inputs    # input.list(which utxo need to be spended)
        self.outputs = outputs  #output.list
        self.txid = self.calculate_txid()  #auto generate id

    def calculate_txid(self) -> str:
        tx_data = ""
        for i in self.inputs:
            tx_data += i.txid
            tx_data += str(i.index)   
        for o in self.outputs:
            tx_data += o.address
            tx_data += str(o.amount)
        return hashlib.sha256(tx_data.encode()).hexdigest()
    
    @classmethod
    def create_with_change(cls, sender_utxo, send_amount, sender_address, recipient_address):
        if send_amount > sender_utxo.amount:
            raise ValueError("transcation fail(amount aren't enough)")
    
        inputs = [sender_utxo]
        outputs = [UTXO(txid="", index=0, amount=send_amount, address=recipient_address)]

        change = sender_utxo.amount - send_amount
        if change > 0:
            outputs.append(UTXO(txid="", index=1, amount=change, address=sender_address))
        return cls(inputs=inputs, outputs=outputs)
