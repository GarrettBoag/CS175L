#CS 175 L
#Garrett Boag
#Restaurant
restaurant_list = ['Joe’s Gourmet Burgers', 'Main Street Pizza Company', 'Corner Café', 'Mama’s Fine Italian', 'The Chef’s Kitchen']

veget_yn = input("Is anyone in your party vegetarian?")
vegan_yn = input("Is anyone in your party vegan?")
gluten_yn = input("Is anyone in your party gluten-free?")

if veget_yn == 'yes' or veget_yn == 'Yes':
    restaurant_list.remove('Joe’s Gourmet Burgers')
    if vegan_yn == 'yes' or vegan_yn == 'Yes':
        restaurant_list.remove('Main Street Pizza Company')
        restaurant_list.remove('Mama’s Fine Italian')
    elif gluten_yn == 'yes' or gluten_yn == 'Yes':
        restaurant_list.remove('Mama’s Fine Italian')
else:
    if vegan_yn == 'yes' or vegan_yn == 'Yes':
        restaurant_list.remove('Main Street Pizza Company')
        restaurant_list.remove('Mama’s Fine Italian')
    elif gluten_yn == 'yes' or gluten_yn == 'Yes':
        restaurant_list.remove('Mama’s Fine Italian')
    
#restaurant_list.remove('Joe’s Gourmet Burgers')
#restaurant_list.remove('Main Street Pizza Company')
#restaurant_list.remove('Corner Café')
#restaurant_list.remove('Mama’s Fine Italian')
#restaurant_list.remove('The Chef’s Kitchen')
print(restaurant_list)
