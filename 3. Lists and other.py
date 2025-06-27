lst = [1,2,'Python', 3.5, True, None]

print(lst)
print(type(lst))
for i in lst:
    print(i, end=' ')

lst[2] = 'Programming'
print("\nUpdated list:", lst)

lst.append('New Item')

lst.insert(2, 'Inserted Item')
print("List after append and insert:", lst)

lst.remove('New Item')
print("List after removing 'New Item':", lst)

lst2 = lst
lst2.append('Another Item')
print("List 2 after appending 'Another Item':", lst2)
print("List 1 after List 2 modification:", lst)

lst3 = lst.copy()
lst3.append('Copied Item')
print("List 3 after appending 'Copied Item':", lst3)
print("List 1 after List 3 modification:", lst)

num_lst = [1,3,5,7,9,2,4,6,8,0]

new_lst = []

for num in num_lst:
    new_lst.append(num ** 2)

print("New list with squared values:", new_lst)

for i in range(len(new_lst)-1):
    for j in range(i + 1, len(new_lst)):
        if new_lst[i] > new_lst[j]:
            new_lst[i], new_lst[j] = new_lst[j], new_lst[i]
print("Sorted new list:", new_lst)

matrix = [[[1, 2, 3], [4, 5, 6]],
          [[7, 8, 9], [10, 11, 12]],
          [[13, 14, 15], [16, 17, 18]]]

print(matrix[0][1][1])

#2D matrix
matrix_2d = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print("2D Matrix:")
for row in matrix_2d:
    for item in row:
        print(item, end=' ')
    print()

tup = (1, 2, 'Python', 3.5, True, None)
print("Tuple:", tup)
print("Type of tuple:", type(tup))

set = {1, 2, 'Python', 3.5, True, None}
print("Set:", set)
print("Type of set:", type(set))
print("Set after adding an item:", set.add('New Item'))
print("Set after removing an item:", set.remove(2))
print("Set after clearing all items:", set.clear())

dict = {
    'name': 'Python',
    'version': 3.10,
    'is_open_source': True,
    'features': ['dynamic typing', 'easy syntax', 'large community']
}
print("Dictionary:", dict)
print("Type of dictionary:", type(dict))
print("Value of 'name' key:", dict['name'])
print("Keys in dictionary:", dict.keys())

for key, value in dict.items():
    print(f"{key}: {value}")

str = 'abcdefghijklmnopqrstuvwxyz'
output = []
for i in range(len(str)-2):
    output.append(str[i:i+3])
print(output)

# program to find the lcm


# program to find hcf
# program to find sum of cubes of natural numbers