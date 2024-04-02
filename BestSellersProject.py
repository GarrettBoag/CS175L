#CS175L
#Group 1
#Garrett Boag, Andrew Fisher, Gabriella Velasquez 
#BestSellersProject

def main():
    x = book_list()
    print("Read 1138 books")
    menu(x)

def menu(x):
    y_n = True
    while y_n == True:
        print("What would you like to do?")
        print("    1: Look up year range")
        print("    2: Look up month/year")
        print("    3: Search for author")
        print("    4: Search for title")
        print("    Q: Quit")

        choice = input("    > ")
        if choice == 1 or choice == '1':
            start_year = int(input("Enter start year: "))
            end_year = int(input("Enter end year: "))
            display_books_in_year_range(x,start_year,end_year)
        elif choice == 2 or choice == '2':
            month = int(input("Enter month (1-12): "))
            year = int(input("Enter year: "))
            display_books_in_month_year(x, month, year)   
        elif choice == 3 or choice == '3':
            name = input("Enter Author's name: ")
            search_by_author(name,x)
        elif choice == 4 or choice == '4':
            title = input("Enter title: ")
            search_by_title(title,x)       
        elif choice == 'q' or choice == 'Q':
            print('done')
            y_n = False
        else:
            print("I don't understand this command")
            y_n = True


def book_list():
    best_sellers = []
    book = open('bestsellers.txt','r')
    for line in book:
        title,author,publisher,date,genre  = line.strip().split("\t")
        month,day,year = date.split("/")
        best_sellers.append((title,author,publisher,int(month),day,int(year),genre))
    return best_sellers
    print("Read 1138 books")



def search_by_author(name,x):
    for book in x:
         if name in book[1].lower():
             print(f'{book[0]} by: {book[1]} (pub date: {book[3]}/{book[4]}/{book[5]})')

def search_by_title(title,x):
    for book in x:
         if title in book[0].lower():
             print(f'{book[0]} by: {book[1]} (pub date: {book[3]}/{book[4]}/{book[5]})')
             
def display_books_in_month_year(x, first, last):
    for book in x:
        if first == book[3]:
            if last == book[5]:
                print(f'{book[0]} by: {book[1]} (pub date: {book[3]}/{book[4]}/{book[5]})')
        
                
def display_books_in_year_range(x, first, last):
    for book in x:
        if (first <= book[5] and book[5] <= last):
            print(f'{book[0]} by: {book[1]} (pub date: {book[3]}/{book[4]}/{book[5]})')



if __name__ == '__main__':
    main()
    
