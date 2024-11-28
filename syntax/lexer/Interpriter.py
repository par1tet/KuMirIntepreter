class Interpriter:
    def __init__(self):
        pass

    def runCode(tokenStream):
        i = 0
        while i < len(tokenStream):
            if tokenStream[i].type == 'Operation':
                match tokenStream[i].value:
                    case "+":
                        print(int(tokenStream[i-1].value) + int(tokenStream[i+1].value))
                        break
                    case "-":
                        print(int(tokenStream[i-1].value) - int(tokenStream[i+1].value))
                        break
                    case "/":
                        print(int(tokenStream[i-1].value) / int(tokenStream[i+1].value))
                        break
                    case "*":
                        print(int(tokenStream[i-1].value) * int(tokenStream[i+1].value))
                        break
                    
            else:
                i+=1
