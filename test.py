import unittest
from Tracking import  process_deposit_data,Deposit
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import csv
class TestSaveDepositData(unittest.TestCase):
  def setUp(self):
        # Clear the database before each test
        engine = create_engine('sqlite:///Database.db')
        Session = sessionmaker(bind=engine)
        session = Session()
        session.query(Deposit).delete()  # Clear all records
        session.commit()
        session.close()

  def test_save_deposit_data_multiple_deposits(self):
      latest_block_number = 12345678
      deposit_data_list = [
      {'gas': 27532, 'hash': '0x5e9f6c9a0b23c7e1b1c9d8f3a1e8c5d6f3a2b1c8', 'pubkey': '0xa1b2c3d4e5f67890123456789abcdef01234567', 'from': '0x1234567890abcdef1234567890abcdef12345678', 'value': 478, 'timestamp': 1673457102},
      {'gas': 31421, 'hash': '0x8f9d4e5b0c6a2b3c7e9f0d1a2b3c4d5e6f7a8b9c', 'pubkey': '0x234567890abcdef1234567890abcdef12345678', 'from': '0xabcdef1234567890abcdef1234567890abcdef12', 'value': 652, 'timestamp': 1687348204},
      {'gas': 28910, 'hash': '0x2c7e8d9f0b1a234c5d678e9f0a1b2c3d4e5f6789', 'pubkey': '0x3456789012abcdef1234567890abcdef12345678', 'from': '0xabcdefabcdefabcdefabcdefabcdefabcdefabcdef', 'value': 342, 'timestamp': 1667839700},
      {'gas': 30312, 'hash': '0x7d9a0b1c2e3f4567890abcdeffedcba98765432', 'pubkey': '0x4567890123abcdef1234567890abcdef12345678', 'from': '0xabcdefabcdefabcdefabcdefabcdefabcdefabcdef', 'value': 743, 'timestamp': 1657489209},
      {'gas': 27845, 'hash': '0x1a2b3c4d5e6f7890abcdef1234567890abcdef12', 'pubkey': '0x5678901234abcdef1234567890abcdef12345678', 'from': '0x1234567890abcdef1234567890abcdef12345678', 'value': 927, 'timestamp': 1694856011},
      {'gas': 29534, 'hash': '0x4f5e6d7c8b9a0c1d2e3f4a5b6c7d8e9f0a1b2c3d', 'pubkey': '0x6789012345abcdef1234567890abcdef12345678', 'from': '0xabcdef1234567890abcdef1234567890abcdef12', 'value': 612, 'timestamp': 1673967823},
      {'gas': 30672, 'hash': '0x6d7e8f9a0b1c2d3e4f5a6b7c8d9e0f1234567890', 'pubkey': '0x7890123456abcdef1234567890abcdef12345678', 'from': '0xabcdefabcdefabcdefabcdefabcdefabcdefabcdef', 'value': 831, 'timestamp': 1656402824},
      {'gas': 28430, 'hash': '0x7a8b9c0d1e2f34567890abcdef1234567890abc', 'pubkey': '0x8901234567abcdef1234567890abcdef12345678', 'from': '0xabcdef1234567890abcdef1234567890abcdef12', 'value': 509, 'timestamp': 1687345728},
      {'gas': 32214, 'hash': '0x2b3c4d5e6f7890abcdef1234567890abcdef1234', 'pubkey': '0x9012345678abcdef1234567890abcdef12345678', 'from': '0xabcdefabcdefabcdefabcdefabcdefabcdefabcdef', 'value': 414, 'timestamp': 1667896900},
      {'gas': 29051, 'hash': '0x5f6e7d8c9a0b1c2d3e4f5a67890bcdef12345678', 'pubkey': '0x0123456789abcdef1234567890abcdef12345678', 'from': '0xabcdefabcdefabcdefabcdefabcdefabcdefabcdef', 'value': 734, 'timestamp': 1694810200},
      {'gas': 30792, 'hash': '0x9a8b7c6d5e4f0c1d2e3f4567890abcdef123456', 'pubkey': '0x1234567890abcdef1234567890abcdef12345678', 'from': '0xabcdef1234567890abcdef1234567890abcdef12', 'value': 643, 'timestamp': 1673968292},
      {'gas': 29673, 'hash': '0xc7d8e9f0a1b2c3d4e5f67890123456789abcdef', 'pubkey': '0x234567890abcdef1234567890abcdef12345678', 'from': '0xabcdefabcdefabcdefabcdefabcdefabcdefabcdef', 'value': 562, 'timestamp': 1687349343},
      {'gas': 31045, 'hash': '0x1b2c3d4e5f67890abcdef1234567890abcdef12', 'pubkey': '0x3456789012abcdef1234567890abcdef12345678', 'from': '0xabcdef1234567890abcdef1234567890abcdef12', 'value': 752, 'timestamp': 1667839827},
      {'gas': 28356, 'hash': '0x2e3f4a5b6c7d8e9f0a1b2c3d4567890abcdef12', 'pubkey': '0x4567890123abcdef1234567890abcdef12345678', 'from': '0xabcdefabcdefabcdefabcdefabcdefabcdefabcdef', 'value': 417, 'timestamp': 1657489202},
      {'gas': 31720, 'hash': '0x3d4e5f6a7b8c9d0e1f234567890abcdef123456', 'pubkey': '0x5678901234abcdef1234567890abcdef12345678', 'from': '0xabcdef1234567890abcdef1234567890abcdef12', 'value': 684, 'timestamp': 1694810512},
      {'gas': 28594, 'hash': '0x4c5d6e7f8a9b0c1d2e3f4567890abcdef123456', 'pubkey': '0x6789012345abcdef1234567890abcdef12345678', 'from': '0xabcdefabcdefabcdefabcdefabcdefabcdefabcdef', 'value': 731, 'timestamp': 1673968342},
      {'gas': 29782, 'hash': '0x5e6f7d8c9a0b1c2d3e4f567890abcdef1234567', 'pubkey': '0x7890123456abcdef1234567890abcdef12345678', 'from': '0xabcdef1234567890abcdef1234567890abcdef12', 'value': 529, 'timestamp': 1687345624},
      {'gas': 31091, 'hash': '0x6a7b8c9d0e1f234567890abcdef123456789012', 'pubkey': '0x8901234567abcdef1234567890abcdef12345678', 'from': '0xabcdefabcdefabcdefabcdefabcdefabcdefabcdef', 'value': 682, 'timestamp': 1667895832},
      {'gas': 28439, 'hash': '0x7c8d9e0f1a2b3c4d5e67890123456789abcdef0', 'pubkey': '0x9012345678abcdef1234567890abcdef12345678', 'from': '0xabcdef1234567890abcdef1234567890abcdef12', 'value': 489, 'timestamp': 1694856165},
      {'gas': 29170, 'hash': '0x8e9f0a1b2c3d4567890abcdef1234567890abcd', 'pubkey': '0x0123456789abcdef1234567890abcdef12345678', 'from': '0xabcdefabcdefabcdefabcdefabcdefabcdefabcdef', 'value': 735, 'timestamp': 1673967411},
      {'gas': 30358, 'hash': '0x9d0a1b2c3d4e5f67890abcdef1234567890abcd', 'pubkey': '0x1234567890abcdef1234567890abcdef12345678', 'from': '0xabcdef1234567890abcdef1234567890abcdef12', 'value': 624, 'timestamp': 1687349200} 

      ]
      process_deposit_data(deposit_data_list, latest_block_number)


      engine = create_engine('sqlite:///Database.db')
      Session = sessionmaker(bind=engine)
      session = Session()
      deposits = session.query(Deposit).all()
      self.assertEqual(len(deposits), len(deposit_data_list))
      csv_file = 'deposits.csv'
    
      with open(csv_file, mode='w', newline='') as file:
        writer = csv.writer(file)
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
      print('Success')
      session.close()

