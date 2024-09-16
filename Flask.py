from flask import Flask, render_template, request
from flask_socketio import SocketIO, emit
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from Tracking import Deposit
from flask_cors import CORS
app = Flask(__name__)
socketio = SocketIO(app)
CORS(app) 
socketio = SocketIO(app, cors_allowed_origins="*")
# Database setup
engine = create_engine('sqlite:///Database.db')
Session = sessionmaker(bind=engine)

@app.route('/')
def index():
    return render_template('index.html')

@socketio.on('get_transactions')
def handle_get_transactions(filters=None):
    session = Session()
    query = session.query(Deposit)

    # Apply filters if provided
    if filters:
        if 'block_number' in filters and filters['block_number']:
            query = query.filter(Deposit.block_number == filters['block_number'])
        if 'pubkey' in filters and filters['pubkey']:
            query = query.filter(Deposit.pubkey == filters['pubkey'])
        if 'hash' in filters and filters['hash']:
            query = query.filter(Deposit.hash == filters['hash'])

    deposits = query.all()
    session.close()

    result = [
        {
            'id': deposit.id,
            'block_number': deposit.block_number,
            'block_timestamp': deposit.block_timestamp,
            'fee': deposit.fee,
            'hash': deposit.hash,
            'pubkey': deposit.pubkey
        }
        for deposit in deposits
    ]
    emit('transactions_data', result)

# Optional: Emit new transactions for real-time updates
def emit_new_transaction(deposit):
    transaction = {
        'id': deposit.id,
        'block_number': deposit.block_number,
        'block_timestamp': deposit.block_timestamp,
        'fee': deposit.fee,
        'hash': deposit.hash,
        'pubkey': deposit.pubkey
    }
    socketio.emit('new_transaction', transaction)

if __name__ == '__main__':
    socketio.run(app, debug=True)
    