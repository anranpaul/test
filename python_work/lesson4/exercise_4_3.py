for number in range(1, 21):
    print(number)

odd_nums = list(range(1, 21, 2))
print(odd_nums)
for odd_num in odd_nums:
    print(odd_num)

numbers = []
for number in range(3, 31, 3):
    numbers.append(number)

print(numbers)

triples = [value**3 for value in range(1, 11)]
print(triples)
