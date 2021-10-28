def progressBar(iterable, prefix = '', suffix = '', decimals = 1, length = 100, fill = '█', printEnd = "\r"):
    total = len(iterable)
    def printProgressBar (iteration):
        percent = ("{0:." + str(decimals) + "f}").format(100 * (iteration / float(total)))
        filledLength = int(length * iteration // total)
        bar = fill * filledLength + '-' * (length - filledLength)
        print(f'\r{prefix} |{bar}| {percent}% {suffix}', end = printEnd)
    printProgressBar(0)
    for i, item in enumerate(iterable):
        yield item
        printProgressBar(i + 1)
    print()

import sys,os,glob
path = sys.argv[1]
stringToFind = sys.argv[2]
resultFile =  "E:/result.log"

def findString(file, str, mode):
    result = open(resultFile, mode)
    inp = file.readlines()
    for i in progressBar(inp, prefix = 'Progress of ' + file.name, suffix = 'Complete', length = 50):
        if str in i:
            result.write(i + "\n")
    result.close()
    
if os.path.isdir(path):
    for fileName in glob.glob(os.path.join(path, '*.log')):
        with open(fileName, 'r') as f:
            findString(f, stringToFind, 'a+')
            f.close()
elif os.path.isfile(path):
    with open(path, 'r') as f:
        findString(f, stringToFind, 'w+')
        f.close()
else: 
    print('Wrong arg!')
