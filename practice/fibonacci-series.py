#Program to display the Fibonacci Series to nth 

numbers = int(input("How many numbers do you want ? "))


#STARTING 
n1, n2 = 0, 1
count = 0

#CHECKING IF THE USER INPUT VALIT CONDN OR NOT
if numbers <= 0:
   print("Enter a positive integer")

# if the user enter only one number then return n1
elif numbers == 1:
   print("Fibonacci series is upto",numbers,":")
   print(n1)

#fibonacci series
else:
   print("Fibonacci series:")
   while count < numbers:
       print(n1)
       result = n1 + n2
       # update values
       n1 = n2
       n2 = result
       count += 1