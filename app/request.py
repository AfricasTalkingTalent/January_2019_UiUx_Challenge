
# import package
import africastalking


# use your sandbox app API key for development in the test environment
username = "sandbox"
api_key = 'ba0f3dd244ccd7943680239340c2ae76fd46df17be3c0a8d5cb130dd264a80c9'
africastalking.initialize(username, api_key)

# Initialize a service e.g. SMS
sms = africastalking.SMS


def send_sms(msg, number):
    response = sms.send(msg, [number])

    return (response)
