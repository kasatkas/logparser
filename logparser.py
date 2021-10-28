import sys,os,glob
path = sys.argv[1]
stringToFind = sys.argv[2]
resultFile =  "E:/result.txt"

def findString(file, str, mode):
    result = open(resultFile, mode)
    inp = file.readlines()
    for i in iter(inp):
        if str in i:
            #print(i)
            result.write(i + "\n")

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

