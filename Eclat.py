from itertools import combinations
import itertools

#Defining Functions to find out the maximum 1D list's length
def FindMaxLength(lst):
    maxList = max(lst, key=lambda i: len(i))
    maxLength = len(maxList)
    return maxLength



#Reading the text file in a list
with open("example.txt", "r") as file:
    nums = [[int(x) for x in line.split()] for line in file]

#Finding out the unique elements in nums list
unique = []
j = 0
while(j!=len(nums)):
    for i in range(0,len(nums[j])):
        if nums[j][i] not in unique:
            unique.append(nums[j][i])
    j = j+1

#Finding out all the combinations of the unique list recursively
allCombinations = []
for L in range(FindMaxLength(nums)):
    for subset in itertools.combinations(unique, L):
        allCombinations.append(subset)


finalList = []
supports = []
#TypeCasting the tuples in lists
for i in range(0, len(allCombinations)):
    allCombinations[i] = list(allCombinations[i])
    supports.append(0)



#This loop checks if the combinations are presented in the nums lists or not
for i in range(0, len(nums)):
    for j in range(0, len(allCombinations)):
         check = all(item in nums[i] for item in allCombinations[j])
         if check == True :
             supports[j] = supports[j]+1 #incrementing supports for each match

nonZeroes = []
#Generating relevant elements
for i in range (1, len(allCombinations)):
        nonZeroes.append([allCombinations[i],supports[i]])

input = int(input("Enter the value of minimum support : "))


#The output
for i in range(0, len(nonZeroes)):
    if nonZeroes[i][1] >= input and supports[i]!=0:
        for j in range(0, len(nonZeroes[i][0])):
            print(nonZeroes[i][0][j],end=" ")
        print("#SUP:",nonZeroes[i][1])
