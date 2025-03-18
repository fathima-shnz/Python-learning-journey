weight = int(input("Enter weight: "))
unit = input("Enter unit: ")

if unit == "Kg":
    converted = weight / 0.45
    print (f"{converted} lbs")

elif unit == "lbs":
    converted = weight * 0.45
    print(f"{converted} Kg")
