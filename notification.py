
import vonage
import pathlib

class Notification:

    def __init__(self, domain, tld) -> None:
        self.domain = domain
        self.tld = tld
    
    current_directory = str(pathlib.Path(__file__).parent.absolute()) 

    # class variables
    client = vonage.Client(
        application_id="6d0de9bd-784e-439c-aad5-4ef50da38e31",
        private_key= current_directory + "/private.key",
    )

    def call(self):
        voice = vonage.Voice(self.client)
        text = 'Hi there, domain {}.{} is available now.'.format(self.domain, self.tld)
        response = voice.create_call({
            'to': [{'type': 'phone', 'number': "6587837006"}],
            'from': {'type': 'phone', 'number': "6587837006"},
            'ncco': [{'action': 'talk', 'text': text}]
        })
        if (response["status"] == "started"):
            print("| Reported to Son dai ka ^o^ ")
        else :
            print("| Could not contact Son dai ka @.@")