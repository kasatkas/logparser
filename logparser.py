import os,glob, argparse

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

parse = argparse.ArgumentParser(add_help=False)
parse.add_argument('-h', '--help', action='help', help='Print this help message and exit')
parse.add_argument('-p', '--path', help='Read file or folder')
parse.add_argument('-f', '--find', help='Search strings')
parse.add_argument('-o', '--output', default='result.txt', help=f'File to write. Default=result.txt')
argp = parse.parse_args()


def findString(fileName, str):
    with open(fileName, 'r') as file:
        inp = file.readlines()
        for i in progressBar(inp, prefix = 'Progress of ' + fileName, suffix = 'Complete', length = 50):
            if str in i:
                result.write(i + "\n")
        file.close()

path = argp.path
if os.path.isdir(path):
    result = open(argp.output, 'a+')
    for fileName in glob.glob(os.path.join(path, '*.log')):
            findString(fileName, argp.find)
    result.close()
elif os.path.isfile(path):
    result = open(argp.output, 'w+')
    findString(path, argp.find)
    result.close()
else: 
    print('Wrong arg!')
