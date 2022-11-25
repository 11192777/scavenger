
class StrUtilServer:
    apiSelector = [
        "Java str to py format",
    ]

    def __init__(self, type, content):
        self.type = type
        self.content = content

    def execute(self):
        if self.type == self.apiSelector[0]:
            return self.javaStrToPyFormat()

    def javaStrToPyFormat(self):
        data = str(self.content)
        data = data.replace("{", "{{")
        data = data.replace("}", "}}")
        return data

