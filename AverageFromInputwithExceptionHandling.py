#Garrett Boag
#3/21/24
#CS 175L 01


def main():

    total = 0.0
    rep = 0
    num = 0
    try:
        infile = open("numbers.txt","r")
        for line in infile:
            try:
                num = line.strip()
                num = int(num)
                rep += 1
                total += num
                
                print(f'I read in {rep} number(s) Current number is:  {num} Total is: {total}')
        
            except ValueError:
                print(f'Bad data: {num} skipping')
    except IOError:
        print('SystemExit: File not found: numbers.txt - existing')
                  
    print(f'Average: {total / 3}')
    pass
    
if __name__ == '__main__':
    main()
