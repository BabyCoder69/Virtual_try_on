

class MessageProcessor:
    def __init__(self):
        pass

    @staticmethod
    def process_msg(msg):
        # check if the msg contains an image


        if msg.lower() in ['p', 'person']:
            return 1
        elif msg.lower() in ['g', 'garment']:
            return 2
        else:
            return 3
