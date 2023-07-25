import math
PI=3.14

sq_weidth = 4
rc_higth = 5
ci_raduies = 2

sq_area = (sq_weidth * sq_weidth) 
rc_area = (0.5 * rc_higth * sq_weidth)
ci_area = (PI * (sq_weidth/ 2) ** 2)

total_area = (sq_area + rc_area) - ci_area
print (total_area)