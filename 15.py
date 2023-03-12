count = 0 
sum = 0 
product = 1 

# Loop will run infinitely till user presses 'q'
while True:
    # Uncomment user_input = comp_input, Comment user_input = input(...) for magic
    # user_input = comp_input
    user_input = input('Enter a number: ')
    if user_input == ‘q’: break
    user_input = int(user_input)

    # Store the result of addition of prev sum and user input
    sum = sum + user_input
        
    # Store the result of addition of prev sum and user input
    product = product * user_input

    # Count the number of times user gave integer input
    count = count + 1

print('Average:', sum/count)
print('Product:', product)
 