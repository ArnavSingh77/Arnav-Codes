fruits = ["Watermelon", "Guava", "Strawberry","Mango","Apple"]

#append() :- Adds List Element as value of List.
fruits.append("Pear")
print("Append: ", fruits)
print("")

#insert(a, x) :- This function inserts an element at the position mentioned in its arguments. It takes 2 arguments, position and element to be added at respective position.
fruits.insert(2,"not")
print("Insert: ", fruits)
print("")

#pop() :- This method deletes the element at the position mentioned in its arguments.
fruits.pop(2)
print("Pop: ", fruits)
print("")

#del[a : b] :- This method deletes all the elements in range starting from index ‘a’ till ‘b’ mentioned in arguments.
del fruits[1:3]
print("Del: ", fruits)
print("")

#remove() :- This function is used to delete the first occurrence of number mentioned in its arguments.
fruits.remove("Mango")
print("Remove: ", fruits)
print("")

#sort() :- This function sorts the list in increasing order.
fruits.sort()
print("Sort: ",fruits)
print("")

#reverse() :- This function reverses the elements of list.
fruits.reverse()
print("Reversed: ",fruits)
print("")

#extend(b) :- This function is used to extend the list with the elements present in another list. This function takes another list as its argument.
adj = ['are', 'very', 'good']
fruits.extend(adj)
print("Extend: ",fruits)

#len(list) :- It gives the total length of the list.
print("LEN: ", len(fruits))

'''

This code demonstrates various list manipulation operations in Python using the list named "fruits." Here's a breakdown of what the code does:

1. Appends the string "Pear" to the end of the list using the `append()` method and prints the updated list.
2. Inserts the string "not" at index 2 in the list using the `insert()` method and prints the updated list.
3. Removes the element at index 2 from the list using the `pop()` method and prints the updated list.
4. Deletes elements within the range of index 1 to 3 (excluding 3) using the `del` statement and prints the updated list.
5. Removes the first occurrence of the string "Mango" from the list using the `remove()` method and prints the updated list.
6. Sorts the list in increasing order using the `sort()` method and prints the sorted list.
7. Reverses the order of elements in the list using the `reverse()` method and prints the reversed list.
8. Extends the list with elements from another list `adj` using the `extend()` method and prints the extended list.
9. Prints the length of the list using the `len()` function.

'''
