sentence = input("Please input a sentence: ")
print(sentence)
sentence = sentence.lower()
print("There are", sentence.count('o'), "o's in the sentence")
print("There are", sentence.count('e'), "e's in the sentence")

if sentence.count('o') == sentence.count('e'):
    print("There is an equal amount of o's and e's in the sentence")
else:
    print("There is not an equal amount of o's and e's in the sentence")


