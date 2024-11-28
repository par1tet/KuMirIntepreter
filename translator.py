from syntax. lexer. Lexer import Lexer
from syntax. lexer. Interpriter import Interpriter

sourceCode = []

with open('kumirCode.txt') as sourceCode:
    sourceCode = sourceCode.readlines()
    
lexer = Lexer(sourceCode)
translateCode = lexer.getTokens()

print(Interpriter.runCode(translateCode))
