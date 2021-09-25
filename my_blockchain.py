import datetime
import json
import hashlib  # The terms “secure hash” and “message digest” are interchangeable. Included the FIPS secure hash algo



class Blockchain:
    # this creates the first block and sets the hash to '0'
    def __init__(self):
        self.chain = []
        self.create_block(proof=1, previous_hash='0')
        
        
    def create_block(self, proof, previous_hash):
        block = {
            "index": len(self.chain) + 1,
            "timestamp": str(datetime.datetime.now()),
            "proof": proof,
            "previous_hash": previous_hash
        }
        
        self.chain.append(block)    # adding further blocks following the prior created one     
        return block
    
    
    def print_previous_block(self):
        return self.chain[-1]   # displays the prior block
    
    
    # for the proof of work used to mine the block succesfully
    def proof_of_work(self, previous_proof):
        new_proof = 1
        check_proof = False

        while check_proof is False:
            hash_operation = hashlib.sha256(
                str(new_proof**2 - previous_proof**2).encode()).hexdigest() 
            #  Functions associated : encode() : Ckeonverts the string into bytes to be acceptable by hash function.
            # hexdigest() : Returns the encoded data in hexadecimal format.
            # What is SHA-256? The SHA (Secure Hash Algorithm) is one of a number of cryptographic hash functions. SHA256 algorithm generates an almost-unique, fixed size 256-bit (32-byte) hash. Hash is so called a one way function.
            
    
    def hash(self, block):
        encoded_block = json.dumps(block, sort_keys=True).encode()
        return hashlib.sha256(encoded_block).hexdigest()
    
    def chain_valid(self, chain):
        previous_block = chain[0]
        block_index = 1
        
        while block_index < len(chain):
            block = chain[block_index]
            
            if block['previous_hash'] != self.hash(previous_block):
                return False
            
            previous_block = previous_block['proof']
            proof = block['proof']
            hash_operation = hashlib.sha256(
                str(proof**2 - previous_block**2).encode()
            ).hexdigest()
        
            if hash_operation[:4] != '00000':
                return False
            
            previous_block = block
            block_index += 1