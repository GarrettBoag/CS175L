#Garrett Boag
#3/21/24
#CS 175L 01


def main():

    total = 0.0
    rep = 0
    num = 0
    
    infile = open("numbers.txt","r")
    for line in infile:

        num = line.strip()
        num = int(num)
        #print(num)
        
        rep += 1
        total += num
        
        print(f'I read in {rep} number(s) Current number is:  {num} Total is: {total}')
    print(f'Average: {total / 3}')

    pass
    #print(total)
if __name__ == '__main__':
    main()
