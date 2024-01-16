# List to Array
import numpy as np
list= []

n=int(input("Enter Number of Elements: "))

for i in range(n):
    val=int(input("Enter Number: "))
    list.append(val)
    arr=np.array(list)
print("The Array is: ", arr)

#Develop a matrix of 3*3 Array using any number range
import numpy as np

arr=np.arange(12,29,2)
arr=arr.reshape(3,3)
print(arr)

#Mean, Median, Mode, Standard Dev, Variance
import statistics as stat

list= [23,5345,12,567,33,6,7,5,34,5,
   5,7,46,23,3,5,357,5,78,34,
   52,35,68,5,67,3,5,24,54,
   57,4,57,4,67,4,67,57,9,
   6,7,345,2,456,46,85,8]

print("The mean is: %.2f"% stat.mean(list))
print("The median is: %.2f"% stat.median(list))
print("The mode is: ", stat.mode(list))
print("The standard deviation is: ", stat.stdev(list))
print("The variance is: ", stat.variance(list))

#Game Rating
import matplotlib.pyplot as plt

games=['Minecraft', 'BGMI', 'Valorant', 'CSGO', 'Fortnite']
rating=[5, 4, 2, 3, 4.8]

bars = plt.bar(games, rating, color=['green','black','red','yellow','blue'])
plt.title("Game Rating")
plt.xlabel("Games")
plt.ylabel("Rating")

# Create a legend
plt.legend(bars, games)

plt.show()
