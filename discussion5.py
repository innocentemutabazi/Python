# Two lists that look the same
list1 = ['apple', 'banana', 'cherry']
list2 = ['apple', 'banana', 'cherry']

print(list1 == list2)  # true (both lists contain the same items)
print(list1 is list2)  # false (they are different lists in memory)

list3 = list1


print(list1 is list3)  # true (both variables refer to the same list)
def add_fruit(basket):
    """Adds 'grape' to the fruit basket."""
    basket.append('grape')

fruit_basket = ['apple', 'banana', 'cherry']
add_fruit(fruit_basket)

print(fruit_basket)  # Output: ['apple', 'banana', 'cherry', 'grape']
