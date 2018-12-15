import turtle

outputFile = open('Errolist.txt', 'w')
for item in dir(__builtins__):
    if 'Error' in item:
        print(item, file=outputFile)
        print(help(item), file=outputFile)
outputFile.close()


