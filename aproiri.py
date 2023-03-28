from itertools import combinations

#Reading the text file in a list
with open("example.txt", "r") as file:
    nums = [[int(x) for x in line.split()] for line in file]


unique = []
highest_len = 0

#Finding out the unique elements in nums list
for j in range(0, len(nums)):
    for i in range(0,len(nums[j])):
        if nums[j][i] not in unique:
            unique.append(nums[j][i])

#Finding out all the combinations of the unique list
allCombinations = []
for n in range(len(unique) + 1):
    allCombinations += combinations(unique, n)

finalList = []
supports = []
#TypeCasting the tuples in lists
for i in range(0, len(allCombinations)):
    allCombinations[i] = list(allCombinations[i])
    supports.append(0) #Initializing all support counts as 0

#Deleting the first combination because it is an empty set
del allCombinations[0]
del supports[0]

#This loop checks if the combinations are presented in the nums lists or not
for i in range(0, len(nums)):
    for j in range(0, len(allCombinations)):
         check = all(item in nums[i] for item in allCombinations[j])
         if check == True :
             supports[j] = supports[j]+1 #incrementing supports for each match
answer = []
#Omitting all zeroes and taking all non zeroes
for i in range (0, len(allCombinations)):
    if supports[i] !=0:
        answer.append([allCombinations[i],supports[i]])

support = int(input("Enter the value of minimum support : "))

#Generating the output
for i in range(0, len(answer)):
    if answer[i][1] >= support:
        for j in range(0, len(answer[i][0])):
            print(answer[i][0][j],end=" ")
        print("#SUP:",answer[i][1])
