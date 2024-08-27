# names= ['Kofi','Ama','Adwoa','Akosua']
# print(list(map(len,names)))


# def too_old(x): return x>30
# ages=[22,25,29,34,56,24,12]
# filtered=list(filter(too_old,ages))
# print(filtered)

# LAMBDA
# items= [1,2,3,4,5]
# squares= map((lambda x: x** 2),items)
# print(list(squares))

def get_even_number(x:int):
    if x % 2==0:
        return x

 
def even_numbers_with_map (numbers:list[int]):
    return map(get_even_number,numbers)

map_values=even_numbers_with_map([1,56,234,87,4,76,24,69,90,135])
print(list(map_values))

# filter
def even_map_filter(numbers:list[int]):
    return filter(get_even_number,numbers)

filtered = even_map_filter([1,56,234,87,4,76,24,69,90,135])
print(list(filtered))

# lamda and filter
numbers= [1,56,234,87,4,76,24,69,90,135]
map_filter = list(filter((lambda x:x%2==0),numbers))
print(map_filter)

# Getting the odd numbers
map_filter = list(filter((lambda x:x%2==1),numbers))
print(map_filter)

# Using the not operation
map_filter = list(filter((lambda x:not(x%2 ==0)),numbers))
print(map_filter)


# def join_strings(words):
#     for word in words:
        

# words = ["hello", "world"]
# helloworld = join_strings(words)
# print(helloworld)

