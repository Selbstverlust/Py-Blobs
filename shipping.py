# Informed weight of the shipped objects.
weight = 41.5

# Ground Shipping
print("Ground Shipping:")
if weight <= 2:
  print(weight * 1.5 + 20)
elif weight > 2 and weight <= 6:
  print(weight * 3 + 20)
elif weight > 6 and weight <= 10:
  print(weight * 4 + 20)
elif weight > 10:
  print(weight * 4.75 + 20)
else:
  print("There is an error with the informed weight.")

# Ground Shipping Premium
print("Ground Shipping Premium:")
print("125.0")

# Drone Shipping
print("Drone Shipping:")
if weight <= 2:
  print(weight * 4.5)
elif weight > 2 and weight <= 6:
  print(weight * 9)
elif weight > 6 and weight <= 10:
  print(weight * 12)
elif weight > 10:
  print(weight * 14.25)
else:
  print("There is an error with the informed weight.")
