tuple2 = ("orange", [10, 20, 30], [5, 15, 25])
x = []
for i in tuple2:
    x.append(tuple2[1][1])
    x.append([i])
print(x)
