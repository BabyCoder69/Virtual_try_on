from twilio.rest import Client


class WhatsappUtils:
    def __init__(self):
        account_sid = ''
        auth_token = ''
        self.client = Client(account_sid, auth_token)

    def send_whatsapp_message(self, phone_number, message):
        self.client.messages.create(
            from_='whatsapp:+14xxx',
            body=message,
            to="whatsapp:" + phone_number
        )

    def send_whatsapp_media(self, phone_number, media_url):
        self.client.messages.create(
            from_='whatsapp:+14xx',
            to="whatsapp:" + phone_number,
            media_url=[media_url]
        )
