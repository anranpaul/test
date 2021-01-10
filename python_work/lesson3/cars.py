# sort()
cars = ['bmw', 'audi', 'toyota', 'subaru']
cars.sort()
print(cars)

cars.sort(reverse=True)
print(cars)

# can't apply sort
# cars.append(1)
# print(cars)
# cars.sort()
# print(cars)

# sorted()
cars = ['bmw', 'audi', 'toyota', 'subaru']
print("Here is the original list:")
print(cars)
print("\nHere is the sorted list:")
print(sorted(cars, reverse=True))
print("\nHere is the original list again:")
print(cars)
