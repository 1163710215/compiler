import string

from MainLogic import Category
from MainLogic import FileAccess
from MainLogic import Parsing

_currentIndex = 0
_Tokens = []
_prog = ""


def readComments(prog):
    '''Read the comments of a program'''
    state = 0
    currentIndex, beginIndex, endIndex = (0, 0, 0)
    commentsIndexs = []
    for c in prog:
        if state == 0:
            if c == '/':
                beginIndex = currentIndex
                state = 1
            else:
                pass
        elif state == 1:
            if c == '*':
                state = 2
            elif c == '/':
                state = 4
            else:
                state = 0
        elif state == 2:
            if c == '*':
                state = 3
            else:
                pass
        elif state == 3:
            if c == '*':
                pass
            elif c == '/':
                endIndex = currentIndex
                commentsIndexs.append([beginIndex, endIndex])
                state = 0  # set 0 state
            else:
                state = 2
        elif state == 4:
            if c == '\n':
                endIndex = currentIndex
                commentsIndexs.append([beginIndex, endIndex])
                state = 0  # set 0 state
            else:
                pass
        currentIndex += 1
    if state == 4:
        endIndex = currentIndex
        commentsIndexs.append([beginIndex, endIndex])
    return commentsIndexs


def cutComments(prog, commentsIndexs):
    # cut the comments of the program prog
    num = len(commentsIndexs)
    if num == 0:
        return prog
    else:
        comments = []
        for i in range(num):
            comments.append(prog[commentsIndexs[i][0]:commentsIndexs[i][1] + 1])
        for item in comments:
            prog = prog.replace(item, "")
        return prog


def isLetter(param):
    if param in string.ascii_letters + '_':
        return True
    else:
        return False


def isDigit(param):
    if param in string.digits:
        return True
    else:
        return False


def getType(currentToken):
    table = Category.IdentifierTable

    if table.keys().__contains__(currentToken):
        return "" + currentToken, table.get(currentToken)
    else:
        return "id", 100


def scan(helper):
    # scan the program, and analysis it
    global _currentIndex, _Tokens, _prog
    while _currentIndex < len(_prog):
        currentToken = ''
        char = _prog[_currentIndex]

        try:
            while char == ' ' or char == '\n' or char == '\t':
                _currentIndex += 1
                # print(_prog[_currentIndex])
                char = _prog[_currentIndex]
            if isLetter(char):
                currentToken += char
                _currentIndex += 1
                while isLetter(_prog[_currentIndex]) or isDigit(_prog[_currentIndex]):
                    currentToken += _prog[_currentIndex]
                    _currentIndex += 1
                _Tokens += [(currentToken, getType(currentToken))]
            elif isDigit(char):
                while isDigit(_prog[_currentIndex]):
                    currentToken += _prog[_currentIndex]
                    _currentIndex += 1
                if _prog[_currentIndex] == '.':

                    currentToken += _prog[_currentIndex]
                    _currentIndex += 1
                    if isDigit(_prog[_currentIndex]):
                        while isDigit(_prog[_currentIndex]):
                            currentToken += _prog[_currentIndex]
                            _currentIndex += 1
                        _Tokens += [(currentToken, ("float", 99))]
                    else:
                        _Tokens += [(currentToken, ("Error", -1))]
                else:
                    _Tokens += [(currentToken, ("digit", 99))]
            elif char == '<':
                nextChar = _prog[_currentIndex + 1]
                if nextChar in '=<':
                    _currentIndex += 2
                    _Tokens += [(char + nextChar, getType(char + nextChar))]
                else:
                    _Tokens += [(char, getType(char))]
                    _currentIndex += 1
            elif char == '+':
                nextChar = _prog[_currentIndex + 1]
                if nextChar in '+':
                    _currentIndex += 2
                    _Tokens += [(char + nextChar, getType(char + nextChar))]
                else:
                    _Tokens += [(char, getType(char))]
                    _currentIndex += 1
            elif char == '-':
                nextChar = _prog[_currentIndex + 1]
                if nextChar in '-':
                    _currentIndex += 2
                    _Tokens += [(char + nextChar, getType(char + nextChar))]
                else:
                    _Tokens += [(char, getType(char))]
                    _currentIndex += 1
            elif char == '>':
                nextChar = _prog[_currentIndex + 1]
                if nextChar in '=>':
                    _currentIndex += 2
                    _Tokens += [(char + nextChar, getType(char + nextChar))]
                else:
                    _Tokens += [(char, getType(char))]
                    _currentIndex += 1
            elif char == '=':
                nextChar = _prog[_currentIndex + 1]
                if nextChar in '=':
                    _currentIndex += 2
                    _Tokens += [(char + nextChar, getType(char + nextChar))]
                else:
                    _Tokens += [(char, getType(char))]
                    _currentIndex += 1
            elif char == '!':
                nextChar = _prog[_currentIndex + 1]
                if nextChar in '=':
                    _currentIndex += 2
                    _Tokens += [(char + nextChar, getType(char + nextChar))]
                else:
                    _Tokens += [(char, getType(char))]
                    _currentIndex += 1
            elif char == '&':
                nextChar = _prog[_currentIndex + 1]
                if nextChar in '&':
                    _currentIndex += 2
                    _Tokens += [(char + nextChar, getType(char + nextChar))]
                else:
                    _Tokens += [(char, getType(char))]
                    _currentIndex += 1
            elif char == '|':
                nextChar = _prog[_currentIndex + 1]
                if nextChar in '|':
                    _currentIndex += 2
                    _Tokens += [(char + nextChar, getType(char + nextChar))]
                else:
                    _Tokens += [(char, getType(char))]
                    _currentIndex += 1
            elif char == '$':
                _Tokens += [('$', getType('$'))]
                return
            elif char in Category.operatorOrDelimiter:
                currentToken = char
                _Tokens += [(currentToken, getType(currentToken))]
                _currentIndex += 1
            else:
                # print(_currentIndex)
                # print(_prog[430:])
                _Tokens += [(char, ("Error", -1))]
                _currentIndex += 1

        except IndexError:
            if currentToken.strip() != "":
                _Tokens += [(currentToken.strip(), ("Error", -1))]
            return

            # print(helper.symbolTable)
        # if getType(currentToken)[0] == 'id':
        #     helper.setSymbolTable(currentToken, getType(currentToken)[0], getType(currentToken)[1])


def show(helper):
    for i in range(len(_Tokens)):
        # print(_Tokens)
        # print(type(_Tokens[i]))
        # if len(_Tokens[i]) == 2 and len(_Tokens[i][1]) == 2:
        helper.outPutToken(_Tokens[i][0], _Tokens[i][1][0], _Tokens[i][1][1])


if __name__ == '__main__':
    helper = FileAccess.FileHelper("txts/test.c", "txts/token.txt", "txts/symbol_table.txt", "txts/error.txt")
    prog = helper.readProg()
    # print(prog)

    comments = readComments(prog)
    _prog = cutComments(prog, comments)
    # print(_prog)

    if _currentIndex < len(_prog):
        scan(helper)
    show(helper)
    Parsing.parse(_Tokens)
    helper.closeFiles()
