# faculty list
faculty = ["Uzair", "Ali", "Samad", "Usman", "Saifullah"]

# Create an empty list for Cofounders
Cofounders = []

# Identify and move "Usman" and "Saifullah" to Cofounders list
for name in faculty[:]:  # Create a copy of the faculty list to avoid modification during iteration
    if name in ["Usman", "Saifullah"]:
        Cofounders.append(name)
        faculty.remove(name)

# Display the Cofounders list and the updated faculty list
print("Cofounders list:", Cofounders)
print("Updated faculty list:", faculty)

# Locate the index of "Ali" in the list
index_of_ali = faculty.index("Ali")

# Replace "Ali" with "Umair" at that specific index
faculty[index_of_ali] = "Umair"

# Display the corrected "faculty" list
print("Corrected faculty list:", faculty)
