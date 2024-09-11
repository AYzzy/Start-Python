def evenOddCount(number):
    contain =[]
    even =0
    odd = 0
    for num in number:
        if num % 2 != 0:
            odd += 1
        else:
            even+=1
    contain.append(even)
    contain.append(odd)
    return contain

num = {4,6,7,3,5,2,8,9}
print(evenOddCount(num))