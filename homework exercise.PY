
# 1. Creating a List
fruits = ["apple", "banana", "mango", "orange"]
print(fruits)

# 2. Accessing Elementsc
colors = ['red', 'blue', 'green', 'yellow', 'purple']
print(colors[0], colors[2], colors[-1])

# 3. Modifying a List
numbers = [10, 20, 30, 40, 50]
numbers[1] = 25  
numbers.append(60)  
print(numbers)

# 4. List Slicing
names = ['Alice', 'Bob', 'Charlie', 'David', 'Emma']
subset = names[:3] 
print(subset)

# 5. Looping through a List
numbers_list1=[1,2,3,4,5,6,7,8,9,10]
print(numbers_list1)

# 6. List Methods: Append and Extend
shopping_cart = []
shopping_cart.append('milk')
shopping_cart.append('bread')
shopping_cart.append('eggs')
shopping_cart.extend(['butter', 'cheese'])
print(shopping_cart)

# 7. Finding Maximum and Minimum in a List
numbers = [45, 22, 88, 56, 92, 33]
print("Maximum:", max(numbers))
print("Minimum:", min(numbers))

# 8. Counting Occurrences
letters = ['a', 'b', 'a', 'c', 'b', 'a', 'd']
count_a = letters.count('a')
print("Occurrences of 'a':", count_a)

# 9. List of Squares of Specific Even Numbers
even_numbers = [2, 4, 6, 8, 10]
even_squares = []
for number in even_numbers:
    square = number * number
    even_squares.append(square)
print(even_squares)



# 10. Removing Duplicates
numbers = [1, 2, 2, 3, 4, 4, 5, 6, 6, 7]
unique_numbers = [] 
for number in numbers: 
    if number not in unique_numbers: 
        unique_numbers.append(number)  
print(unique_numbers)

