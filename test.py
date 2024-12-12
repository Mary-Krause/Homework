nested_list = []
for i in range(3):
    inner_list = []
    for j in range(3):
        inner_list.append(i * j)
nested_list.append(inner_list)
print(nested_list)