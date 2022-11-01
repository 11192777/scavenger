class SqlAdapterServer:
    apiSelector = [
        "Create Table"
    ]

    def __init__(self, type, content):
        self.type = type
        self.content = content

    def changeSetCreateTable(self):
        data = self.content
        data = data.replace("bigint(20)", "bigint")
        data = data.replace("bigint", "number(20)")
        data = data.replace('type="int"', 'type="number(11)"')
        data = data.replace("varchar", "nvarchar2")
        data = data.replace("timestamp", "date")
        data = data.replace('type="text"', 'type="varchar2(4000)"')
        data = data.replace('autoIncrement="${autoIncrement}" ', "")
        temp = ""
        for line in data.split("\n"):
            if "<createTable tableName" in line and "remarks=" in line:
                line = line.split("remarks=")[0] + ">"
            temp = temp + line + "\n"
        data = temp
        return data

    def execute(self):
        if self.type == self.apiSelector[0]:
            return self.changeSetCreateTable()
