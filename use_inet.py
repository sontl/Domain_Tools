import requests
from custom_exception import ApiError

class Inet:

    def __init__(self, domain, tld) :
        self.domain = domain
        self.tld = tld

    def check_status(self):
        # check using inet api
        resp = requests.get('https://inet.vn/api/order/checkavailable/' + self.domain + '.' + self.tld)
        if resp.status_code != 200:
            # This means something went wrong.
            raise ApiError('GET https://inet.vn/api/order/checkavailable/ {}'.format(resp.status_code))
        
        domain_data = resp.json()
        status = True
        if domain_data['status'] == "notavailable":
            status = False
        return status