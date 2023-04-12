balance = 1000

print("Welcome to Northern Rock!")
print("Please pick an option from the menu: ")
print("Menu:")

print("1 - Display balance")
print("2 - Withdraw funds")
print("3 - Deposit funds")
print("4 - Return card")

menu_option = int(input("Enter Option: "))

if menu_option == 1:
    print("Your available balance is £", balance)
elif menu_option == 2:
   print("Withdraw amount: 1 - £10, 2 - £20, 3 - £40, 4 - £60, 5 - £80, 6 - £100, 7 - other ")
   withdraw = int(input("Please select withdrawl amount "))
   if withdraw == 1:
       print("You have withdrawn £10. Your new balance is: ", balance - 10)
       print('Choose an option:', menu)
   elif withdraw == 2:
       print("You have withdrawn £20. Your new balance is: ",balance - 20)
   elif withdraw == 3:
       print("You have withdrawn £40. Your new balance is: ",balance - 40)
   elif withdraw == 4:
       print("You have withdrawn £60. Your new balance is: ",balance - 60)
   elif withdraw == 5:
       print("You have withdrawn £80. Your new balance is: ",balance - 80)
   elif withdraw == 6:
       print("You have withdrawn £100. Your new balance is: ",balance - 100)
   elif withdraw == 7:
        other_amount = int(input("How much would you like to withdraw?"))
        if other_amount % 10 !=0:
            print("This machine only gives out £10s")
        elif other_amount < balance: 
            print("You have withdrawn ", other_amount," Your new balance is: ",balance - other_amount)
        else:
            print("You have insufficent funds")    
elif menu_option == 3:
    deposit = int(input("Enter the amount you would like to deposit: "))
    print("Your new balance is: ", balance + deposit) 
elif menu_option == 4:
    print("Here is your card, thank you and Goodbye!")
else:
    print("You have entered an invalid opition, please try again")