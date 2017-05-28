from twilio.rest import TwilioRestClient

account_sid = "AC15bdd975d1b83d435a823eeb74b2d99e" # Your Account SID from www.twilio.com/console
auth_token  = "79b2b1e3ee955e4c6e33372b2d7d85e4"  # Your Auth Token from www.twilio.com/console

client = TwilioRestClient(account_sid, auth_token)

message = client.messages.create(body="yoo.i am vishnu",
    to="+919944597594",    # Replace with your phone number
    from_="+17603003388") # Replace with your Twilio number

print(message.sid)
