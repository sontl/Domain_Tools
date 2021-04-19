import requests
from custom_exception import ApiError
class NhanHoa:

    def __init__(self, domain, tld) -> None:
        self.domain = domain
        self.tld = '.' + tld 

    def check_status(self):
        # check using nhanhoa api
        resp = requests.post('https://nhanhoa.com/service/', data=dict(view='check_whois', site='whois', 
            domain=self.domain, ext=self.tld))
        if resp.status_code != 200:
            # This means something went wrong.
            raise ApiError('POST https://nhanhoa.com/service/ {}'.format(resp.status_code))
        else:
            if (resp.json()['status'] == 1):
                return False
            else:
                return True