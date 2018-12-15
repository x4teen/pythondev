with open('sample.txt', 'a') as results_file:
    for num in range(1, 13):
        print("{0:3} times 2 is {1:2}".format(num, num*2),
              file=results_file)

