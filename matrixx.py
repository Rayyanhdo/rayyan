Matrix1=[[1,2,3]
       ,[4,5,6]]
Matrix2=[[1,2,3]
       ,[4,5,6]]

Matrix3 = []

if len(Matrix1) == len(Matrix2)and len(Matrix1[0]) == len(Matrix2[0]) and len(Matrix1[1]) == len(Matrix2[1]):

    for i in range(2):
        for j in range(3):
            Matrix3.append(Matrix1[i][j]+ Matrix2[i][j])
else:
    print("error")

print(Matrix3)
            
            
            
        