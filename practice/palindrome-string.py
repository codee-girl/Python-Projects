#using reversed function 
str=input("Enter a String : ")
str.casefold()
rev= reversed(str)

if list(str)==list(rev):
    print("It is palindrome")
else:
    print("Not a palindrome")    

#usine [::-1]):  
string=input(("Enter a string:"))  
if(string==string[::-1]):  
      print("The letter is a palindrome")  
else:  
      print("The letter is not a palindrome")  
