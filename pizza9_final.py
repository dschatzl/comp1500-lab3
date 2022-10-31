#Put it all together to make a program that
#
# 1. Asks the user for a number of pizzas
# 2. Prompts the user to retry if they enter an amount < 1
# 3. If the user orders more than 5 (6 or more) pizzas, tells them they get a free soda
# 4. Asks the user if it is for delivery, and adds the delivery charge if it is
# 5. Prints the total to the user
#
#Here are three example outputs:

#Enter number of pizzas: 2
#Is this for delivery? (yes/no): yes
#Your total is $28

#Enter number of pizzas: 8
#You get a free soda!
#Is this for delivery? (yes/no): yes
#Your total is $100

#Enter number of pizzas: -1
#Enter a positive number: -5
#Enter a positive number: 6
#You get a free soda!
#Is this for delivery? (yes/no): no
#Your total is $72

PRICE_PER_PIZZA = 12
DELIVERY_CHARGE = 4
