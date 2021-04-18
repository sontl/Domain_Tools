import requests

class Digistar:
    
    def __init__(self, domain, tld) -> None:
        self.domain = domain
        self.tld = tld

    def check_status(self):
        # check using digistar api
        form_data = {"domain" : self.domain, "tld" : self.tld}
        resp = requests.post('https://manage.digistar.vn/ds-ajax/check-domain.php', form_data)
        if resp.status_code != 200:
            # This means something went wrong.
            raise ApiError('GET /tasks/ {}'.format(resp.status_code))
        else:
            status = resp.json()['status']
            if (status == "unavailable"):
                return False
            else  :
                return True