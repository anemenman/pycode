multi_dim = [[1, 2, 3], [4, 5, 6]]
print(multi_dim)

print(multi_dim[0][0])  # 1
print(multi_dim[1][2])  # 6

print("-----")
for i in range(len(multi_dim)):
    for j in range(len(multi_dim[i])):
        print(multi_dim[i][j])
    print("------")
