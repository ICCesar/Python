# Create calculate_insurance_cost() function below: 
def calculate_insurance_cost(name, age, sex, bmi, num_of_children, smoker):
  estimated_cost = 250 * age - 128 * sex + 370 * bmi + 425 * num_of_children + 24000 * smoker - 12500
  print("The estimated insurance cost for " + name + " is " + str(estimated_cost) + " dollars.")
  return estimated_cost
  return print

# Estimate Maria's insurance cost
maria_insurance_cost = calculate_insurance_cost("Maria", 28, 0, 26.2, 3, 0)

# Estimate Omar's insurance cost 
omar_insurance_cost = calculate_insurance_cost("Omar", 35, 1, 22.2, 0, 1)

# Estimation for X
x_insurance_cost = calculate_insurance_cost("X", 37, 1, 26.2, 0, 0)

def difference_insurance_cost(name_0, name_1):
  diff_cost = name_0 - name_1
  print("The difference in insurance cost is " + str(diff_cost) + " dollars.")
  return diff_cost

difference_insurance_cost(omar_insurance_cost, maria_insurance_cost)
