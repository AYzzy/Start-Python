numbers = list(range(1, 101))


def is_multiples_of_five(n):
    return n % 5 == 0


result = [n for n in numbers if n % 5 == 0]

# result = []
# for number in numbers:
#   if is_multiples_of_five(number):
#      result.append(number)

print(result)

x = [[_ for _ in range(4)] for _ in range(5)]
print(x)

# y = [_ for _ in range(5)]
# z = []
# for i in y:
#    z.append(y)
#
# print(z)
#
# y = list(range(1,5))
# z = []
# for i in y:
#    z.append(y)
#
# print(z)
#
# y=[]
# z=[]
# for i in range(5):
#     y.append(i)
# for i in y:
#     z.append(y)
# print(z)

for i in range(5):
    for j in range(4):
        x[1][2] = 8
        x[2][3] = 10

print(x)

# Tuple

score = (1, 2, 3, "bimbola", 4.6)
single_tuple = (1,)

print(type(score))

numbers = [1, 2, 3, 4, 5]

print(6 not in numbers)
print(6 in numbers)

# deep learning
# it aligns to the left
print(f'[{'asa':10}]')
# align to the right
print(f'[{2.5:20f}]')

print(f'[{2.5:^20}]')

print(f'[{2.5:+20.2f}] {'asa':20}')

print(f'${20000000:,.2f}')

print('{} {} '.format("miracle", "mystery"))
