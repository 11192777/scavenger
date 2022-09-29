class ArchiveResult:

    def __init__(self, response):
        self.response = response

    def data(self, key=None):
        if key is not None:
            return self.response["result"][key]
        else:
            return self.response["result"]

    def status_code(self):
        return self.response["statusCode"]

    def message(self):
        return self.response["message"]

