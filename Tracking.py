import time
from setup import provider
from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
w3=provider()
Beacon_contract='0x00000000219ab540356cBB839Cbe05303d7705Fa'
Base = declarative_base()

class Deposit(Base):
    __tablename__ = 'deposits'
    id = Column(Integer, primary_key=True)
    block_number = Column(Integer)
    block_timestamp = Column(Integer)
    fee = Column(Integer)
    hash = Column(String(66))
    pubkey = Column(String(42))
def monitor_deposits(w3):
    while True:
        latest_block_number = w3.eth.block_number
        deposit_data= fetch_block_transactions(w3, Beacon_contract, latest_block_number)
        process_deposit_data(deposit_data, latest_block_number)
        time.sleep(60)
def fetch_block_transactions(w3, contract_addr, block_number):
    block = w3.eth.get_block(block_number, full_transactions=True)
    transactions = [tx for tx in block['transactions'] if tx['to'] == contract_addr]
    return transactions,block
def process_deposit_data(deposit_data,latest_block_number):
    block = w3.eth.get_block(latest_block_number)
    block_timestamp = block['timestamp'] 
    for tx in deposit_data:
        sender_addr = tx['from']
        amount = tx['value']
        save_deposit_data(sender_addr, amount,  block_timestamp, latest_block_number,tx)
def save_deposit_data(sender_addr, amount, timestamp, latest_block_number, deposit_data):
    engine = create_engine('sqlite:///Database.db')
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()

    # Add a single deposit entry
    deposit = Deposit(
        block_number=latest_block_number,
        block_timestamp=timestamp,
        fee=deposit_data['gas'],
        hash=deposit_data['hash'],
        pubkey=sender_addr
    )
    session.add(deposit)
    
    session.commit()
    session.close()