decName = {1:{"name": "John", "age":27, "sex": "male"},
           2:{"name": "Marie", "age":22, "sex": "famel"},
           3:{"name": "Sali", "age":23, "sex": "famel"}}

#access to diecationri inside diecationri 
for i in decName:
    if decName[i]["age"]>22:
        print (decName[i]["name"])
    