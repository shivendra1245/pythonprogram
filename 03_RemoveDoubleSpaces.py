
print("\n*****Program To Find Double Spaces*****\n")
MyString = input("Enter A String : ")
hasDoubleSpaces = MyString.find("  ")

if hasDoubleSpaces != -1:

    print("\nThis String Have Double Spaces At Index : ", hasDoubleSpaces)
    AfterReplace = MyString.replace("  ", " ")
    print("\nAfter Replace The String Is : "+AfterReplace)

else:

    print("\n*****This String Haven't Any Double Spaces*****\n")
