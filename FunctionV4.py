def get_expected_cost(beds, baths, has_basement):
    cost = 80000 + (30000 * beds) + (10000 * baths) + (40000 * has_basement)
    return str(cost)

beds = int(input("how many bedrooms do you have:"))
baths = int(input("how many bathrooms do you have:"))
has_basement = input("do you have a basement:")

if has_basement.lower() in ["y", "yes", "yup"]:
    has_basement = True
else:
    has_basement = False

print("your house value is: " + get_expected_cost(beds, baths, has_basement) + "$")
