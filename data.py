from Tracking import  process_deposit_data,Deposit
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import csv
def test_save_deposit_data_multiple_deposits():
        latest_block_number = 12345678
        deposit_data_list = [
        {'gas': 27532, 'hash': '0x5e9f6c9a0b23c7e1b1c9d8f3a1e8c5d6f3a2b1c8', 'pubkey': '0xa1b2c3d4e5f67890123456789abcdef01234567', 'from': '0x1234567890abcdef1234567890abcdef12345678', 'value': 478, 'timestamp': 1673457102},
        {'gas': 31421, 'hash': '0x8f9d4e5b0c6a2b3c7e9f0d1a2b3c4d5e6f7a8b9c', 'pubkey': '0x234567890abcdef1234567890abcdef12345678', 'from': '0xabcdef1234567890abcdef1234567890abcdef12', 'value': 652, 'timestamp': 1687348204},
        {'gas': 28910, 'hash': '0x2c7e8d9f0b1a234c5d678e9f0a1b2c3d4e5f6789', 'pubkey': '0x3456789012abcdef1234567890abcdef12345678', 'from': '0xabcdefabcdefabcdefabcdefabcdefabcdefabcdef', 'value': 342, 'timestamp': 1667839700},
        {'gas': 30312, 'hash': '0x7d9a0b1c2e3f4567890abcdeffedcba98765432', 'pubkey': '0x4567890123abcdef1234567890abcdef12345678', 'from': '0xabcdefabcdefabcdefabcdefabcdefabcdefabcdef', 'value': 743, 'timestamp': 1657489209},
        {'gas': 27845, 'hash': '0x1a2b3c4d5e6f7890abcdef1234567890abcdef12', 'pubkey': '0x5678901234abcdef1234567890abcdef12345678', 'from': '0x1234567890abcdef1234567890abcdef12345678', 'value': 927, 'timestamp': 1694856011},
        ]
        
        process_deposit_data(deposit_data_list, latest_block_number)


        engine = create_engine('sqlite:///Database.db')
        Session = sessionmaker(bind=engine)
        session = Session()
        deposits = session.query(Deposit).all()
        print('deposited')
        csv_file='deposits.csv'
        with open(csv_file,mode='w',newlime='') as file:
            writer= csv.writer(file)
            writer.writerow(['ID', 'Block Number', 'Timestamp', 'Fee', 'Hash', 'Public Key'])
            for deposit in deposits:
                writer.writerow([
                    deposit.id,
                    deposit.block_number,
                    deposit.block_timestamp,
                    deposit.fee,
                    deposit.hash,
                    deposit.pubkey,
                ])
        print('Saved')
        session.close()
        
