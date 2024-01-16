#***********pseudo code*********
# The program will create a list of items in a menu for cafe
# And create 2 dictionaries to save the stock value and price for each item in the menu
# program will used for loop to acess items from dictionaries and perform calculation on the values rferred by keys
# At the end program will display the result calculation on screen

#declare variable for later use
total_stock = 0
item_value = 0
#creating a list called menu
menu = ["waffle", "doghnuts", "cakes", "shake"]
# creating dictionary to store stock value of each item
stock = {'waffle': 7,
         'doghnuts': 2,
         'cakes': 4,
         'shake': 4
        }
# create dictionary to store price of each item in menu
price = {'waffle': 9,
         'doghnuts': 3,
         'cakes': 5,
         'shake': 6
        }

for item in menu:
    # item value is calculated by multiplying the value of stock and price 
    # the value of stock and price is accessed by keys 
    item_value = stock[item] * price[item]
    total_stock += item_value
    
    #print total stock worth on screen
print(f"Total stock worth is   {total_stock} ")
#print(f"Total stock velue is  {item_value}")
    
    

