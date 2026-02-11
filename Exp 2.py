print("circle")
print("rectangle")
print("triangle")

c=int(input("choose"))

if c == 1:
     r=float(input("radius:")) 
     print("area=",3.148*r*r)

elif c == 2:
     l = float(input("length"))
     b = float(input("breath"))
     print("area =",l*b)

elif c == 3:
    h = float(input("height"))
    b = float(input("base"))
print("area = ",0.5*b*h)