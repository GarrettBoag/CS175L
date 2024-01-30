#Garrett Boag
#stocks.py
#CS 175L 01


commision_purchase = float(input('Enter commission rate percentage (ex 0.03) on stock purchase :'))
commision_sale = float(input("Enter commission rate percentage (ex 0.03) on stock sale :"))
num_of_shares = float(input('Enter number of shares purchased :'))
num_sold = float(input('Enter number of shares sold :'))
price_p_stock = float(input('Enter purchase price per share :'))
sell_price = float(input('Enter sell price per share :'))

#print(commision_purchase, commision_sale, num_of_shares, num_sold, price_p_stock, sell_price)

amount_paid = price_p_stock * num_of_shares
purchase_commission = amount_paid * commision_purchase
amount_sold = num_sold * sell_price
sale_commission = amount_sold * commision_sale
profit = amount_sold - sale_commission - purchase_commission - amount_paid


#print('Amount paid for the stock

print()
print("Amount paid for the stock : ${:,.2f}".format(amount_paid))
print("Commission paid on the purchase : ${:,.2f}".format(purchase_commission))
print("Amount the stock sold for : ${:,.2f}".format(amount_sold))
print("commission paid on the sale : ${:,.2f}".format(sale_commission))
print("Profit (or loss if negative) : ${:,.2f}".format(profit))

