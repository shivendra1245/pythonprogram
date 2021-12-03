
def GreatestOfThree(n1,n2,n3):
    # Comparing 1st and 2nd Number
    if(n1 > n2):
        g = n1
    else:
        g = n2

    # Comparing Greatest and 3rd Number
    if(n3 > g):
        g = n3
    return g
    
print ("\n*****Program to Find The Greatest Number In 3 Numbers Entered By User*****\n")

# Taking Input From User 
n1 = int(input("Enter The Number 1 : "))
n2 = int(input("Enter The Number 2 : "))
n3 = int(input("Enter The Number 3 : "))



print("\nThe Greatest Number Is : ",GreatestOfThree(n1,n2,n3))
    














