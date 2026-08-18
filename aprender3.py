bread_price = float(0.50) # bread price variable
bread_quantity = int(input("How many breads do you want? ")) # bread quantity variable
total = (float(bread_price) * int(bread_quantity)) # total to pay variable

print(f"Pay: R${total}") # print the total to pay

customer_money = float(input("How much do you have? R$")) # customer's money variable

if customer_money > total: # condition
    change = (customer_money - total) # change variable
    print(f"Your change is R${change}") # print the change
    print("Thank you for your purchase!") # thank-you print
elif customer_money == total: # condition, elif combines else with if and ensures only one condition runs
    print("Thank you for your purchase!") # thank-you print
else: # opposite condition, if the customer does not have enough money
    print("Insufficient money!") # denial of purchase print