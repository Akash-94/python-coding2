Employee = {"Name": "John", "Age": 29, "salary": 25000, "Company": "GOOGLE"}

print(type(Employee))

Employee["Country"] = "United States"
Employee["State"] = "Albuquerque"

print(Employee)

print("printing Employee data .... ")

print("Name : %s" % Employee["Name"])
print("Age : %d" % Employee["Age"])
print("Salary : %d" % Employee["salary"])
print("Company : %s" % Employee["Company"])
print("Country : %s" % Employee["Country"])
print("State : %s" % Employee["State"])

print("=" * 50)

Computer = {"Brand": "Apple", "Model": "Mac_Book_Pro", "Screen_Size": "13.6 inch", "Price": "1,13,000 rupees at start",
            "Place of Origin": "California, USA"}

print(type(Computer))

print(Computer)

print("printing Specs.... ")

print("Brand : %s" % Computer["Brand"])
print("Model : %s" % Computer["Model"])
print("Screen_Size : %s" % Computer["Screen_Size"])
print("Price : %s" % Computer["Price"])
print("Place of Origin : %s" % Computer["Place of Origin"])

print()

# 1st remove the error from the above code
# the try to update the entry by providing ur own entries by keyboard input and update the dictionary
