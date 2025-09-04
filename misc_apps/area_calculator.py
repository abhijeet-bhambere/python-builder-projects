try:
    length = float(input(">>>Enter length: "))
    breadth = float(input(">>>Enter breadth: "))

    if length==breadth:
        exit("That's a square!! 🟨 ")

    area = length * breadth
    print(f"Area of the rectangle is: {area} cm² ▭📏🟪🟪☑️")


except ValueError:
    print("Pls enter valid numeric values.")

