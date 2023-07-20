# in a list we can use the function sum(list) to sum the values

heights = [129, 139, 138, 147, 160]
heights_total = sum(heights)
height_mean = heights_total/len(heights)
print(height_mean)

i = 0
total = 0 
for height in heights:
    total += height
    i +=1

loop_mean = total/i
print(loop_mean)    


# get highest value
# max()
scores = [45, 56, 78, 83, 90, 56, 87,78,45, 78, 99, 87, 46, 35]

max , min = scores[0], scores[0]

for score in scores:
    if score > max:
        max = score
    if score < min:
        min = score
print(max, min)

# For loops with range exclusive end
# 
for num in range(1, 49, 3):
    print(num)


# print every even value between 1 and 100
even = 0 
for num in range(1, 101):
    if(num %2 == 0):
        even += num
print(even)

neven = 0 
for num in range(2, 101, 2):
    neven += num
print(neven)