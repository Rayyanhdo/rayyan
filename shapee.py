import math

#1 Calcation of the regtangl area 
def regtanglArea ( r_length, r_wedgth):
    area = (r_length * r_wedgth)
    return area

#2 Calcation of the squer area 
def scurArea ( s_length ):
    area = (s_length ** 2)
    return area
 
#3 Calcation of the tringal area
def tringalArea ( p_base ,t_length ):
    area = 5.0/( p_base * t_length )
    return area

#4 Calcation of the circle area
def circlArea ( Radius ):
    area = ( Radius** 2 * math.pi )
    return area

#5 Calcation of the cylinder area
def cylinderArea (base ,length):
    area=2*math.pi* base * length
    return area
    
def display_menu():
    print("1.regtangl")
    print("2.squer ")
    print("3.tringal")
    print("4.circle")
    print("5.cylinder")
    

while True:
    
    display_menu()
    user= input("choose the number, or quit: ")
    if user.lower() == 'quit':
        break
    if (user == '1'):
        num_length = int(input("enter the number of side: "))
        num_wedgth = int(input("enter the length of side:"))
        re_Area =regtanglArea(num_length  ,num_wedgth )
        print ( "the arae is :" , re_Area)
    elif (user == '2'):
        side_length = int(input("enter the number of side: "))
        sc_Area =scurArea(side_length )
        print ( "the arae is :" , sc_Area)
    elif (user == '3'):
        sid_length  = int(input("enter the number of side: "))
        sid_base  = int(input("enter the number of base: "))
        tr_Area =tringalArea(sid_length, sid_base )
        print ( "the arae is :" , tr_Area)
    elif (user == '4'):
        Radius = float (input ("Please enter the radius of the given circle: "))
        ci_Area =circlArea(Radius)
        print (" The area of the given circle is: ", ci_Area)
    elif (user == '5'):
        base = int(input("enter the base length: "))
        length = int (input("enter the legth: "))
        cy_Arae = cylinderArea(base, length)
        print (" The area of the given cylinder is: ",  cy_Arae)
    else:
        print("invalid chooise")
        
        
        
        
        
    