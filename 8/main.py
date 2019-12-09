WIDTH = 25
HEIGHT = 6
LAYER = WIDTH * HEIGHT

def main1():
    data = ""
    with open('input', 'r') as file:
        data = file.read()
    leastZeroes = 151
    zeroLayer = -1
    for i in range(len(data) // LAYER):
        zeroes = getLayer(data, i).count('0')
        if zeroes < leastZeroes:
            leastZeroes = zeroes
            zeroLayer = i
    zeroLayerData = getLayer(data, zeroLayer)
    return zeroLayerData.count('1') *zeroLayerData.count('2')

def main2():
    data = ""
    with open('input', 'r') as file:
        data = file.read()
    image = [None] * LAYER
    for i in range(LAYER):
        image[i] = getPixel(data, i)

    answerArr = []
    for i in range(HEIGHT):
        answerArr.append(''.join(image[WIDTH*i:WIDTH*(i+1)]))
    return '\n'.join(answerArr)

def getLayer(data, layerIndex):
    start = layerIndex * LAYER
    end = (layerIndex + 1) * LAYER
    return data[start:end]

def getPixel(data, n):
    # Reverse colors to make message readable in terminal
    if data[n] == '0':
        return " "
    elif data[n] == '1':
        return "#"
    else:
        return getPixel(data, n + LAYER)
    
print(main1())
print(main2())
