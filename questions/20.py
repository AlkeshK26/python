l = [1,3,4,46589,254412,123] 
print (l)
largest = 0
second_largest = 0
for i in range(len(l)):
    if l[i] > largest :
        largest = l[i]
        second_largest = largest

    elif l[i] > second_largest and l[i] != largest:
        second_largest = l[i]

print(second_largest)

             