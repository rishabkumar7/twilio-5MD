from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse, Message
from twilio.rest import Client
from dotenv import load_dotenv
import os

load_dotenv()

account_sid = os.getenv('TWILIO_ACCOUNT_SID')
auth_token = os.getenv('TWILIO_AUTH_TOKEN')

client = Client(account_sid, auth_token)
app = Flask(__name__)

@app.route('/sms', methods=['POST'])
def inbound_sms():
    response = MessagingResponse()
    response.message('Thanks for texting!'
                    'Wait to receive a phone call :)'
                    '- Drake')
    from_number = request.form['From']
    to_number = request.form['To']
    client.api.account.calls.create(to=from_number, from_=to_number,
                        url='https://thistle-toad-4490.twil.io/assets/Drake-HotlineBling.mp3')
    """
    call = client.calls.create(to=from_number,
          from_=to_number,
          url="https://thistle-toad-4490.twil.io/assets/Drake-HotlineBling.mp3")
    """
    return str(response)

if __name__ == '__main__':
    app.run(debug=True)