a = [[0,1],[2,3]]

print(*a)
print(list(zip(*a)))

print(list(zip([0,1],[2,3])))
print([0,1],[2,3])


matrix = [[1,2,3],[4,5,6],[7,8,9]]
print(matrix.pop(0)) # output [1, 2, 3]

matrix = [[1,2,3],[4,5,6],[7,8,9]]
a = matrix.pop()
print(a) # output [7,8,9]

matrix = [[1,2,3],[4,5,6],[7,8,9]]
print([1] + matrix.pop())
