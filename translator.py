from syntax. lexer. Lexer import Lexer
from syntax. lexer. Interpreter import Interpreter

sourceCode = [input('code >> ')]

#with open('kumirCode.txt') as sourceCode:
    #sourceCode = sourceCode.readlines()

lexer = Lexer(sourceCode)
interpreter = Interpreter(lexer)
translateCode = interpreter.runCode()

print(translateCode)
