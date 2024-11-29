import re

tokenTypes = {
    "Operation": [r"\+",r"-",r"\*",r"/"],
    "Number": [r'\d+|\.'],
    "Space": [r'\s']
}

class Token:
    def __init__(self, type, value):
        self.type = type
        self.value = value

    def tokenize(stroke, position):
        for i in tokenTypes.keys():
            for k in tokenTypes[i]:
                finds = re.findall(k, stroke[position])

                if i == 'Space':
                    return {"step": 1, "token":None}

                if finds:
                    value = finds[0]
                    stepCounter = 1

                    if i == 'Number':
                        while (stepCounter + position) < len(stroke):
                            finds = re.findall(k, stroke[position + stepCounter])
                                               
                            if finds and re.findall(tokenTypes["Number"][0], finds[0]):
                                stepCounter+=1
                                value += finds[0]
                            else:
                                break

                    return {"step": stepCounter, "token":{"type": i, "value": value}}

        return {"step": 1, "token":None}
