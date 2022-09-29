import requests



class HermesServer:
    def __init__(self, env):
        self.comapnies = None
        self.headers = {
            'Authorization': env["token"],
            'Content-Type': 'application/json',
            'key': 'archive-fields-manage'
        }
        self.env_url = env["hermes_url"]

    def list_companies(self):
        if self.comapnies is not None:
            return self.comapnies
        url = '/api/company/controlled/by/term?roleType=true&page=0&size=100&name='
        self.comapnies = requests.get(url=self.env_url + url, headers=self.headers).json()
        return self.comapnies