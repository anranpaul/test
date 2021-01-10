motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)
motorcycles[0] = 'ducati'
print(motorcycles)

#    append()
motorcycles[0] = 'honda'
motorcycles.append('ducati')
print(motorcycles)

#    pop()
poped_motorcycle = motorcycles.pop()
print(motorcycles)
print(poped_motorcycle)

first_motorcycle = motorcycles.pop(0)
print(first_motorcycle)

#    remove()
motorcycles = ['honda', 'yamaha', 'suzuki', 'ducati']
print(motorcycles)
# motorcycles.remove('ducati')
too_expensive = 'ducati'
motorcycles.remove(too_expensive)
print(motorcycles)
