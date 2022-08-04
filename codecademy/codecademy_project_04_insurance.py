names = ["Mohamed", "Sara", "Xia", "Paul", "Valentina", "Jide", "Aaron", "Emily", "Nikita", "Paul"]
insurance_costs = [13262.0, 4816.0, 6839.0, 5054.0, 14724.0, 5360.0, 7640.0, 6072.0, 2750.0, 12064.0]

# 01
names.append("Priscilla")
insurance_costs.append(8320.0)

# 02
medical_records = zip(insurance_costs,names)
list(zip(insurance_costs,names))
medical_records = list(medical_records)

# 03
print(medical_records)

# 04
num_medical_records = len(medical_records)

# 05
print("There are " + str(num_medical_records) + " medical records.")

# 06
first_medical_record = medical_records[0]

# 07
print("Here is the first medical record: " + str(first_medical_record))

# 08
medical_records.sort()
print("Here are the medical records sorted by insurance cost: " + str(medical_records))

# 09
cheapest_three = medical_records[:3]

# 10
print("Here are the three cheapest insurance costs in our medical records: " + str(cheapest_three))

# 11
priciest_three = medical_records[-3:]

# 12
print("Here are the three most expensive insurance costs in our medical records: " + str(priciest_three))

# 13
occurrences_paul = names.count("Paul")
print("There are " + str(occurrences_paul) + " individuals with the name Paul in our medical records.")

# 14
medical_records = (zip(names, insurance_costs))
list(zip(names, insurance_costs))
medical_records = list(medical_records)
medical_records.sort()

middle_five_records = (medical_records[3:8])
