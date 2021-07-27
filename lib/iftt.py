import urequests
import keys
import sys

class iftt:
    """
    Credits:
    By Erik Karlsson
    Inspired by webrequests.py by zerox13.
    """
    def send_request(event):
        """
        input: event that you set up in IFTT.
        Use key in keys.py file.
        """
        try:
            url = "https://maker.ifttt.com/trigger/{}/with/key/{}".format(event, keys.iftt_token)
            req = urequests.post(url) #send request to iftt
            print(req.text)
        except: 
            #TODO: write better exceptions
            print("Unexpected error:", sys.exc_info()[0])
            raise
