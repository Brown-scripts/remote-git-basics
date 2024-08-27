from functools import reduce


'''numbers=[1,2,3,4,5,6,7,8]

def add(a,b):
    sum=a+b
    return sum

print(reduce(add,numbers))'''

# Fold

'''words=['hello',' world']

def join_strings(words):
    sentence=reduce((lambda x,y:x+y),words)
    return sentence

print(join_strings(words))'''

# List Comprehension
'''sentence = "the quick brown fox jumps over the lazy dog"
words = sentence.split()
print([len(word) for word in words])
print([len(word) for word in words if word != "the"])
print([word for word in words if word != "the"])'''

# List out this list containing only positive numbers
'''numbers = [34.6, -203.4, 44.9, 68.3, -12.2, 44.6, 12.7]
def is_positive(x):
    if(x>=0) : return x

print([number for number in numbers if is_positive(number)])'''

# Even numbers

'''numbers = [12, 54, 33, 67, 24, 89, 11, 24, 47]
def is_even(x):
    if x%2==0: return x
    
print([number for number in numbers if is_even(number)])'''

# words with their lengths in a tuple
'''words = ["hello", "my", "name", "is", "Sam"]
print([(word.upper(),len(word)) for word in words])'''





