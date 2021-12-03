
print("\n*****Program to create a dictionary of Hindi words with values as their English Translation*****\n")
# Creating A Dictionary
Dict = {
    "sanganak": "Computer",
    "dhvani": "Sound",
    "swarg": "Heaven"
}
# Providing Options To User
print("Dictionary Has Option : ", Dict.keys())

# Taking Input From User
userWord = input("\nEnter The Hindi Word From Given Option : ")

# Printing Corresponding English Word
print("\nThe English Word For This Word Is :", Dict[userWord],)
