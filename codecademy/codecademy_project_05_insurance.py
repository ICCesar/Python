names = ["Judith", "Abel", "Tyson", "Martha", "Beverley", "David", "Anabel"]
estimated_insurance_costs = [1000.0, 2000.0, 3000.0, 4000.0, 5000.0, 6000.0, 7000.0]
actual_insurance_costs = [1100.0, 2200.0, 3300.0, 4400.0, 5500.0, 6600.0, 7700.0]

# Add your code here
# 1 
total_cost = 0

# 2
for insurance_cost in actual_insurance_costs:
  total_cost += insurance_cost
  # 3
  average_cost = total_cost/len(actual_insurance_costs)
  # 4
  print("Average insurance cost: " + str(average_cost) + " dollars.")

# 5
for i in range(len(names)):
  # 6
  name = names[i]
  insurance_cost = actual_insurance_costs[i]
  print("The insurance cost for " + name + " is " + str(insurance_cost) + " dollars.")
  # 7 Check Output
  # 8
  if insurance_cost > average_cost:
    print("The insurance cost for " + name + " is above average.")
  elif insurance_cost > average_cost:
    print("The insurance cost for " + name + " is below average.")
  else:
    print("The insurance cost for " + name + " is equal to the average.")
# 9 Check again
# 10
updated_estimated_costs = [estimated_cost * 11/10 for estimated_cost in estimated_insurance_costs]
# 11
print(updated_estimated_costs)
