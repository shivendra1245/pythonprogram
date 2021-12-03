
UserName = input("Enter the Name: ")
Date = input("Enter the Date: ")

letter = '''\nDear <|NAME|>
You Are Selected!
Date - <|DATE|>
'''
letter = letter.replace("<|NAME|>", UserName)
letter = letter.replace("<|DATE|>", Date)
print(letter)
