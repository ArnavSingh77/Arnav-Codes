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
