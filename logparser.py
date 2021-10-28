import sys,os,glob
arg = sys.argv[1]

if os.path.isdir(arg):
    for filename in glob.glob(os.path.join(arg, '*.log')):
        with open(filename, 'r') as f:
            #do smth
            f.close()
elif os.path.isfile(arg):
    with open(arg, 'r') as f:
        #do smth
        f.close()
else: 
    print('Wrong arg!')

