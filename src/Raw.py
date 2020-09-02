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
        self.virtualKey = {"1'b0", "1'b1", "JinkelaOut"}

    def print(self):
        print("name:", self.name)
        print("input:", self.input)
        print("output:", self.output)
        print("wire:", self.wire)
        print("assign:", self.assign)
        for subModule in self.subModuleList:
            subModule.print()
    
    def verilog_output(self, fout):
        fout.write("module %s("%(self.name))
        first = False
        for w in self.input:
            if w in self.virtualKey:
                continue
            if first:
                fout.write(',')
            first = True
            fout.write(w)
        fout.write(");\n")
        for w in self.wire:
            if w in self.virtualKey:
                continue
            if w in self.input:
                continue
            if w in self.output:
                continue
            fout.write("    wire %s;\n"%(w))
        for w in self.input:
            if w in self.virtualKey:
                continue
            fout.write("    input %s;\n"%(w))
        for w in self.output:
            if w in self.virtualKey:
                continue
            fout.write("    output %s;\n"%(w))
        fout.write("\n")
        for sm in self.subModuleList:
            if sm.masterName in self.virtualKey:
                continue
            fout.write("    %s %s (\n"%(sm.masterName, sm.name))
            outNum = len(sm.ioDict)
            for k, v in sm.ioDict.items():
                outNum -= 1
                fout.write("        .%s(%s)"%(k, v))
                if outNum == 0:
                    fout.write("\n")
                else:
                    fout.write(",\n")
            fout.write("    );\n\n")

        fout.write("endmodule\n")

