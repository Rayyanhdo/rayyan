
#creat the decationri in list 
contacts = {"Rayan": 1122,
           "Bayan": 2233,
           "Zayana": 6677,
           "Balga": 6655}
#creat new deationri same the last deationri
oldContacts = dict(contacts)
print(oldContacts)

print(oldContacts["Rayan"])
#we cheek this name in c or not 
if "maram" in oldContacts:
    print(oldContacts["maram"])
    
else:
    print("maram not in oldContacts list")

#
number = oldContacts.get("Rayan", 99876)
print("Dial" +str(number))
print("*********************")
#add new key and value in decationri
oldContacts["maram"] = 5599
print (oldContacts)
print("*********************")
#when i want o delet the keys from the decationri
oldContacts.pop("Rayan")
print(oldContacts)
print("*********************")
if "Bayan" in oldContacts:
    oldContacts.pop("Bayan")
print (oldContacts)
print("*********************")
# sorted
print (" My Contacts:")
for key in sorted(oldContacts):
    print(key,oldContacts[key])
    print("*********************")

for item in oldContacts.items( ):
    print(item[0], item[1])
    print("*********************")
    
    
    
    
    