import math



def polygonArea ( n_side, side_len):
    area = (n_side * (side_len  ** 2)) / (4 * math.tan((math.pi) / n_side))
    return area
num_side = int(input("enter the number of side: "))
side_length = float(input("enter the length of side:"))
    
p_Area =polygonArea(num_side ,side_length)
print ( "the arae is :" , p_Area)
 