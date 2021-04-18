import requests

class HostVN:

    def __init__(self, domain, tld) -> None:
        self.domain = domain
        self.tld = tld
    
    def check_status(self):
        # check using hostvn api
        resp = requests.get('https://hostvn.net/checkdomain.php?domain=' + self.domain + '.' + self.tld)
        if resp.status_code != 200:
            # This means something went wrong.
            raise ApiError('GET /tasks/ {}'.format(resp.status_code))
        #print(resp.json())
        return resp.json()['available']