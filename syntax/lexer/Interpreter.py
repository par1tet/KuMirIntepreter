from syntax. lexer. Token import Token

class Interpreter:
    def __init__(self, lexer):
        self.currentTokenNumber = 0
        self.lexer = lexer

    def error(self,text):
        raise Exception(text)

    def nextToken(self):
        self.currentTokenNumber += 1

    def eatToken(self,tokenType):
        if self.currentTokenNumber > len(self.lexer.tokenStream)-1:
            return Token('EOF', None)

        token = self.lexer.tokenStream[self.currentTokenNumber]

        if tokenType == token.type:
            self.nextToken()
            return token
        else:
            self.error('Syntax error')

    def factor(self):
        token = self.eatToken('Number')
        return float(token.value)

    def term(self):
        result = self.factor()

        if result == None: return result

        while self.currentTokenNumber < len(self.lexer.tokenStream) and self.lexer.tokenStream[self.currentTokenNumber].value in ('*', '/'):
            match self.lexer.tokenStream[self.currentTokenNumber].value:
                case "*":
                    self.eatToken('Operation')

                    termResult = self.factor()

                    if termResult == None: return result
                    result *= (termResult)
                    break
                case "/":
                    self.eatToken('Operation')
                    termResult = self.factor()

                    if termResult == None: return result

                    result /= (termResult)
                    break

        return result

    def runCode(self):
        self.lexer.getTokens()
        result = self.term()

        while self.currentTokenNumber < len(self.lexer.tokenStream) and self.lexer.tokenStream[self.currentTokenNumber].value in ('+', '-'):
            if self.lexer.tokenStream[self.currentTokenNumber].value == '+':
                    self.eatToken('Operation')
                    termResult = self.term()

                    if termResult == None: return result

                    result += termResult
            elif self.lexer.tokenStream[self.currentTokenNumber].value == '-':
                    self.eatToken('Operation')
                    termResult = self.term()

                    if termResult == None: return result
                    
                    result -= termResult

        return result
