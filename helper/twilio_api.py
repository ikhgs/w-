import os


from twilio.rest import Client
from dotenv import load_dotenv
load_dotenv()


account_sid = os.getenv('ACb1e27aa70ecc3659544b58a8a3450afa')
auth_token = os.getenv('Tb8064608c257774ee16e0f230d0d81fd')
client = Client(account_sid, auth_token)


def send_message(to: str, message: str) -> None:
    '''
    Send message to a Telegram user.

    Parameters:
        - to(str): sender whatsapp number in this whatsapp:+919558515995 form
        - message(str): text message to send

    Returns:
        - None
    '''

    _ = client.messages.create(
        from_=os.getenv('FROM'),
        body=message,
        to=to
    )
