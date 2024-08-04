#Decorator allows to modify or extend the behaviour of functions or methods
#without changing their actual code.
def convert_upper(func):
    #def wrapper(word):
    #*args: list of argument
    #**kwargs: dictionaries of arguments
    def wrapper(*args):
        #return func(*args).upper() #processing
        result = func(*args) #call the orignal function
        return tuple(word.upper() for word in result) #Convert each word in tuple to uppercase
    return wrapper
     
@convert_upper  
def show_word(word,word2,word3):
    return word,word2,word3

print(show_word("gaurav","raj", "rajesh"))


def remove_punctuations(func):
    def wrapper():
        return func().replace(","," ")
    return wrapper
"""
@remove_punctuations
def take_sentence():
    sent = input("Enter a sentence: ")
    return sent

print(take_sentence())

"""