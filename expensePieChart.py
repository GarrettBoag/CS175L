#expensePieChart
#Garrett Boag
#CS 175L

import matplotlib.pyplot as plt

def main():
    cost = []
    needs = []
    try:
        info = open('expenses.txt','r')
    
        for line in info:
            needs_,cost_ = line.strip().split("\t")
            try:
                cost_ = int(cost_)
                cost.append(cost_)
                needs.append(needs_)
            except ValueError:
                print(f'Error(ValueError), the expense "{needs_}" can\'t cost "{cost_}"')
        plt.pie(cost, labels=needs)
    
        plt.title('Monthly Expenses')
        
        plt.show()

    except IOError:
            print('Error(io), file not found')
    
    
if __name__ == '__main__':
    main()
