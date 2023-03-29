from flask import Flask, request, redirect
from twilio.twiml.messaging_response import MessagingResponse

app = Flask(__name__)

@app.route("/sms", methods=['GET', 'POST'])
def sms():
  resp = MessagingResponse()
  msg = resp.message()
  resp.message('Hello, welcome this is your host Rishab here.')
  msg.media('https://cataas.com/cat')
  return str(resp), 200

  #Running
if __name__ == '__main__':
  app.run(debug=True)