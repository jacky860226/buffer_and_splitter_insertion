class SubModule:
    def __init__(self, masterName, name):
        self.masterName = masterName
        self.name = name
        self.ioDict = dict()

    def print(self):
        print("SubModule:", self.masterName, self.name)
        for k, v in self.ioDict.items():
            print("   ", k, v)


class Module:
    def __init__(self, name):
        self.name = name
        self.input = set()
        self.output = set()
        self.wire = set()
        self.subModuleList = set()
        self.assign = list()

    def print(self):
        print("name:", self.name)
        print("input:", self.input)
        print("output:", self.output)
        print("wire:", self.wire)
        print("assign:", self.assign)
        for subModule in self.subModuleList:
            subModule.print()