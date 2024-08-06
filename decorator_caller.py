from decorator_test import remove_punctuations

@remove_punctuations
def take_sentence():
    sent = input("Enter a sentence: ")
    return sent
print(take_sentence())