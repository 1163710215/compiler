class FileHelper(object):
    def __init__(self, progPath, tokenPath, symbolTablePath, errorPath):
        self.progPath = progPath
        self.tokenPath = tokenPath
        self.symbolTablePath = symbolTablePath
        self.errorPath = errorPath

        self.tokenFp = open(self.tokenPath, "w", encoding='UTF-8')
        self.symbolTableFp = open(self.symbolTablePath, "w", encoding='UTF-8')
        self.errorFp = open(self.errorPath, "w", encoding='UTF-8')

        self.symbolTable = {}  # .fromkeys(Category.KeyWordsTable)  # initialize symbol table
        print(self.symbolTable)

    def readProg(self):
        '''read the program into the RAM'''
        fp = open(self.progPath, "r+", encoding='UTF-8')
        prog = ""
        for eachLine in fp.readlines():
            # print eachLine
            prog = "{}{}".format(prog, eachLine)
        fp.close()
        return prog

    def outPutToken(self, tokenSelf, tokenInner, tokenNo):
        '''output token into a file'''
        if tokenNo == -1:
            self.errorFp.write("<{1:^5},{0:^5},{2:^5}>\n".format(tokenSelf, tokenInner, tokenNo))
        else:
            self.tokenFp.write("<{1:^5},{0:^5},{2:^5}>\n".format(tokenSelf, tokenInner, tokenNo))
        print("<{1:^5},{0:^5},{2:^5}>".format(tokenSelf, tokenInner, tokenNo))

    # def setSymbolTable(self, tokenSelf, tokenInner, tokenNo):
    #     '''output symbol into symbol table'''
    #     if not self.symbolTable.keys().__contains__(tokenSelf):
    #         self.symbolTable[tokenSelf] = tokenNo
    #
    # def writeSymbolToFile(self):
    #     for k in self.symbolTable:
    #         self.symbolTableFp.write("{:^5}\t{:^5}\n".format(k, self.symbolTable[k]))

    def closeFiles(self):
        '''close token Files'''
        # self.writeSymbolToFile()
        if self.tokenFp != None:
            self.tokenFp.close()
        if self.symbolTableFp != None:
            self.symbolTableFp.close()
