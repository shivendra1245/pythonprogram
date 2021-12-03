
print ("\n*****Program To Recursive function to remove a word from a list and strip it at the same time. (to strip is to remove spaces)*****\n")
def remove_Split(string,word):
    string =string.replace(word,"")
    print(string.strip())


sentence = "        Hello everyone New       "


remove_Split(sentence,"New")