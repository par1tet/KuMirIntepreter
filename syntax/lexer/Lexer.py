from syntax. lexer. Token import Token

class Lexer:
    def __init__(self, sourceCode):
        self.sourceCode = sourceCode
        self.tokens = []
        self.numberString = 0
        self.numberCharacter = 0

    def nextToken(self):
        tokenize = Token.tokenize(self.sourceCode[self.numberString], self.numberCharacter)

        self.numberCharacter+=tokenize["step"]

        if tokenize['token']: self.tokens.append(Token(tokenize["token"]['type'], tokenize["token"]['value']))

    def getTokens(self):

        while len(self.sourceCode) > self.numberString:

            while len(self.sourceCode[self.numberString]) > self.numberCharacter:
                self.nextToken()

            print()
            self.numberString += 1
            self.numberCharacter = 0

        return self.tokens
