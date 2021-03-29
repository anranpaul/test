squares = []
for value in range(1, 11):
    square = value ** 2
    squares.append(square)

print(squares)

min_num = min(squares)
print(min_num)

max_num = max(squares)
print(max_num)

sum_of_numbers = sum(squares)
print(sum_of_numbers)

squares = [value**2 for value in range(1, 10)]
print(squares)
