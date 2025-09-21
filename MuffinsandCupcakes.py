#The bakery i work for sells two items muffins and cupcakes the number of items in the store.
Muffins = 10
Cupcakes = 10

while True:
    Order = input('Muffins or Cupcakes:')
    if Order == '0':
        break
    
    Quantity = int(input('How many'))
#calculating remaining stock.
    
    if Order == 'Muffins':
       if Quantity <= Muffins:
           Muffins -= Quantity
           print('Muffins left:', Muffins)
       if Muffins < Quantity:
           print('Out of stock')

    elif Order == 'Cupcakes':
        if Quantity <= Cupcakes:
            Cupcakes -= Quantity
            print('Cupcakes left:', Cupcakes)
        if Cupcakes < Quantity:
            print('Out of stock')
