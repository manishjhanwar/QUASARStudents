import manufacturing_utilis as utilis

# 1. read_number: accepts any whole number (negatives allowed)
number = utilis.read_number("Enter any whole number: ")
print("read_number returned:", number)

# 2. read_non_negative: rejects negatives
non_negative = utilis.read_non_negative("Enter a non-negative number: ")
print("read_non_negative returned:", non_negative)

# 3. read_production_data: asks for production, defective, unit cost
production, defective, unit_cost = utilis.read_production_data()

print("Good units:", production - defective)
print("Total cost:", production * unit_cost)