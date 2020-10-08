class vectors:

    def __init__(self,x,y):
        self.x = x
        self.y = y

    def __add__(self,other):
        return vectors(self.x+other.x, self.y + other.y)

    def __sub__(self,other):
        return vectors(self.x-other.x, self.y - other.y)

    def dot(self, other):
        return self.x*other.x + self.y*other.y

    def length(self):
        return (vectors.dot(self,self))**0.5

    def cos(self,other):
        return vectors.dot(self,other)/(vectors.length(self)*vectors.length(other))

    def __str__(self):
        return "<" + str(self.x) + "," + str(self.y) + ">"

def coordinates_v():
    while True:
        try:
            v_x = int(input("Enter 'x' coordinates for v: "))

        except:
            print("That's not a number!")
            continue

        else:
            break

    while True:
        try:
            v_y = int(input("Enter 'y' coordinates for v: "))

        except:
            print("That's not a number!")
            continue

        else:
            break

    return v_x, v_y

def coordinates_w():
    while True:
        try:
            w_x = int(input("Enter 'x' coordinates for w: "))

        except:
            print("That's not a number!")
            continue

        else:
            break

    while True:
        try:
            w_y = int(input("Enter 'y' coordinates for w: "))

        except:
            print("That's not a number!")
            continue

        else:
            break

    return w_x, w_y

print("-----------------VECTOR CALCULATOR-----------------\n")
coord_v = coordinates_v()
print("\n")
coord_w = coordinates_w()
v = vectors(coord_v[0], coord_v[1])
w = vectors(coord_w[0], coord_w[1])
print(f'\nv is: {v}')
print(f'w is: {w}\n')

while True:  ### Main loop for the calculator
    while True: ###Secondary loop to get user input
        try:
             choice = int(input("1.Lenght of v;\n2.Length of w;\n3.Dot product of v and w;\n4.Cosine of the angle between v and w;\n5.Choose new vectors;\n6.Print v and w;\n7.Quit.\n\n"))

        except:
            print("Please pick a number!")
            continue

        else:
            if choice == 1 or choice == 2 or choice == 3 or choice == 4 or choice == 5 or choice == 6 or choice == 7:
                break

            else:
                print("Please pick one of the available options.")

    if choice == 1:
        print(f'\nThe length of v is {v.length()}.\n')
        continue

    elif choice == 2:
        print(f'\nThe length of w is {w.length()}.\n')
        continue

    elif choice == 3:
        print(f'\nThe dot product is {vectors.dot(v,w)}.\n')
        continue

    elif choice == 4:
        print(f'\nThe cosine of the angle between v and w is {round(vectors.cos(v,w),4)}.\n')
        if round(vectors.cos(v,w),4) == 1 or round(vectors.cos(v,w),4) == -1:
            print("Vectors are parallel.\n")

        elif vectors.cos(v,w) == 0:
            print("Vectors are perpendicular.\n")
        continue

    elif choice == 5:
        print("\n")
        coord_v = coordinates_v()
        print("\n")
        coord_w = coordinates_w()
        v = vectors(coord_v[0], coord_v[1])
        w = vectors(coord_w[0], coord_w[1])
        print(f'\nv changed to: {v}')
        print(f'w changed to: {w}\n')
        continue

    elif choice == 6:
        print(f'\nv is: {v}')
        print(f'w is: {w}\n')
        continue

    elif choice == 7:
        print("\nBye!")
        break
