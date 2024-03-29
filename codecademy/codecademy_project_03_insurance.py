# Function to estimate insurance cost:
def estimate_insurance_cost(name, age, sex, bmi, num_of_children, smoker):
  estimated_cost = 250*age - 128*sex + 370*bmi + 425*num_of_children + 24000*smoker - 12500
  print(name + "'s Estimated Insurance Cost: " + str(estimated_cost) + " dollars.")
  return estimated_cost
 
# Estimate Maria's insurance cost
maria_insurance_cost = estimate_insurance_cost(name = "Maria", age = 31, sex = 0, bmi = 23.1, num_of_children = 1, smoker = 0)

# Estimate Rohan's insurance cost
rohan_insurance_cost = estimate_insurance_cost(name = 
"Rohan", age = 25, sex = 1, bmi = 28.5, num_of_children = 3, smoker = 0)

# Estimate Valentina's insurance cost
valentina_insurance_cost = estimate_insurance_cost(name = "Valentina", age = 53, sex = 0, bmi = 31.4, num_of_children = 0, smoker = 1)

# Add your code here

# 2
names = ["Maria", "Rohan", "Valentina"]

# 3
insurance_costs = [4150, 5320, 35210]

# 4
insurance_data = zip(names, insurance_costs)
print(insurance_data)

# 5
list(zip(names, insurance_costs))
insurance_data = list(insurance_data)
print(insurance_data)

# 6
estimated_insurance_data = []

# 7
estimated_insurance_data.append(("Maria", maria_insurance_cost))
estimated_insurance_data.append(("Rohan", rohan_insurance_cost))
estimated_insurance_data.append(("Valentina", valentina_insurance_cost))

# 8
print(estimated_insurance_data)

# 9
print("Here is the actual cost data: " + str (insurance_data))

# 10
print("Here is the estimated insurance cost data: " + str(estimated_insurance_data))
