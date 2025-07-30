motorcycles = ['honda', 'yamaha', 'suzuki', 'ducati']
print(motorcycles)

motorcycles.append('BMW') #add to the list
print(motorcycles)

motorcycles.insert(2, 'mac') #add to the list with location
print(motorcycles)

del motorcycles[2] #removes with location
print(motorcycles)

popped_motorcycle = motorcycles.pop()
print(popped_motorcycle)




too_expensive = 'ducati'
motorcycles.remove(too_expensive)
print(motorcycles)
print(f"\nA {too_expensive.title()} is too expensive for me.")