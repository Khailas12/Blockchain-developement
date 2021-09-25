from flask import Flask, jsonify
from my_blockchain import Blockchain


app = Flask(__name__)
blockchain = Blockchain()


@app.route('/')
def home():
    return jsonify({'message': 'Welcome'})


@app.route('/mine_block', methods=['GET'])
def mine_block():
    previous_block = blockchain.print_previous_block()
    previous_proof = previous_block['proof']
    
    proof = blockchain.proof_of_work(previous_proof)
    previous_hash = blockchain.hash(previous_block)
    block = blockchain.create_block(proof, previous_hash)
    
    response = {
        'message': 'A block in Mined',
        'index': block['index'], 
        'timestamp': block['timestamp'],
        'proof': block['proof'],
        'previous_hash': block['previous_hash']
    }
    
    return jsonify(response), 200


@app.route('/get_chain', methods=['GET'])
def display_chain():
    response = {
        'chain': blockchain.chain,
        'length': len(blockchain.chain)
    }
    return jsonify(response), 200
    

@app.route('/valid', methods=['GET'])
def valid():
    valid = blockchain.chain_valid(blockchain.chain)
    
    if valid:
        response = {'message': 'The Blockchain is valid'}
    
    else:
        response = {'message': 'Sorry, the Blockchain is not valid'}
    
    return jsonify(response), 200



if __name__ == '__main__':
    app.run(debug=True, port=5000)