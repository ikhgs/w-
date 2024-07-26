import os
from twilio.rest import Client

TWILIO_ACCOUNT_SID = 'ACb1e27aa70ecc3659544b58a8a3450afa'
TWILIO_AUTH_TOKEN = 'Tb8064608c257774ee16e0f230d0d81fd'
FROM_PHONE_NUMBER = '+14155238886'

client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)

def send_message(to: str, message: str) -> None:
    '''
    Send message to a Telegram user.

    Parameters:
        - to(str): recipient phone number in this format: whatsapp:+919558515995
        - message(str): text message to send

    Returns:
        - None
    '''

    _ = client.messages.create(
        from_=FROM_PHONE_NUMBER,
        body=message,
        to=to
    )

# Exemple d'utilisation
send_message('whatsapp:+14155238886', 'Hello from Twilio!')

