import logging
logging.basicConfig(filename='deposit_tracker.log', level=logging.INFO)
def handle_error(error):
    logging.error(error)
    send_alert(error)
def send_alert(error):
    pass
