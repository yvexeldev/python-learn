fav_numbers = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
print(fav_numbers)

unique_letters = set("Mississippi")
print(unique_letters)

fruits = {"apple", "banana", "orange", "kiwi"}
vegetables = {"carrot", "spinach", "broccoli", "banana"}

# Union of fruits and vegetables
print("Union:", fruits.union(vegetables))  # All unique items from both sets

# Intersection of fruits and vegetables
print("Intersection:", fruits.intersection(vegetables))  # Items present in both sets

# Difference between fruits and vegetables
print("Difference (fruits - vegetables):", fruits.difference(vegetables))  # Items only in fruits

# Symmetric difference between fruits and vegetables
print("Symmetric Difference:", fruits.symmetric_difference(vegetables))  # Items in either set, but not both

fav_numbers.add(11)
fav_numbers.remove(10)
print(fav_numbers.pop())
print(fav_numbers)