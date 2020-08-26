#Ryan Mackenzie
#IT140 - Intro to scripting
#Final Grocery List

#Declaring the empty dictionary and dictionary list.
grocery_item = {}
grocery_history = []
stop = '' #While loop variable that controls if it continues

while stop is not 'q' : #Loops until the user enters q.
  #Three variables collect and store the item information from the user. Sring, int, then a float.
  item_name = input('Item name:\n')
  quantity = input('Quantity purchased:\n')
  cost = input('Price per item:\n')
  #Creates a dictionary item from the previous variables, then adds it to the history list.
  grocery_item = {'name':item_name, 'number':int(quantity), 'price': float(cost)}
  grocery_history.append(grocery_item)
  #Asks the user if they want to add more items, and ends the loop if not.
  stop = input('Would you like to enter another item?\nType \'c\' for continue or \'q\' to quit:\n')

grand_total = 0 #Initilization, will store the final price of all items.
 
for item in grocery_history: #loops through each dictionary entry for each item in the list.
  item_total = item['number'] * item['price'] #Calculates the total cost for the selected item.
  grand_total += item_total
  #prints item statistics
  print(str(item['number'])+' '+item['name']+' @ $' + str(item['price'])+' ea  $'+str(item_total))
  item_total = 0 #resets the item total for each item
  
print('Grand total: $' + str(grand_total)) #Prints the final price

