from sys import argv
from src.validateInput import validateInputs
from constant.constants import INPUT_ERR,FILE_PATH_ERROR

def main():
    i=0
    if len(argv) != 2:
        raise Exception(FILE_PATH_ERROR)
    filePath = argv[1]
    f = open(filePath, 'r')
    lines = f.readlines()
    for line in lines:
        cmd=line.split()
        if not validateInputs(cmd):
            print(INPUT_ERR)
    
if __name__ == "__main__":
    main()