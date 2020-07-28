import sys
import Structure.Raw


class Parser:
    specialChars = "(),;.="

    def __removeUselessChar(self):
        while True:
            while self.lastChar == None or self.lastChar.isspace():
                self.lastChar = self.inputStream.read(1)
            if '/' not in self.lastChar:
                return
            self.lastChar = self.inputStream.read(1)
            if '/' in self.lastChar:
                while not '\n' in self.lastChar:
                    self.lastChar = self.inputStream.read(1)
            elif '*' in self.lastChar:
                while True:
                    while not '*' in self.lastChar:
                        self.lastChar = self.inputStream.read(1)
                    self.lastChar = self.inputStream.read(1)
                    if '/' in self.lastChar:
                        break

    def __getNextToken(self):
        self.__removeUselessChar()
        res = ""
        if self.lastChar in Parser.specialChars:
            res += self.lastChar
            self.lastChar = self.inputStream.read(1)
            return res
        while self.lastChar not in Parser.specialChars and not self.lastChar.isspace():
            res += self.lastChar
            self.lastChar = self.inputStream.read(1)
        return res

    def __readSubModuleIo(self):
        res = list()
        self.__getNextToken()  # '('
        while True:
            token = self.__getNextToken()
            if token == ',':
                continue
            if token == ')':
                break
            if token == '.':
                left = self.__getNextToken()
                self.__getNextToken()  # '('
                right = self.__getNextToken()
                self.__getNextToken()  # ')'
                res.append((left, right))
        self.__getNextToken()  # ';'
        return res

    def __readModule(self):
        rawModule = Structure.Raw.Module(self.__getNextToken())
        while ';' not in self.__getNextToken():
            pass
        while True:
            token = self.__getNextToken()
            if token == 'endmodule':
                break
            if token == 'wire' or token == 'input' or token == 'output':
                memberName = token
                token = self.__getNextToken()
                getattr(rawModule, memberName).add(token)
                self.__getNextToken()  # ';'
            elif token == 'assign':
                left = self.__getNextToken()
                self.__getNextToken()  # '='
                right = self.__getNextToken()
                self.__getNextToken()  # ';'
                rawModule.assign.append((left, right))
            else:
                rawSubModule = Structure.Raw.SubModule(
                    token, self.__getNextToken())
                rawSubModule.ioList = self.__readSubModuleIo()
                rawModule.subModuleList.append(rawSubModule)
        return rawModule

    def parse(self, inputStream=sys.stdin):
        self.inputStream = inputStream
        self.lastChar = None
        token = self.__getNextToken()
        if token == 'module':
            return self.__readModule()
        return None
