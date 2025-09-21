'''Assume each pizza has 8 Slices. Assume that there is a family 4.
Ask how many Slices each person in the family eats.
Then calculate how many pizzas you need to order and
how many pizza Slices are left over after everyone is done eating.'''

# Constant for Slices.
SLICES_PER_PIZZA = 8

# Number of Slices for each family member.
Slices_person1 = int(input('Enter slices for person #1: '))
Slices_person2 = int(input('Enter slices for person #2: '))
Slices_person3 = int(input('Enter slices for person #3: '))
Slices_person4 = int(input('Enter slices for person #4: '))

#Total Slices needed.
Total_Slices = Slices_person1 + Slices_person2 + Slices_person3 + Slices_person4

#Pizzas needed.
Pizzas_needed = Total_Slices // SLICES_PER_PIZZA
if Total_Slices % SLICES_PER_PIZZA != 0:
    Pizzas_needed += 1


#Left over Slices.
Leftover_Slices = (Pizzas_needed * SLICES_PER_PIZZA) - Total_Slices

print('You need', Pizzas_needed, 'Pizzas.')
print('You will have', Leftover_Slices, 'Slices left over.')

                    
                
