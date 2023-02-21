
class StrUtilServer:
    apiSelector = [
        "Java str to py format",
        "Java class to JSON"
    ]

    def __init__(self, type, content):
        self.type = type
        self.content = content

    def execute(self):
        if self.type == self.apiSelector[0]:
            return self.javaStrToPyFormat()
        elif self.type == self.apiSelector[1]:
            return self.javaClassToJSON()

    def javaStrToPyFormat(self):
        data = str(self.content)
        data = data.replace("{", "{{")
        data = data.replace("}", "}}")
        return data

    def javaClassToJSON(self):
        data = str(self.content)


