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